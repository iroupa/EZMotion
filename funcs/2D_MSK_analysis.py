#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 Ivo Roupa

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ 		= 'Ivo_Roupa'
__copyright__ 	= "Copyright (C) 2023 Ivo Roupa"
__email__ 		= "iroupa@gmail.com"
__license__ 	= "Apache 2.0"

import numpy as np
from collections import Counter
import os
from raw2selectedData import raw2selectedData
from scipy.optimize import minimize
from file2dataConst import file2dataConst
from initialize_analysis_variables import initialize_analysis_variables
from initialize_report_variables import initialize_report_variables
from read_muscle_db import read_muscle_db
from compute_splined_forces import compute_splined_forces
from read_force_file_info import read_force_file_info
from read_inertial_parameters import read_inertial_parameters
from read_DoF_labels import read_DoF_labels
from assemble_mass_matrix import assemble_mass_matrix
from assemble_gravitational_forces import assemble_gravitational_forces
from update_G_vector import update_G_vector
from read_model_data import read_model_data
from compute_spline_coords import compute_spline_coords
from kinematic_analysis import kinematic_analysis
from inverse_dynamics import inverse_dynamics
from compute_joints_angles_inverse import compute_joint_angles
from muscle_analysis import muscle_analysis
from compute_splined_forces_coords import compute_splined_forces_coords
from compute_moments_of_force import compute_moments_of_force
from set_optimization_bounds import set_optimization_bounds
from set_objective_function import objective_function, objective_function_der
from compute_eom_constraints import compute_eom_constraints
import cProfile, pstats, io
from pstats import SortKey

# Subject anthropometric measurements
weight            = 54    # kg
height          = 1.60  # m
segmentlengths  = []
gender          = 'F'
age             = 22
scale_factor = height / 1.74

# Run Inverse Dynamics Analysis?
run_kinematic_analyis = 'yes'

# Run Inverse Dynamics Analysis?
run_inverse_dynamics = 'no'

# Run Muscle Analysis?
run_muscle_analysis = 'no'

# Export data
export_data = False

# Path information
input_folder        = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_6_Dynamics_Indetermined_Systems'
model               = r'trial_0003_1passagem_FCC_act3'
muscle_db_path      = os.path.join(input_folder, model, r'muscle_attachments_original_local_coords_pelvis_corrected_simple.msk')

# Initialize muscle_info
muscles_info = {}

# Dictionary with the number of the bodies to which the muscles are attached
rb_info = {'pelvis'     : 3,
           'femur'      : 8,
           'patella'    : 8,
           'tibia'      : 10,
           'phalanx'    : 12,
           'midfoot'    : 12,
           'hindfoot'   : 12
           }

if run_muscle_analysis == 'yes':
    # Read muscle_db
    muscles_info = read_muscle_db(muscle_db_path, 0.9, rb_info, 65, False)

# Files absolute path
model_file                  = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.mod')][0]
model_dof_data              = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.data')][0]
model_dof_labels            = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.lbl')][0]
model_state                 = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.q')][0]
model_inertial_parameters   = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.mp')][0]
model_force_files           = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.f')]#[0]

# Initialize dataConst from '.txt' file
dataConst = file2dataConst(model_file)

# N. rigid bodies
nRigidBodies = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 1])

# N. of generalized coordinates
nCoordinates = nRigidBodies * 4

# N. of constraints by type
nConstraintsByType= len(dataConst[:, 0])

# N. of angular drivers constraints
angDriversConstraints = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 2 or k == 3])

# N. total lines of dataConst
totalNumberConstraints = 0

for key, value in Counter(dataConst[:, 0]).items():
    if key in [1, 2, 3, 4, 5, 7, 10]:
        totalNumberConstraints += value
    else:
        totalNumberConstraints += value*2

# Read all raw laboratory data
labData = read_model_data(model_dof_data, '', 100, 0.8, '', '')

# Acquisition time data
time = labData.iloc[:, 0]

# Initialize acquisition info variables
rawdata_t0, rawdata_tf, rawdata_nFrames = time.iloc[0], time.iloc[-1], len(time)

# Maximum admissible error
erroMax = 1.e-6

# Initialize Kinematic Analysis variables
q, qp, qpp, Phi, niu, gamma, dPhidq = initialize_analysis_variables(nCoordinates, totalNumberConstraints)

# Simulation Data

# Simple Pendulum Initial position -> 'q Coordinates vector'
q = np.loadtxt(model_state, dtype='float', delimiter=',').flatten()

# Change muscle points coordinates
# muscles_info = change_muscle_coords_body_rf(muscles_info, lines_dic)

# N. muscle coordinates
nb_muscles = len(list(muscles_info.keys()))
        
n_muscle_coordinates = 0

for muscle in muscles_info.keys():
    nb_muscles = len(muscles_info.keys())
    n_muscle_coordinates += 2*nb_muscles # TODO

# Drivers : Column Name Correspondence
# Dictionary with dof number and respective column label in data file
# to be splined and updated in dataConst for each time instant
dof_colName_dict = read_DoF_labels(model_dof_labels)

# Data to be splined
data2spline = raw2selectedData(labData, dof_colName_dict)

# Kinematic Analysis initial time
t0 = 0.0

# Kinematic Analysis final time
tf = labData['Time'].iloc[-2]
# tf = .01

# Frequency during kinematic analysis
fs = 100

# Time interval between consecutive frames during kinematic analysis
dt = 1/fs

# Kinematic analysis total number of frames
nFrames = int((tf-t0)*fs)+1

# tAdjusted final time
tf_adj = t0+(nFrames-1)*dt

# Initialize Kinematic Analysis report variables
t_rep, q_rep, qp_rep, qpp_rep, phi_rep, erro_rep, joint_angles_rep = initialize_report_variables(nFrames, nCoordinates, angDriversConstraints)

joint_angles_vel_rep = np.zeros((joint_angles_rep.shape[0], joint_angles_rep.shape[1]))
joint_angles_acc_rep = np.zeros((joint_angles_rep.shape[0], joint_angles_rep.shape[1]))

if run_muscle_analysis == 'yes':
    # Initialize muscle_rep
    muscle_rep = np.zeros((nFrames, n_muscle_coordinates)) 

# Get data spline and derivatives knots, coefficients and degree
dataSplineFuncs = compute_spline_coords(time, data2spline, splineDegree=3)

force_total_data = {}

for _ in range(0, len(model_force_files)):
    force_data = read_force_file_info(model_force_files[_])
    key = int(list(force_data.keys())[0])
    force_total_data[_] = {key: force_data[key]}

# Create
forceSplineFuncs = compute_splined_forces(time, force_total_data, splineDegree=3)

# Kinematic Analysis Start
t = t0

# Get body segment inertial parameters for subject
InertialParameters = read_inertial_parameters(model_inertial_parameters)

# Create
gravitationalForces = assemble_gravitational_forces(dataConst, InertialParameters)

massMatrix = assemble_mass_matrix(nRigidBodies, dataConst, InertialParameters)

generalized_forces_vector = np.zeros(nCoordinates)

generalized_forces_vector = update_G_vector(generalized_forces_vector, gravitationalForces)

lagrangeMultipliers_rep = np.zeros((nFrames, totalNumberConstraints))

moments_of_force_rep = np.zeros((nFrames, angDriversConstraints))

activation_rep = []

f_ce_rep = []

f_pe_rep = []

fl_component_rep = []

fv_component_rep = []

x_rep = []

muscle_act_rep = []

xo = np.ones(totalNumberConstraints + nb_muscles) * 0.1

itmax = 1

pr = cProfile.Profile()
pr.enable()
for frame in range(0, nFrames-1):
    erro = erroMax
    it = 0

    while erro >= erroMax: 
        
        it += 1
        
        # Kinematic Analysis
        modelKinematics, erro, q = kinematic_analysis(t, nRigidBodies, nCoordinates, nConstraintsByType, dataConst, 
                                                   q, qp, Phi, dPhidq, niu, gamma, erro, dataSplineFuncs)
         
        # To report maximum number of iterations
        if it > itmax:
            itmax += 1
    
    q_rep[frame] = q
        
    # velocity coordinates vector
    qp = np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['niu'], rcond=None)[0]
    
    # acceleration coordinates vector
    qpp = np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['gamma'], rcond=None)[0]

    # Compute joint angles
    joint_angles_rep[frame] = compute_joint_angles(dataConst, q)

    # Update time
    # t = t + dt
    # print('t',t)

    if run_muscle_analysis == 'yes':
        # Muscle analysis
        g_M_pe, g_M_ce, fl_component, fv_component, f_pe, f_ce = muscle_analysis(muscles_info, q, qp, nCoordinates, rb_info)

        f_ce_rep.append(f_ce)
        f_pe_rep.append(f_pe)

        fl_component_rep.append(fl_component)
        fv_component_rep.append(fv_component)

    if run_inverse_dynamics == 'yes' and run_muscle_analysis == 'yes':
        # generalized_forces_vector = compute_splined_Force_Coords(t, q, forceSplineFuncs, generalized_forces_vector)
        generalized_forces_vector = compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector)

        # Inverse Dynamics Analysis without muscles
        lmm = inverse_dynamics(generalized_forces_vector,
                               modelKinematics,
                               massMatrix,
                               qpp,
                               t
                               )

        lagrangeMultipliers_rep[frame] = lmm

        net_moments_of_force = compute_moments_of_force(dataConst, q_rep[frame], lmm, weight)

        moments_of_force_rep[frame] = net_moments_of_force

        # Optimization
        # bnds = define_bounds(totalNumberConstraints, nb_muscles, muscles_info, dataConst)
        bnds = set_optimization_bounds(totalNumberConstraints, nb_muscles, muscles_info, dataConst)

        xo[:totalNumberConstraints] = lmm

        if frame == 0:
           xo[totalNumberConstraints:] = np.ones(nb_muscles) * 0.1

        con = {'type': 'eq',
               'fun': compute_eom_constraints,
               'args': (generalized_forces_vector,
                        dPhidq,
                        massMatrix,
                        qpp,
                        nCoordinates,
                        g_M_pe,
                        g_M_ce)
               }

        sol = minimize(objective_function,
                       xo,
                       args=(totalNumberConstraints,
                             nb_muscles),
                       bounds=bnds,
                       method='SLSQP',
                       jac=objective_function_der,
                       constraints=con,
                       options={'maxiter': 250,
                                'disp': True})
                       # options={'disp': True})

        generalized_forces_vector = np.zeros(nCoordinates)

        muscle_act = sol.x[totalNumberConstraints:]
        xo[totalNumberConstraints:] = muscle_act

        x_rep.append(sol.x)

        muscle_act_rep.append(sol.x[totalNumberConstraints:])

    elif run_inverse_dynamics == 'yes':
        # Update generalized_forces_vector
        generalized_forces_vector = compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector)

        # Inverse Dynamics Analysis
        lmm = inverse_dynamics(generalized_forces_vector,
                               modelKinematics,
                               massMatrix,
                               qpp,
                               t
                               )

        lagrangeMultipliers_rep[frame] = lmm

        ang_driver_info, net_moments_of_force = compute_moments_of_force(dataConst, q_rep[frame], lmm)

        moments_of_force_rep[frame] = net_moments_of_force

        generalized_forces_vector = np.zeros(nCoordinates)

    # Update time
    t = t + dt
    # print('t', np.round(t, 3))

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

# muscles_norm_length = compute_norm_muscle_lengths(q_rep, muscles_info)
#
# header = []
# norm_lenghts = []
#
# for idx in range(0, len(muscles_norm_length.keys())):
#     muscle_label = list(muscles_norm_length[idx].keys())[0]
#     muscle_norm_length = muscles_norm_length[idx][muscle_label]
#     header.append(muscle_label)
#     norm_lenghts.append(muscle_norm_length)
#
# endTime = timer()
# print("Time taken:", str(np.round(endTime - startTime, 2)) + ' seconds.')
#
# ys = joint_angles_rep[:,_].shape[0]
# xs = np.arange(t0, tf, dt)
# if ys != int(xs.shape[0]):
#     xs = np.arange(t0, tf + dt, dt)
#
# for _ in range(0, joint_angles_rep.shape[1]):
#     y = joint_angles_rep[:,_]
#     angle_spline_func       = CubicSpline(xs, y)
#     angular_velocity        = angle_spline_func(xs, 1)
#     angular_acceleration    = angle_spline_func(xs, 2)
#     joint_angles_vel_rep[:, _] = angular_velocity
#     joint_angles_acc_rep[:, _] = angular_acceleration
#

if export_data == True:
    print(os.path.join(input_folder, model, model + '_q_rep_msk.out'))
    fmt = '%.8f'
    np.savetxt(os.path.join(input_folder, model, model + '_q_rep_msk.out'),
               q_rep,
               fmt=fmt,
               delimiter=',')

    np.savetxt(os.path.join(input_folder, model, model + '_qp_rep_msk.out'),
               qp_rep,
               fmt=fmt,
               delimiter=',')

    np.savetxt(os.path.join(input_folder, model, model + '_qpp_rep_msk.out'),
               qpp_rep,
               fmt=fmt,
               delimiter=',')

    np.savetxt(os.path.join(input_folder, model, model + '_joint_angles_rep.out'),
               joint_angles_rep,
               fmt=fmt,
               delimiter=',')

    np.savetxt(os.path.join(input_folder, model, model + '_joint_angles_velocity_rep.out'),
               joint_angles_vel_rep,
               fmt=fmt,
               delimiter=',')

    np.savetxt(os.path.join(input_folder, model, model + '_joint_angles_acceleration_rep.out'),
               joint_angles_acc_rep,
               fmt=fmt,
               delimiter=',')

    if run_inverse_dynamics == True:
        np.savetxt(os.path.join(input_folder, model, model + '_lmm_msk_rep.out'),
                   lagrangeMultipliers_rep,
                   fmt='%.8f',
                   delimiter=',')

        np.savetxt(os.path.join(input_folder, model, model + '_joint_moments_of_force_rep.out'),
                   moments_of_force_rep,
                   fmt=fmt,
                   delimiter=',')

    if run_inverse_dynamics == True and run_muscle_analysis == True:
        np.savetxt(os.path.join(input_folder, model, model + '_x_rep.out'),
                   np.array(x_rep),
                   fmt='%.8f',
                   delimiter=',')

#         np.savetxt(os.path.join(input_folder, model, model + '_fl_component_rep.out'),
#                    np.array(fl_component_rep),
#                    fmt='%.8f',
#                    header=','.join(header),
#                    delimiter=',')
#
#         np.savetxt(os.path.join(input_folder, model, model + '_fv_component_rep.out'),
#                    np.array(fl_component_rep),
#                    header=','.join(header),
#                    fmt='%.8f',
#                    delimiter=',')
#
#         np.savetxt(os.path.join(input_folder, model, model + '_joint_moments_of_force_rep.out'),
#                    moments_of_force_rep,
#                    fmt=fmt,
#                    delimiter=',')
# #
#     header = []
#     for _ in range(0, len(muscles_info.keys())):
#         # print(muscles_info[_]['muscle'], _)
#         header.append(muscles_info[_]['muscle'])
#
#     np.savetxt(os.path.join(input_folder, model, model + '_muscle_activations_rep.out'),
#                np.array(muscle_act_rep),
#                header=','.join(header),
#                fmt='%.8f',
#                delimiter=',')
#
#     np.savetxt(os.path.join(input_folder, model, model + '_muscle_norm_lengths_rep_msk.out'),
#                np.array(norm_lenghts).T,
#                fmt=fmt,
#                header=','.join(header),
#                delimiter=',')
#
    # np.savetxt(os.path.join(input_folder, model, model + '_muscles_norm_lenghts_rep.out'),
    #            compute_norm_muscle_lengths(q_rep, muscles_info),
    #            fmt='%.8f',
    #            delimiter=',')

    # with open (os.path.join(input_folder, model, model + r'_msk_activations_rep.csv'), mode='w', newline='') as activations_file:
    #     activations_writer = csv.writer(activations_file, delimiter=',')
    #     for frame in range(len(x_rep)):
    #         activations_writer. writerow(x_rep[frame][totalNumberConstraints:-1])
