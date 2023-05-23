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

__author__ = 'Ivo_Roupa'
__copyright__ = "Copyright (C) 2023 Ivo Roupa"
__email__ = "iroupa@gmail.com"
__license__ = "Apache 2.0"

import os
import time
from collections import Counter
import numpy as np
from scipy.optimize import minimize
from assemble_gravitational_forces import assemble_gravitational_forces
from assemble_mass_matrix import assemble_mass_matrix
from compute_eom_constraints import compute_eom_constraints
from compute_joint_angles_derivative import compute_joint_angles_derivative
from compute_joints_angles_inverse import compute_joints_angles_inverse
from compute_export_model_loc_coords import compute_export_model_loc_coords
from compute_moments_of_force import compute_moments_of_force
from compute_normalized_muscle_length import compute_norm_muscle_lengths
from compute_q_coords_labels import compute_q_coords_labels
from compute_spline_coords import compute_spline_coords
from compute_splined_forces import compute_splined_forces
from compute_splined_forces_coords import compute_splined_forces_coords
from count_model_DoF import count_model_DoF
from eval_kinematic_constraints import evaluate_kinematic_constraints
from export_analysis_outputs import export_analysis_outputs
from file2dataConst import file2dataConst
from initialize_analysis_variables import initialize_analysis_variables
from initialize_report_variables import initialize_report_variables
from muscle_analysis import muscle_analysis
from raw2selectedData import raw2selectedData
from read_DoF_labels import read_DoF_labels
from read_force_file_info import read_force_file_info
from read_inertial_parameters import read_inertial_parameters
from read_model_input_data import read_model_input_data
from read_model_q import read_model_q
from read_muscle_db import read_muscle_db
from set_objective_function import objective_function, objective_function_der
from set_optimization_bounds import set_optimization_bounds
from update_G_vector import update_G_vector
from compute_moments_of_force_MC import compute_moments_of_force_MC

def run_inverse_analysis(analysis_type,
                         subject_bodymass,
                         modeling_file_fpath,
                         model_data_fpath,
                         model_state_fpath,
                         model_drivers_labels_fpath,
                         inertial_parameters_fpath,
                         model_force_files_fpath,
                         muscle_db_fpath,
                         model_outputs_folder,
                         fs,
                         t0,
                         tf,
                         widget):
    """

    Function performs the kinematic, inverse dynamic or inverse musculoskeletal analysis of a multibody system.

    Parameters:
    analysis_type               :   str
                                    type of analysos to perform (Kinematic, Inverse Dynamic, Musculoskeletal)
    modeling_file_fpath         :   str
                                    absolute path of the modeling file of the multibody system
    model_data_fpath            :   str
                                    absolute path of the file containing the multibody system drives data
    model_state_fpath           :   str
                                    absolute path of the file containing the generalized coodinates of the multibody system for the initial instant
    inertial_parameters_fpath   :   str
                                    absolute path of the file containing the inertial parameters of the multibody system
    model_force_files_fpath     :   str
                                    absolute path of the folder containing the external forces files to apply during the analysis
    muscle_db_fpath             :   str
                                    absolute path of the file containing the parameters of the muscles dataset
    model_outputs_folder        :   str
                                    absolute path of the folder to export the analysis outcomes
    fs                          :   float
                                    analysis sampling frequency
    t0                          :   float
                                    analysis initial time
    tf                          :   float
                                    analysis final time
    widget                      :   wx.TextCtrl
                                    widget used to export analysis messages and errors

    Returns:

    """

    # Dictionary with the number of the bodies to which the muscles are attached
    rb_info = {'pelvis': 3,
               'femur': 8,
               'patella': 8,
               'tibia': 10,
               'phalanx': 12,
               'midfoot': 12,
               'hindfoot': 12
               }

    if analysis_type.lower() == 'musculoskeletal':
        # Read muscle_db
        muscles_info = read_muscle_db(muscle_db_fpath, 0.9, rb_info, 65, False)

    # Create list of force files to apply during the analysis
    if analysis_type.lower() == 'inverse dynamic' or analysis_type.lower() == 'musculoskeletal':
        force_files = [os.path.join(model_force_files_fpath, x) for x in
                       os.listdir(os.path.join(model_force_files_fpath)) if x.endswith('.f')]

    # Initialize dataConst from '.txt' file
    dataConst = file2dataConst(modeling_file_fpath)

    # Export model local coordinates file
    compute_export_model_loc_coords(modeling_file_fpath, model_outputs_folder)

    # N. rigid bodies
    nRigidBodies = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 1])

    # Get number of model angular drivers
    model_angular_drivers = count_model_DoF(dataConst)['angular_dofs']

    # Get number of model mixed angular drivers
    model_mixed_angular_drivers = int(count_model_DoF(dataConst)['mixed_dofs'])

    # N. of generalized coordinates
    nCoordinates = nRigidBodies * 4 + model_mixed_angular_drivers

    # N. of total constraints
    nConstraintsByType = len(dataConst[:, 0])

    # N. of angular drivers constraints
    angDriversConstraints = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 2 or k == 3])

    # N. of ground and revolute joints  constraints
    ground_revolute_DriversConstraints = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 8 or k == 9])

    # N. total lines of dataConst
    totalNumberConstraints = 0

    # Update total number of constraints of the model
    for key, value in Counter(dataConst[:, 0]).items():
        if key in [1, 2, 3, 4, 5, 7, 10]:
            totalNumberConstraints += value
        else:
            totalNumberConstraints += value * 2

    # Read acquisition data
    labData = read_model_input_data(model_data_fpath, filter_data='butter', fs = fs, fc = 8, order = 4)

    # Acquisition time data
    acq_time = labData.iloc[:, 0]

    # Maximum admissible error
    erroMax = 1.e-6

    # Initialize Kinematic Analysis variables
    q, qp, qpp, Phi, niu, gamma, dPhidq = initialize_analysis_variables(nCoordinates, totalNumberConstraints)

    # Read q vector
    q = read_model_q(model_state_fpath)

    if analysis_type.lower() == 'musculoskeletal':
        # Compute number of muscles of the model
        nb_muscles = len(list(muscles_info.keys()))

        # Compute number of muscle coordinates
        n_muscle_coordinates = 0

        # Update number of muscles and respective coordinates
        for muscle in muscles_info.keys():
            nb_muscles = len(muscles_info.keys())
            n_muscle_coordinates += 2 * nb_muscles

    # Drivers : Column Name Correspondence
    # Dictionary with dof number and respective column label in data file
    # to be splined and updated in dataConst for each time instant
    dof_colName_dict = read_DoF_labels(model_drivers_labels_fpath)

    # Data to be splined
    data2spline = raw2selectedData(labData, dof_colName_dict)

    # Time interval between consecutive frames during kinematic analysis
    dt = 1 / fs

    # Kinematic analysis total number of frames
    nFrames = int((tf - t0) * fs) + 1

    # Adjusted final time
    # tf_adj = t0+(nFrames-1)*dt

    # Get data spline and derivatives knots, coefficients and degree
    dataSplineFuncs = compute_spline_coords(acq_time, data2spline, splineDegree=3)

    # Read files of external forces to apply during the analysis
    if analysis_type.lower() == 'inverse dynamic' or analysis_type.lower() == 'musculoskeletal':
        force_total_data = {}

        for _ in range(0, len(force_files)):
            force_data = read_force_file_info(force_files[_])
            key = int(list(force_data.keys())[0])
            force_total_data[_] = {key: force_data[key]}

        # Create splines functions to interpolate and compute the external forces applied during the analysis
        forceSplineFuncs = compute_splined_forces(time, force_total_data, splineDegree=3)

    # Kinematic Analysis Start
    t = t0

    # Get the type of all kinematic contraints of the model
    constraint_types = dataConst[:, 0]

    # Create weights matrix ('W')
    W = np.ones(dPhidq.shape[0])

    # Update weights matrix in case of Mixed Coordinates are used
    if (12 or 13 or 14 or 15) in constraint_types:
        trajectory_drivers_weight = 1.e-5
        trajectory_drivers_idxs = []
        for row in dataConst:
            if int(row[0]) == 6:
                trajectory_drivers_idxs.append(int(row[1]))
                trajectory_drivers_idxs.append(int(row[1]) + 1)

        for idx in trajectory_drivers_idxs:
            W[idx] = trajectory_drivers_weight
        W = np.diag(W)
    else:
        W = np.diag(W)

    if analysis_type.lower() == 'inverse dynamic' or analysis_type.lower() == 'musculoskeletal':
        # Get body segment inertial parameters for subject
        model_inertial_parameters = read_inertial_parameters(inertial_parameters_fpath)

        # Create model mass matrix
        massMatrix = assemble_mass_matrix(nRigidBodies, dataConst, model_inertial_parameters)

        # Create model mass matrix
        gravitational_forces = assemble_gravitational_forces(dataConst, model_inertial_parameters)

        generalized_forces_vector = np.zeros(nCoordinates)

        generalized_forces_vector = update_G_vector(generalized_forces_vector, gravitational_forces)

    # Create report variables
    # Initialize kinematic analysis report variables
    t_rep, q_rep, qp_rep, qpp_rep, phi_rep, erro_rep, joint_angles_rep = initialize_report_variables(nFrames,
                                                                                                     nCoordinates,
                                                                                                     angDriversConstraints)
    # Reshape joint_angles_report variable in case of mixed coordinates are used
    if model_mixed_angular_drivers > 0:
        joint_angles_rep = np.zeros((nFrames, model_mixed_angular_drivers))

    # Initialize inverse dynamic analysis report variables
    if analysis_type.lower() == 'inverse dynamic':
        lmm_rep = np.zeros((nFrames, totalNumberConstraints))
        moments_of_force_rep = np.zeros((nFrames, angDriversConstraints))

    # Initialize musculoskeletal analysis report variables
    if analysis_type.lower() == 'musculoskeletal':
        lmm_rep = np.zeros((nFrames, totalNumberConstraints))
        moments_of_force_rep = np.zeros((nFrames, angDriversConstraints))
        intersegmental_forces_rep = np.zeros((nFrames, nCoordinates))

        muscle_rep = np.zeros((nFrames, n_muscle_coordinates))
        muscle_activations_rep = np.zeros((nFrames, nb_muscles))
        f_ce_rep = []
        f_pe_rep = []
        fl_component_rep = []
        fv_component_rep = []
        x_rep = []
        muscle_act_rep = []

    # Initialize initial vector for musculoskeletal analysis
    if analysis_type.lower() == 'musculoskeletal':
        xo = np.ones(totalNumberConstraints + nb_muscles) * 0.1

    # Start analysis
    for frame in range(0, nFrames):
        erro = erroMax
        it = 0

        # Kinematic Analysis
        while erro >= erroMax:
            widget.AppendText('Kinematic Analysis: ' + 'Frame: ' + str(frame) +
                              ', Iteration: ' + str(it) + ', Error: ' + str(np.format_float_scientific(erro, 3)) + '\n')

            # Evaluate functions: const, Jacobian matrix and vectors niu and gamma
            modelKinematics = evaluate_kinematic_constraints(t,
                                                             nRigidBodies,
                                                             nCoordinates,
                                                             nConstraintsByType,
                                                             dataConst,
                                                             q,
                                                             qp,
                                                             Phi,
                                                             dPhidq,
                                                             niu,
                                                             gamma,
                                                             dataSplineFuncs
                                                             )

            Aw = W.dot(modelKinematics['dPhidq'])
            Bw = W.dot(-modelKinematics['Phi'])

            # Solution
            dq = np.linalg.lstsq(Aw, Bw, rcond=None)[0]

            # Calculate error. Dot product between two vectors returns a scalar
            erro = np.sqrt(np.dot(dq, dq))

            it += 1

            # Update positions with residual value
            q = q + dq

        # Compute model joints angles and obtain respective labels
        joint_angles_header, joint_angles = compute_joints_angles_inverse(dataConst, q[0:nRigidBodies*4])

        # Assign model joints angles to report variable
        joint_angles_rep[frame, :] = joint_angles

        # Assign model generalized coordinates to report variable
        q_rep[frame, :] = q

        # Compute and assign model generalized velocities to report variable
        qp_rep[frame, :] = \
            np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['niu'], rcond=None)[0]

        # Compute and assign model generalized accelerations to report variable
        qpp_rep[frame, :] = \
            np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['gamma'], rcond=None)[0]

        if analysis_type.lower() == 'musculoskeletal':
            # Muscle analysis
            g_M_pe, g_M_ce, fl_component, fv_component, f_pe, f_ce = muscle_analysis(muscles_info, q, qp, nCoordinates,
                                                                                     rb_info)

            f_ce_rep.append(f_ce)
            f_pe_rep.append(f_pe)

            fl_component_rep.append(fl_component)
            fv_component_rep.append(fv_component)

            # Update generalized_forces_vector
            generalized_forces_vector = compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector)

            A = modelKinematics['dPhidq'].T
            b = generalized_forces_vector - massMatrix.dot(qpp)

            # Compute lagrange multipliers
            lmm = np.linalg.lstsq(A, b, rcond=None)[0]

            # Assign model lagrange multipliers to report variable
            lmm_rep[frame] = lmm

            # Compute and assign model intersegmental_forces to report variable
            intersegmental_forces_rep[frame] = (modelKinematics['dPhidq'].T).dot(lmm)

            # Compute and assign model joints moments of force to report variable
            moments_of_force_rep[frame] = compute_moments_of_force(dataConst, q, lmm, subject_bodymass)

            # Set optimization problem bounds
            bnds = set_optimization_bounds(totalNumberConstraints, nb_muscles, muscles_info, dataConst)

            # Assign lagrange multipliers to initial state vector
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
                           options={'maxiter': 500,
                                    'disp': False})

            widget.AppendText('Musculoskeletal Analysis: Frame ' + str(frame) + ' : ' +
                              sol['message'] + ' (Exit mode ' + str(sol['status']) + ' ) ' + '\n' +
                              'Musculoskeletal Analysis: Frame ' + str(
                frame) + ' : ' + ' Current function value: ' + str(sol['fun']) + '\n' +
                              'Musculoskeletal Analysis: Frame ' + str(frame) + ' : ' + ' Number of iterations: ' + str(
                sol['nit']) + '\n' +
                              'Musculoskeletal Analysis: Frame ' + str(
                frame) + ' : ' + ' Number of function evaluations: ' + str(sol['nfev']) + '\n' +
                              'Musculoskeletal Analysis: Frame ' + str(
                frame) + ' : ' + ' Number of gradient evaluations: ' + str(sol['njev']) + '\n')

            # Reset the vector of generalized external forces
            generalized_forces_vector = np.zeros(nCoordinates)

            # Update vector of external generalized forces with the vector of gravtational forces
            generalized_forces_vector = update_G_vector(generalized_forces_vector, gravitational_forces)

            # Update vector of muscle activations
            muscle_act = sol.x[totalNumberConstraints:]

            # Update vector of initial estiamtes for the optimization problem
            xo[totalNumberConstraints:] = muscle_act

            # Append complete solution of optimization problem to report variable
            x_rep.append(sol.x)

            # Assign muscle activations of optimization problem to report variable
            muscle_activations_rep[frame] = sol.x[totalNumberConstraints:]

        if analysis_type.lower() == 'inverse dynamic':
            # Update generalized_forces_vector
            generalized_forces_vector = compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector)

            A = modelKinematics['dPhidq'].T
            b = generalized_forces_vector - massMatrix.dot(qpp)

            # Compute lagrange multipliers of the system for every frame
            lmm = np.linalg.lstsq(A, b, rcond=None)[0]

            # Assign lagrange multipliers vetor to report variable
            lmm_rep[frame] = lmm

            # Compute and assign moments of force of each angular driver to report variable
            if model_mixed_angular_drivers == 0:
                moments_of_force_rep[frame] = compute_moments_of_force(dataConst, q, lmm, subject_bodymass)

            # Reset the vector of generalized external forces
            generalized_forces_vector = np.zeros(nCoordinates)

            # Update vector of external generalized forces with the vector of gravitational forces
            generalized_forces_vector = update_G_vector(generalized_forces_vector, gravitational_forces)

            # Write inverse dynamic analysis feedback to 'Messages' wxTextCtrl widget
            widget.AppendText('Inverse Dynamic Analysis: Frame ' + str(frame) + ' terminated successfully. \n')

        # Update time
        t = t + dt

    # Write analysis feedback to 'Messages' wxTextCtrl widget
    if analysis_type.lower() == 'kinematic':
        widget.AppendText(
            'Kinematic Analysis finished at ' + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000 \n")))
    elif analysis_type.lower() == 'inverse dynamic':
        widget.AppendText(
            'Inverse Dynamic Analysis finished at ' + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000 \n")))
    elif analysis_type.lower() == 'musculoskeletal':
        widget.AppendText(
            'Musculoskeletal Inverse Dynamic Analysis finished at ' + str(
                time.strftime("%a, %d %b %Y %H:%M:%S +0000 \n")))

    # Create outputs folder
    if not os.path.isdir(model_outputs_folder):
        os.mkdir(model_outputs_folder)

    frames_rep = np.arange(0, nFrames, 1)
    frames_rep = frames_rep.reshape(frames_rep.shape[0], 1)
    time_rep = np.arange(0, nFrames / fs, 1 / fs)
    time_rep = time_rep.reshape(time_rep.shape[0], 1)

    # Obtain the labels of each generalized coordinate of the model
    model_q_coords_header = compute_q_coords_labels(nRigidBodies, model_mixed_angular_drivers)

    # Compute joints angles velocity and acceleration
    joint_angles_vel_rep = compute_joint_angles_derivative(joint_angles_rep, t0, tf, dt, 1)
    joint_angles_acc_rep = compute_joint_angles_derivative(joint_angles_rep, t0, tf, dt, 2)

    # Export analysis outputs
    if analysis_type.lower().strip() == 'kinematic':
        # Export kinematic analysis outputs
        export_analysis_outputs(
            model_outputs_fpath=os.path.join(model_outputs_folder, analysis_type.lower() + '_analysis_outputs.out'),
            nRigidBodies=nRigidBodies,
            fs=fs,
            model_q_header=['# Frame', 'Time'] + model_q_coords_header,
            q_rep=np.concatenate((frames_rep, time_rep, q_rep), axis=1),
            qp_rep=np.concatenate((frames_rep, time_rep, qp_rep), axis=1),
            qpp_rep=np.concatenate((frames_rep, time_rep, qpp_rep), axis=1),
            model_joints_angles_header=['# Frame', 'Time'] + joint_angles_header,
            model_joints_angles=np.concatenate((frames_rep, time_rep, joint_angles_rep), axis=1),
            model_joints_ang_vel=np.concatenate((frames_rep, time_rep, joint_angles_vel_rep), axis=1),
            model_joints_ang_acc=np.concatenate((frames_rep, time_rep, joint_angles_acc_rep), axis=1),
        )

    elif analysis_type.lower() == 'inverse dynamic':
        # Compute model joints power
        joint_powers_rep = joint_angles_vel_rep * moments_of_force_rep

        # Get the labels for the moments of force and power of each joint of the model
        joints_moments_of_force_header = []
        joints_powers_header = []
        for _ in joint_angles_header:
            joints_moments_of_force_header.append(_.replace('Angle', 'Joint_Moment_of_Force'))
            joints_powers_header.append(_.replace('Angle', 'Joint_Power'))

        # Export inverse dynamic analysis outputs
        export_analysis_outputs(
            model_outputs_fpath=os.path.join(model_outputs_folder, analysis_type.lower() + '_analysis_outputs.out'),
            nRigidBodies=nRigidBodies,
            fs=fs,
            model_q_header=['# Frame', 'Time'] + model_q_coords_header,
            q_rep=np.concatenate((frames_rep, time_rep, q_rep), axis=1),
            qp_rep=np.concatenate((frames_rep, time_rep, qp_rep), axis=1),
            qpp_rep=np.concatenate((frames_rep, time_rep, qpp_rep), axis=1),
            model_joints_angles_header=['# Frame', 'Time'] + joint_angles_header,
            model_joints_angles=np.concatenate((frames_rep, time_rep, joint_angles_rep), axis=1),
            model_joints_ang_vel=np.concatenate((frames_rep, time_rep, joint_angles_vel_rep), axis=1),
            model_joints_ang_acc=np.concatenate((frames_rep, time_rep, joint_angles_acc_rep), axis=1),
            model_joints_moments_of_force_header = ['# Frame', 'Time'] + joints_moments_of_force_header,
            model_joints_moments_of_force=np.concatenate((frames_rep, time_rep, moments_of_force_rep), axis=1),
            model_joints_powers_header=['# Frame', 'Time'] + joints_powers_header,
            model_joints_powers = np.concatenate((frames_rep, time_rep, joint_powers_rep), axis=1),
        )

    elif analysis_type.lower().strip() == 'musculoskeletal':
        # Get the labels for the moments of force and power of each joint of the model
        joints_moments_of_force_header = []
        joints_powers_header = []
        for _ in joint_angles_header:
            joints_moments_of_force_header.append(_.replace('Angle', 'Joint_Moment_of_Force'))
            joints_powers_header.append(_.replace('Angle', 'Joint_Power'))

        # Compute model joints power
        joint_powers_rep = joint_angles_vel_rep * moments_of_force_rep

        # Compute the normalized length of each muscle of the model and respective label
        model_muscles_header, muscles_norm_length = compute_norm_muscle_lengths(q_rep, muscles_info)

        # Export musculoskeletal analysis outputs
        export_analysis_outputs(
            model_outputs_fpath=os.path.join(model_outputs_folder, analysis_type.lower() + '_analysis_outputs.out'),
            nRigidBodies=nRigidBodies,
            fs=fs,
            model_q_header=['# Frame', 'Time'] + model_q_coords_header,
            q_rep=np.concatenate((frames_rep, time_rep, q_rep), axis=1),
            qp_rep=np.concatenate((frames_rep, time_rep, qp_rep), axis=1),
            qpp_rep=np.concatenate((frames_rep, time_rep, qpp_rep), axis=1),
            model_joints_angles_header=['# Frame', 'Time'] + joint_angles_header,
            model_joints_angles=np.concatenate((frames_rep, time_rep, joint_angles_rep), axis=1),
            model_joints_ang_vel=np.concatenate((frames_rep, time_rep, joint_angles_vel_rep), axis=1),
            model_joints_ang_acc=np.concatenate((frames_rep, time_rep, joint_angles_acc_rep), axis=1),
            model_joints_moments_of_force_header=['# Frame', 'Time'] + joints_moments_of_force_header,
            model_joints_moments_of_force=np.concatenate((frames_rep, time_rep, moments_of_force_rep), axis=1),
            model_joints_powers_header = ['# Frame', 'Time'] + joints_powers_header,
            model_joints_powers = np.concatenate((frames_rep, time_rep, joint_powers_rep), axis=1),
            model_muscles_header=['# Frame', 'Time'] + model_muscles_header,
            model_muscles_normalized_length = np.concatenate((frames_rep, time_rep, muscles_norm_length), axis=1),
            model_muscle_activations=np.concatenate((frames_rep, time_rep, muscle_activations_rep), axis=1),
        )

    return os.path.join(model_outputs_folder, analysis_type.lower() + '_analysis_outputs.out')
if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)