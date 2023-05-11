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
import pandas as pd

from read_angular_driver_info import read_angular_driver_info

def compute_joints_angles_inverse(dataConst, q):
    """

    Function computes the angle for each revolute joint of the multibody system.

    Parameters
    dataConst		:   numpy.array
                        information about the modeling of the multibody system
    q				:   numpy.array
                        vector of generalized coordinates of the multibody system

    Return
    joint_angles	:   numpy.array
                        joint angles of the revolute joints of the multibody system

    """

    # Collects data regarding
    ang_drivers_info = {}
    model_joint_angles_labels = []

    constraints_type_idx = [2,3,4,5,12,13,14,15]
    for row in dataConst:
        for constraint_type in constraints_type_idx:
             read_angular_driver_info(row, constraint_type, ang_drivers_info)

    joint_angles = {}

    for ang_driver in sorted(ang_drivers_info.keys()):
        n_body_1 = ang_drivers_info[ang_driver]['body_1']
        body_1_direction_unit_vector = q[4 * (n_body_1 - 1) + 2:4 * (n_body_1 - 1) + 4]

        if ang_drivers_info[ang_driver]['n_bodies'] == 1:
            body_2_direction_unit_vector = ang_drivers_info[ang_driver]['unit_vec_dir']
            label = 'Body_' + str(n_body_1) + '_Abs_Angle'
            model_joint_angles_labels.append(label)
        elif ang_drivers_info[ang_driver]['n_bodies'] == 2:
            n_body_2 = ang_drivers_info[ang_driver]['body_2']
            body_2_direction_unit_vector = q[4 * (n_body_2 - 1) + 2:4 * (n_body_2 - 1) + 4]
            label = 'Body_' + str(n_body_1) + '_Body_' + str(n_body_2) + '_Angle'
            model_joint_angles_labels.append(label)

        # Compute joint  angle between two model bodies
        body_1_abs_angle = np.arctan2(body_1_direction_unit_vector[1], body_1_direction_unit_vector[0])
        body_2_abs_angle = np.arctan2(body_2_direction_unit_vector[1], body_2_direction_unit_vector[0])
        joint_angle = np.degrees(body_1_abs_angle - body_2_abs_angle)

        # Assign net moment of force to angular driver dictionary
        if ang_driver not in joint_angles.keys():
            joint_angles[ang_driver] = [joint_angle]
        elif ang_driver in joint_angles.keys():
            joint_angles[ang_driver].append(joint_angle)

    joint_angles = pd.DataFrame.from_dict(joint_angles).to_numpy()

    return model_joint_angles_labels, joint_angles

if __name__ == "__main__":

    # doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    from file2dataConst import file2dataConst

    dataConst_fpath = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\test_data_files\trial_0003_1passagem.tsv_FCC\Modeling_File.mod'
    q_fpath = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\test_data_files\trial_0003_1passagem.tsv_FCC\kinematic_analysis_outputs_teste.out'

    dataConst = file2dataConst(dataConst_fpath)
    q_rep = np.loadtxt(q_fpath, dtype='float', delimiter=',')

    for _ in range(0, q_rep.shape[0]):
        angles_labels, angles = compute_joint_angles_inverse(dataConst, q_rep[_])