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


def export_analysis_outputs_fd(model_outputs_fpath, model, nRigidBodies, fs, model_angular_drivers,
                               model_mixed_angular_drivers, q_rep, qp_rep, model_joint_angles,
                               model_joint_ang_vel, model_joint_ang_acc):
    """
    
    Function exports kinematic, dynamic and musculoskeletal analysis outputs to csv file.

    Parameters:
        model_outputs_fpath: string :   string
                                        absolute path of the model outputs file
        model                       :   string
                                        model label    
        nRigidBodies                :   int
                                        number of rigid bodies of the multibody system
        fs                          :   float
                                        sampling frequency
        model_angular_drivers       :   int
                                        number of angular drivers of the multibody system       
        model_mixed_angular_drivers :   int
                                        number of mixed angular drivers of the multibody system
        q_rep                       :   numpy.ndarray
                                        generalized coordinates of the multibody system
        qp_rep                      :   numpy.ndarray
                                        generalized velocities of the multibody system
        qpp_rep                     :   numpy.ndarray
                                        generalized accelerations of the multibody system
        model_joint_angles          :   numpy.ndarray
                                        joint angles of each revolute joint of the multibody system
        model_joint_ang_vel         :   numpy.ndarray
                                        joint angular velocities of each revolute joint of the multibody system
        model_joint_ang_acc         :   numpy.ndarray
                                        joint angular accelerations of each revolute joint of the multibody system
        moments_of_force            :   numpy.ndarray
                                        net moments of force of each revolute joint of the multibody system
        muscle_activations          :   numpy.ndarray
                                        muscle activations of each muscle of the multibody system

    Returns:

    """

    coordinates_list = [q_rep,
                        qp_rep]

    coordinates_list_labels = ['# ***** Coordinates [m] *****',
                               '# ***** Velocities [m.s-1] *****']

    angles_list = [model_joint_angles,
                   model_joint_ang_vel,
                   model_joint_ang_acc]

    angles_list_labels = ['# ***** Angles [deg] *****',
                          '# ***** Angles Velocities [deg.s-1] *****',
                          '# ***** Angles Accelerations [deg.s-2] *****']

    with open(model_outputs_fpath, 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Write file header
        writer.writerow(['# Model:' + str(model)])
        writer.writerow(['# Number_of_Rigid_Bodies:' + str(nRigidBodies)])
        writer.writerow(['# Number_of_Frames:' + str(q_rep.shape[0] - 1)])
        writer.writerow(['# Sampling_Frequency:' + str(int(fs))])
        writer.writerow([])

        if isinstance(q_rep, np.ndarray):
            # Append segments coordinates and velocities
            output_file_data_header = []
            for _ in range(0, nRigidBodies):
                if _ == 0:
                    output_file_data_header += ['# Body_' + str(_ + 1) + '_X']
                else:
                    output_file_data_header += ['Body_' + str(_ + 1) + '_X']
                output_file_data_header += ['Body_' + str(_ + 1) + '_Y']
                output_file_data_header += ['Body_' + str(_ + 1) + '_Ux']
                output_file_data_header += ['Body_' + str(_ + 1) + '_Uy']
            for idx in range(0, len(coordinates_list)):
                for frame in range(0, coordinates_list[idx].shape[0] - 1):
                    if frame == 0:
                        writer.writerow([coordinates_list_labels[idx]])
                        for _ in range(0, model_mixed_angular_drivers):
                            output_file_data_header += ['Mixed_Ang_Driver_' + str(_ + 1)]
                        writer.writerow(output_file_data_header)
                    else:
                        writer.writerow(np.around(coordinates_list[idx][frame], decimals=4))
                writer.writerow([])

        if isinstance(model_joint_angles, np.ndarray):
            # Append joints angles, angular velocities and angular accelerations
            output_file_data_header = []
            for _ in model_angular_drivers:
                output_file_data_header += [str(_)]
            for idx in range(0, len(angles_list)):
                for frame in range(0, angles_list[idx].shape[0] - 1):
                    if frame == 0:
                        writer.writerow([angles_list_labels[idx]])
                        writer.writerow(output_file_data_header)
                    else:
                        writer.writerow(np.around(angles_list[idx][frame], decimals=4))
                writer.writerow([])


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
