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
from scipy.integrate import odeint
from compute_joint_angles_derivative import compute_joint_angles_derivative
from compute_joints_angles_forward import compute_joints_angles_fd
from compute_q_coords_labels import compute_q_coords_labels
from count_model_DoF import count_model_DoF
from export_analysis_outputs import export_analysis_outputs
from file2dataConst import file2dataConst
from initialize_analysis_variables import initialize_analysis_variables
from read_inertial_parameters import read_inertial_parameters
from solve_equations_of_motion import solve_equations_of_motion
from assemble_mass_matrix import assemble_mass_matrix
from assemble_gravitational_forces import assemble_gravitational_forces
from read_force_file_info import read_force_file_info
from compute_splined_forces import compute_splined_forces
from compute_export_model_loc_coords import compute_export_model_loc_coords


def run_forward_analysis(analysis_type,
                         modeling_file_fpath,
                         model_state_pos_fpath,
                         model_state_vel_fpath,
                         model_force_files_folder_path,
                         model_outputs_folder,
                         fs,
                         t0,
                         tf,
                         widget):
    """

    Function performs the forward dynamic analysis of a multibody system.

    Parameters:
        analysis_type                   :   str
                                            type of analysis to perform (Kinematic, Inverse Dynamic, Musculoskeletal)
        modeling_file_fpath             :   str
                                            absolute path of the modeling file of the multibody system
        model_state_pos_fpath           :   str
                                            absolute path of the file containing the generalized coordinates of the
                                            multibody system for the initial instant
        model_state_vel_fpath           :   str
                                            absolute path of the file containing the generalized velocities of the
                                            multibody system for the initial instant
        model_force_files_folder_path   :   str
                                            absolute path of the folder containing the external force files to apply
                                            to the multibody system
        model_outputs_folder            :   str
                                            absolute path of the folder to export the analysis outcomes
        fs                              :   float
                                            analysis sampling frequency
        t0                              :   float
                                            analysis initial time
        tf                              :   float
                                            analysis final time
        widget                          :   wx.TextCtrl
                                            widget used to export analysis messages and errors

    Returns:


    """

    force_files = [os.path.join(model_force_files_folder_path, x) for x in
                   os.listdir(os.path.join(model_force_files_folder_path)) if x.endswith('.f')]  # [0]

    # Initialize dataConst from '.csv' file
    dataConst = file2dataConst(modeling_file_fpath)

    # Export model local coordinates file
    compute_export_model_loc_coords(modeling_file_fpath, model_outputs_folder)

    # N. rigid bodies
    nRigidBodies = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 1])

    # Get number of model angular drivers
    model_angular_drivers = count_model_DoF(dataConst)['angular_dofs']

    # Get number of model mixed angular drivers
    model_mixed_angular_drivers = count_model_DoF(dataConst)['mixed_dofs']

    # N. of generalized coordinates
    nCoordinates = nRigidBodies * 4 + model_mixed_angular_drivers

    # N. of constraints by type
    nConstraintsByType = len(dataConst[:, 0])

    # N. of angular drivers constraints
    angDriversConstraints = sum([v for k, v in Counter(dataConst[:, 0]).items() if k == 6])

    # N. total lines of dataConst
    totalNumberConstraints = 0

    for key, value in Counter(dataConst[:, 0]).items():
        if key in [1, 2, 3, 4, 5, 7, 10]:
            totalNumberConstraints += value
        else:
            totalNumberConstraints += value * 2

    # Initialize Kinematic Analysis variables
    q, qp, qpp, Phi, niu, gamma, dPhidq = initialize_analysis_variables(nCoordinates, totalNumberConstraints)

    # Model initial position -> 'q Coordinates vector'
    q = np.loadtxt(model_state_pos_fpath, dtype='float', delimiter=',')

    # Model initial velocities -> 'qp Coordinates vector'
    qp = np.loadtxt(model_state_vel_fpath, dtype='float', delimiter=',')

    # Time interval between consecutive frames during kinematic analysis
    dt = 1 / fs

    # Kinematic analysis total number of frames
    nFrames = int((tf - t0) * fs) + 1

    force_total_data = {}

    for _ in range(0, len(force_files)):
        force_data = read_force_file_info(force_files[_])
        key = int(list(force_data.keys())[0])
        force_total_data[_] = {key: force_data[key]}

    # Create splines functions to interpolate and compute the external forces applied during the analysis
    forceSplineFuncs = compute_splined_forces(time, force_total_data, splineDegree=3)

    # tAdjusted final time
    tf_adj = t0 + nFrames * dt

    momentsSplineFuncs = {}

    # Kinematic Analysis Start
    t = t0

    # Get model inertial parameters
    inertial_parameters = read_inertial_parameters(modeling_file_fpath)

    # Compute Baumgarte parameters
    alpha = 1 / float(dt)
    beta = np.sqrt(2) / float(dt)

    # Create initial state vector of the system
    y0 = np.hstack((q, qp))

    # Create the time vector of the forward analysis
    time_span = np.arange(t0, tf_adj, dt)

    #
    sda_Parameters = {}

    widget.Clear()
    widget.SetValue(
        'Forward Dynamic Analysis started at ' + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000 \n")))

    gravitationalForces = assemble_gravitational_forces(dataConst, inertial_parameters)

    massMatrix = assemble_mass_matrix(nRigidBodies, dataConst, inertial_parameters)

    # Perform forward dynamic analysis
    sol = odeint(solve_equations_of_motion,
                 y0,
                 time_span,
                 args=(nRigidBodies,
                       massMatrix,
                       nCoordinates,
                       nConstraintsByType,
                       dataConst,
                       Phi,
                       dPhidq,
                       niu,
                       gamma,
                       alpha,
                       beta,
                       gravitationalForces,
                       forceSplineFuncs,
                       sda_Parameters,
                       momentsSplineFuncs),
                 full_output=0)

    # Write forward dynamic analysis feedback to 'Messages' wxTextCtrl widget
    widget.AppendText(
        'Forward Dynamic Analysis finished at ' + str(time.strftime("%a, %d %b %Y %H:%M:%S +0000 \n")))

    # Assign generalized coordinates to report variable
    q_rep = sol[:, 0:nRigidBodies * 4]

    # Assign generalized velocities to report variable
    qp_rep = sol[:, nRigidBodies * 4:nRigidBodies * 4 + nRigidBodies * 4]

    # Create model joint angles report variable
    joint_angles_rep = np.zeros((q_rep.shape[0], 1))

    # Compute and assign model joints angles to report variable
    for _ in range(0, q_rep.shape[0]):
        joint_angles_header, joint_angles = compute_joints_angles_fd(dataConst, q_rep[_])
        joint_angles_rep[_] = joint_angles

    frames_rep = np.arange(0, nFrames, 1)
    frames_rep = frames_rep.reshape(frames_rep.shape[0], 1)
    time_span = time_span.reshape(time_span.shape[0], 1)

    # Obtain the labels of each generalized coordinate of the model
    model_q_coords_header = compute_q_coords_labels(nRigidBodies, model_mixed_angular_drivers)

    # Compute model joints angles velocity and acceleration
    joint_angles_vel_rep = compute_joint_angles_derivative(joint_angles_rep, 1)
    joint_angles_acc_rep = compute_joint_angles_derivative(joint_angles_rep, 2)

    # Export analysis outputs
    export_analysis_outputs(model_outputs_fpath=os.path.join(model_outputs_folder, analysis_type.lower()
                                                             + '_analysis_outputs.out'),
                            nRigidBodies=nRigidBodies,
                            fs=fs,
                            model_q_header=['#Frame', 'Time'] + model_q_coords_header,
                            q_rep=np.concatenate((frames_rep, time_span, q_rep), axis=1),
                            qp_rep=np.concatenate((frames_rep, time_span, qp_rep), axis=1),
                            model_joints_angles_header=['#Frame', 'Time'] + joint_angles_header,
                            model_joints_angles=np.concatenate((frames_rep, time_span, joint_angles_rep), axis=1),
                            model_joints_ang_vel=np.concatenate((frames_rep, time_span, joint_angles_vel_rep), axis=1),
                            model_joints_ang_acc=np.concatenate((frames_rep, time_span, joint_angles_acc_rep), axis=1),
                            )

    return os.path.join(model_outputs_folder, analysis_type.lower() + '_analysis_outputs.out')


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
