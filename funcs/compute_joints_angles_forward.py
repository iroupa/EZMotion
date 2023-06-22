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


def compute_joints_angles_fd(dataConst, q):
    """

    Function computes the angle for each revolute joint of the multibody system during the forward analysis.

    Parameters:
        dataConst		:   numpy.array
                            information about the modeling of the multibody system
        q				:   numpy.array
                            vector of generalized coordinates of the multibody system

    Returns:
        joint_angles	:   numpy.array
                            joint angles of the revolute joints of the multibody system

    """

    # Dictionary to store joint angles
    model_joint_angles = {}

    # List to store labels of joint angles
    model_joint_angles_labels = []

    # Dictionary to store information about joints
    joints_info = {}

    # Counter for joints
    joint_counter = 0

    # Iterate through the rows of dataConst
    for row in range(0, dataConst.shape[0]):
        # Check for ground joint constraint (idx = 8)
        if int(dataConst[row, 0]) == 8:
            # Store information about the joint with ground in joints_info dictionary
            joints_info[joint_counter] = {'body_1': int(dataConst[row, 1]), 'body_2': 'ground'}
            joint_counter += 1

        # Check for revolute joints constraint (idx == 9)
        if int(dataConst[row, 0]) == 9:
            # Store information about the joint in joints_info dictionary
            joints_info[joint_counter] = {'body_1': int(dataConst[row, 1]), 'body_2': int(dataConst[row, 2])}
            joint_counter += 1

    # Iterate through the joints in joints_info
    for _ in range(0, len(joints_info.keys())):
        body_1 = joints_info[_]['body_1']
        body_2 = joints_info[_]['body_2']

        if body_2 == 'ground':
            # Calculate joint angle for a joint with ground
            body_1_q = q[(int(body_1)-1) * 4: (int(body_1)-1) * 4 + 4]
            angle = np.arctan2(body_1_q[3], body_1_q[2])

            # Create joint angle label
            label = 'Body_' + str(body_1) + '_Abs_Angle'

            # Store information about the joint angle in model_joint_angles dictionary
            model_joint_angles[label] = float((np.degrees(angle)))

            # Store information about the joint angle label in model_joint_angles_labels list
            model_joint_angles_labels.append(label)
        else:
            # Calculate joint angle for a joint between two bodies
            body_1_q = q[(int(body_1)-1) * 4: (int(body_1)-1) * 4 + 4]
            body_2_q = q[(int(body_2)-1) * 4: (int(body_2)-1) * 4 + 4]
            angle = np.arctan2(body_1_q[3], body_1_q[2]) - np.arctan2(body_2_q[3], body_2_q[2])

            # Create joint angle label
            label = 'Body_' + str(body_1) + '_Body_' + str(body_2) + '_Angle'

            # Store information about the joint angle model_joint_angles dictionary
            model_joint_angles[label] = float((np.degrees(angle)))

            # Store information about the joint angle label in model_joint_angles_labels list
            model_joint_angles_labels.append(label)

    # Convert the dictionary to a numpy array
    model_joint_angles = pd.DataFrame.from_dict([model_joint_angles]).to_numpy()

    # Return model joint labels and angles
    return model_joint_angles_labels, model_joint_angles


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
