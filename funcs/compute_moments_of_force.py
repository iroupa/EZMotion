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
__copyright__ = 'Copyright (C) 2023 Ivo Roupa'
__email__ = 'iroupa@gmail.com'
__license__ = 'Apache 2.0'

import numpy as np
import pandas as pd
from read_angular_driver_info import read_angular_driver_info


def compute_moments_of_force(dataConst, q, lmm, weight):
    """
    
    Function computes the net moment of force for each revolute joint of the model.

    Parameters:
        dataConst				:   numpy.array
                                    multidimensional numpy array containing the information regarding the modeling
                                    of the multibody system
        q						:   numpy.array
                                    vector of generalized coordinates of the multibody system
        lmm						:   numpy.array
                                    vector of lagrange multipliers of the multibody system
        weight					:   float
                                    subject weight

    Returns:
        net_moments_of_force	:   numpy.array
                                    vector of normalized net moments of force for each revolute joint of the model.
    
    """

    ang_drivers_info = {}

    constraints_type_idx = [2, 3, 4, 5, 12, 13, 14, 15]
    for row in dataConst:
        for constraint_type in constraints_type_idx:
            read_angular_driver_info(row, constraint_type, ang_drivers_info)

    net_moments_of_force = {}
    joint_angles = {}

    for ang_driver in sorted(ang_drivers_info.keys()):
        # for frame in range(0, q.shape[0]):
        n_body_1 = ang_drivers_info[ang_driver]['body_1']
        body_1_direction_unit_vector = q[4 * (n_body_1 - 1) + 2:4 * (n_body_1 - 1) + 4]

        if ang_drivers_info[ang_driver]['n_bodies'] == 1:
            body_2_direction_unit_vector = ang_drivers_info[ang_driver]['unit_vec_dir']
        elif ang_drivers_info[ang_driver]['n_bodies'] == 2:
            n_body_2 = ang_drivers_info[ang_driver]['body_2']
            body_2_direction_unit_vector = q[4 * (n_body_2 - 1) + 2:4 * (n_body_2 - 1) + 4]

        # Compute joint angle between two model bodies
        body_1_abs_angle = np.arctan2(body_1_direction_unit_vector[1], body_1_direction_unit_vector[0])
        body_2_abs_angle = np.arctan2(body_2_direction_unit_vector[1], body_2_direction_unit_vector[0])
        joint_angle = body_1_abs_angle - body_2_abs_angle

        # Assign net moment of force to angular driver dictionary
        if ang_driver not in net_moments_of_force.keys():
            joint_angles[ang_driver] = [joint_angle]
        elif ang_driver in net_moments_of_force.keys():
            joint_angles[ang_driver].append(joint_angle)

        # Compute joint lmm for 'dot' and cross' product angular driver constraints
        joint_lmm_dot_product_index = ang_drivers_info[ang_driver]['dot_idx']
        joint_lmm_cross_product_index = ang_drivers_info[ang_driver]['cross_idx']

        # Compute moment of force for 'dot' and cross' product angular driver constraint
        joint_dot_product_moment = lmm[joint_lmm_dot_product_index] * np.sin(joint_angle)
        joint_cross_product_moment = lmm[joint_lmm_cross_product_index]*np.cos(joint_angle)

        # Compute net moment of force for product angular driver constraint
        joint_net_moment_of_force = joint_dot_product_moment + joint_cross_product_moment

        # Assign net moment of force to angular driver dictionary
        if ang_driver not in net_moments_of_force.keys():
            net_moments_of_force[ang_driver] = [joint_net_moment_of_force/weight]
        elif ang_driver in net_moments_of_force.keys():
            net_moments_of_force[ang_driver].append(joint_net_moment_of_force/weight)

    net_moments_of_force = pd.DataFrame.from_dict(net_moments_of_force).to_numpy()

    return net_moments_of_force


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
