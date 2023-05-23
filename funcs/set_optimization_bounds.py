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

from math import inf
import numpy as np
from det_crossed_joints import det_crossed_joints


def set_optimization_bounds(nh, nm, muscle_info, dataConst):
    """

    Function sets the bounds for the static optimization problem used to solve the redundancy muscle problem.
    
    Parameters:
        nh                  :   float
                                number of kinematic constraint equations of the biomechanical system
        nm                  :   float
                                number of muscles of the biomechanical system
        muscle_info         :   dictionary
                                muscle parameters database (fo, alfa, lo, lt, points) of the biomechanical model
        dataConst           :   numpy.ndarray
                                info regarding the modeling of each component of the multibody system

    Returns:
        bnds                : tuple
                              bounds for every variable

    """
    
    # Bounds for each variable
    b_lagrange_rem = [-inf, +inf]

    # Bounds for joins crossed by muscles
    # b_lagrange_joint = [-10.0**(-3), +10.0**(-3)]
    b_lagrange_joint = [-10.0, +10.0]

    # Bounds for muscle activation
    b_a = [0.0, 1.0]
    
    # Size of x (lambda and a)
    size_x = nh + nm
    
    # Initialize bounds list
    bnds = list(np.zeros(size_x))

    # Define bounds for the lagrange multipliers
    for i in range(0, nh):
        bnds[i] = b_lagrange_rem

    for i in range(nh, size_x):
        bnds[i] = b_a

    # Determine the joints crossed by muscles
    crossed_joints_list = det_crossed_joints(muscle_info)

    # Define bounds for the joints crossed by muscles
    for joint in crossed_joints_list:
        a = joint
        # Iterate through all lines of Jacobian matrix
        for row in range(len(dataConst[:, 1])):
            constraint_type = dataConst[row, 0]
            if constraint_type == 2 or constraint_type == 4:
                if sorted(joint) == sorted([dataConst[row, 2], dataConst[row, 3]]):
                    lagrange_line = dataConst[row, 1]
                    bnds[int(lagrange_line)] = b_lagrange_joint

    # Transform bound list into tuple
    for b in range(0, len(bnds)):
        bnds[b] = tuple(bnds[b])
    
    bnds = tuple(bnds)
    
    return bnds


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
