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

import csv
import numpy as np


def export_analysis_outputs(model_label='',
                            model_outputs_fpath='',
                            nRigidBodies='',
                            fs='',
                            model_q_header='',
                            q_rep='',
                            qp_rep='',
                            qpp_rep='',
                            model_joints_angles_header='',
                            model_joints_angles='',
                            model_joints_ang_vel='',
                            model_joints_ang_acc='',
                            model_joints_moments_of_force_header='',
                            model_joints_moments_of_force='',
                            model_joints_powers_header='',
                            model_joints_powers='',
                            model_muscles_header='',
                            model_muscles_normalized_length='',
                            model_muscle_activations=''
                            ):
    """

    Function exports kinematic, dynamic and musculoskeletal analysis outputs to .out file.

    Parameters:
        model_label                             :   string
                                                    model label
        model_outputs_fpath: string             :   string
                                                    absolute path of the model outputs file
        nRigidBodies                            :   int
                                                    number of rigid bodies of the multibody system
        fs                                      :   float
                                                    sampling frequency
        model_q_header                          :   list
                                                    label of each generalized coordinate of the model,
                                                    including mixed coordinates
        q_rep                                   :   numpy.ndarray
                                                    generalized coordinates of the multibody system
        qp_rep                                  :   numpy.ndarray
                                                    generalized velocities of the multibody system
        qpp_rep                                 :   numpy.ndarray
                                                    generalized accelerations of the multibody system
        model_joints_angles_header              :   list
                                                    label of each joint angle of the multibody system
        model_joints_angles                     :   numpy.ndarray
                                                    joint angles of each revolute joint of the multibody system
        model_joints_ang_vel                    :   numpy.ndarray
                                                    joint angular velocities of each revolute joint of the
                                                    multibody system
        model_joints_ang_acc                    :   numpy.ndarray
                                                    joint angular accelerations of each revolute joint of the
                                                    multibody system
        model_joints_moments_of_force_header    :   list
                                                    label of each joint moment of the multibody system
        model_joints_moments_of_force           :   numpy.ndarray
                                                    net moments of force of each revolute joint of the multibody system
        model_joints_powers_header              :   list
                                                    label of each joint power of the multibody system
        model_joints_powers                     :   numpy.ndarray
                                                    power of each joint of the multibody system
        model_muscles_header                    :   list
                                                    label of each muscle of the multibody system
        model_muscles_normalized_length         :   numpy.ndarray
                                                    normalized length of each muscle of the multibody system
        model_muscle_activations                :   numpy.ndarray
                                                    muscle activations of each muscle of the multibody system

    Returns:

    """

    with open(model_outputs_fpath, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Write file header
        writer.writerow(['# Model:' + str(model_label)])
        writer.writerow(['# Number_of_Rigid_Bodies:' + str(nRigidBodies)])
        writer.writerow(['# Number_of_Frames:' + str(q_rep.shape[0])])
        writer.writerow(['# Sampling_Frequency:' + str(int(fs))])
        writer.writerow([])

        if isinstance(q_rep, np.ndarray):
            # Export model generalized coordinates
            writer.writerow(['# ***** Coordinates [m] *****'])
            writer.writerow(model_q_header)
            for frame in range(0, q_rep.shape[0]):
                writer.writerow(np.around(q_rep[frame], decimals=4))
            writer.writerow([])

        if isinstance(qp_rep, np.ndarray):
            # Export model generalized velocities
            writer.writerow(['# ***** Velocities [m.s^-1] *****'])
            writer.writerow(model_q_header)
            for frame in range(0, qp_rep.shape[0]):
                writer.writerow(np.around(qp_rep[frame], decimals=4))
            writer.writerow([])

        if isinstance(qpp_rep, np.ndarray):
            # Export model generalized accelerations
            writer.writerow(['# ***** Accelerations [m.s^-2] *****'])
            writer.writerow(model_q_header)
            for frame in range(0, qpp_rep.shape[0]):
                writer.writerow(np.around(qpp_rep[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_joints_angles, np.ndarray):
            # Export model generalized accelerations
            writer.writerow(['# ***** Angles [deg] *****'])
            writer.writerow(model_joints_angles_header)
            for frame in range(0, model_joints_angles.shape[0]):
                writer.writerow(np.around(model_joints_angles[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_joints_ang_vel, np.ndarray):
            # Export model joints angular velocities
            writer.writerow(['# ***** Angles Velocities [deg.s^-1] *****'])
            writer.writerow(model_joints_angles_header)
            for frame in range(0, model_joints_ang_vel.shape[0]):
                writer.writerow(np.around(model_joints_ang_vel[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_joints_ang_acc, np.ndarray):
            # Export model joints angular accelerations
            writer.writerow(['# ***** Angles Accelerations [deg.s^-2] *****'])
            writer.writerow(model_joints_angles_header)
            for frame in range(0, model_joints_ang_acc.shape[0]):
                writer.writerow(np.around(model_joints_ang_acc[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_joints_moments_of_force, np.ndarray):
            # Export model joints moments of force
            writer.writerow(['# ***** Moments of Force [N.m] *****'])
            writer.writerow(model_joints_moments_of_force_header)
            for frame in range(0, model_joints_moments_of_force.shape[0]):
                writer.writerow(np.around(model_joints_moments_of_force[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_joints_powers, np.ndarray):
            # Export model joints powers accelerations
            writer.writerow(['# ***** Joints Powers [W] *****'])
            writer.writerow(model_joints_powers_header)
            for frame in range(0, model_joints_powers.shape[0]):
                writer.writerow(np.around(model_joints_powers[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_muscles_normalized_length, np.ndarray):
            # Export model muscles normalized length
            writer.writerow(['# ***** Muscles normalized length [%] *****'])
            writer.writerow(model_muscles_header)
            for frame in range(0, model_muscles_normalized_length.shape[0]):
                writer.writerow(np.around(model_muscles_normalized_length[frame], decimals=4))
            writer.writerow([])

        if isinstance(model_muscle_activations, np.ndarray):
            # Export model muscles activations
            writer.writerow(['# ***** Muscles Activations [%] *****'])
            writer.writerow(model_muscles_header)
            for frame in range(0, model_muscle_activations.shape[0]):
                writer.writerow(np.around(model_muscle_activations[frame], decimals=4))
            writer.writerow([])


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
