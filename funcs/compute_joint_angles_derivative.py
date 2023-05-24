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
from scipy.interpolate import CubicSpline


def compute_joint_angles_derivative(joint_angles, der):
    """

    Function computes the 'n' derivative of each angle of each revolute
    joint of the multibody system.

    Parameters:
        joint_angles			:   numpy array
                                    angle of each revolute joint of the multibody system
        der						:   int
                                    degree of the derivative

    Returns:
        joint_angles_der_rep	:   numpy array
                                    'n' derivative of each angle of each revolute joint of the multibody system

    """

    # Initialize the joint_angles_der_rep array with zeros
    joint_angles_der_rep = np.zeros((joint_angles.shape[0], joint_angles.shape[1]))

    # Get the number of data points (samples)
    ys = joint_angles.shape[0]

    # Generate the corresponding x values using numpy arange
    xs = np.arange(0, ys, 1)

    # Iterate over each joint angle column
    for _ in range(0, joint_angles.shape[1]):
        # Get the y values for the current joint angle column
        y = joint_angles[:, _]

        # Create a cubic spline interpolation function for the current joint angle column
        angle_spline_func = CubicSpline(xs, y)

        # Compute the derivative (angular velocity) using the spline function
        angular_velocity = angle_spline_func(xs, der)

        # Assign the computed angular velocity to the corresponding column in joint_angles_der_rep
        joint_angles_der_rep[:, _] = angular_velocity

    return joint_angles_der_rep


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
