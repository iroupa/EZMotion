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

def compute_joints_angles_fd(dataConst, q_vector):

    model_joint_angles = {}
    model_joint_angles_labels = []
    joints_info = {}
    joint_counter = 0

    for row in range(0, dataConst.shape[0]):
        # Check for revolute joints constraint (idx == 9)
        if int(dataConst[row, 0]) == 9:
            joints_info[joint_counter] = {'body_1': int(dataConst[row, 2]), 'body_2': int(dataConst[row, 3])}
            joint_counter += 1
        # Check for ground joint constraint (idx = 8)
        if int(dataConst[row, 0]) == 8:
            joints_info[joint_counter] = {'body_1':int(dataConst[row,2]),'body_2':'ground'}
            joint_counter += 1

    for _ in range(0, len(joints_info.keys())):
        body_1 = joints_info[_]['body_1']
        body_2 = joints_info[_]['body_2']

        if body_2 == 'ground':
            body_1_q = q_vector[(int(body_1)-1) * 4: (int(body_1)-1) * 4 + 4]
            angle = np.arctan2(body_1_q[3], body_1_q[2])
            label = 'Body_' + str(body_1) + '_Abs_Angle'
            model_joint_angles[label] = float((np.degrees(angle)))
            model_joint_angles_labels.append(label)
        else:
            body_1_q = q_vector[(int(body_1)-1) * 4: (int(body_1)-1) * 4 + 4]
            body_2_q = q_vector[(int(body_2)-1) * 4: (int(body_2)-1) * 4 + 4]
            angle = np.arctan2(body_1_q[3], body_1_q[2]) - np.arctan2(body_2_q[3], body_2_q[2]);
            label = 'Body_' + str(body_1) + '_Body_' + str(body_2) + '_Angle'
            model_joint_angles[label] = float((np.degrees(angle)))
            model_joint_angles_labels.append(label)

    model_joint_angles = pd.DataFrame.from_dict([model_joint_angles]).to_numpy()

    return model_joint_angles_labels, model_joint_angles

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

