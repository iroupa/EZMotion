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

    # Dictionary to store information about angular drivers
    ang_drivers_info = {}

    # List to store labels of joint angles
    model_joint_angles_labels = []

    constraints_type_idx = [2, 3, 4, 5, 12, 13, 14, 15]

    # Iterate through each row of dataConst
    for row in dataConst:
        # Check for specific constraint types related to angular drivers
        for constraint_type in constraints_type_idx:
            # Read and store angular driver information
            read_angular_driver_info(row, constraint_type, ang_drivers_info)

    # Dictionary to store joint angles
    joint_angles = {}

    for ang_driver in sorted(ang_drivers_info.keys()):
        # Obtain body 1 number
        n_body_1 = ang_drivers_info[ang_driver]['body_1']

        # Obtain body 1 direction vector
        body_1_direction_unit_vector = q[4 * (n_body_1 - 1) + 2:4 * (n_body_1 - 1) + 4]

        if ang_drivers_info[ang_driver]['n_bodies'] == 1:
            # Obtain body 2 direction vector
            body_2_direction_unit_vector = ang_drivers_info[ang_driver]['unit_vec_dir']

            # Create angle label
            label = 'Body_' + str(n_body_1) + '_Abs_Angle'

            # Store information about the joint angle label in model_joint_angles_labels list
            model_joint_angles_labels.append(label)

        elif ang_drivers_info[ang_driver]['n_bodies'] == 2:
            # Obtain body 2 number
            n_body_2 = ang_drivers_info[ang_driver]['body_2']

            # Obtain body 2 direction vector
            body_2_direction_unit_vector = q[4 * (n_body_2 - 1) + 2:4 * (n_body_2 - 1) + 4]

            # Create angle label
            label = 'Body_' + str(n_body_1) + '_Body_' + str(n_body_2) + '_Angle'

            # Store information about the joint angle label in model_joint_angles_labels list
            model_joint_angles_labels.append(label)

        # Compute joint angle between two model bodies
        body_1_abs_angle = np.arctan2(body_1_direction_unit_vector[1], body_1_direction_unit_vector[0])
        body_2_abs_angle = np.arctan2(body_2_direction_unit_vector[1], body_2_direction_unit_vector[0])
        joint_angle = np.degrees(body_1_abs_angle - body_2_abs_angle)

        # Assign net moment of force to angular driver dictionary
        if ang_driver not in joint_angles.keys():
            joint_angles[ang_driver] = [joint_angle]
        elif ang_driver in joint_angles.keys():
            joint_angles[ang_driver].append(joint_angle)

    # Convert the dictionary to a numpy array
    joint_angles = pd.DataFrame.from_dict(joint_angles).to_numpy()

    # Return model joint labels and angles
    return model_joint_angles_labels, joint_angles


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
