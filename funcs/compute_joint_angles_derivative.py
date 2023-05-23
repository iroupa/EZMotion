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


def compute_joint_angles_derivative(joint_angles, t0, tf, dt, der):
    """

    Function computes the 'n' derivative of each angle of each revolute
    joint of the multibody system.

    Parameters:
        joint_angles			:   numpy array
                                    angle of each revolute joint of the multibody system
        t0						:   float
                                    initial time of the analysis
        tf						:   float
                                    final time of the analysis
        dt						:   float
                                    time step of the analysis
        der						:   int
                                    degree of the derivative

    Returns:
        joint_angles_der_rep	:   numpy array
                                    'n' derivative of each angle of each revolute joint of the multibody system

    """

    joint_angles_der_rep = np.zeros((joint_angles.shape[0], joint_angles.shape[1]))

    ys = joint_angles.shape[0]
    xs = np.arange(t0, tf, dt)

    if ys != int(xs.shape[0]):
        xs = np.arange(t0, tf + dt, dt)

    for _ in range(0, joint_angles.shape[1]):
        y = joint_angles[:, _]
        angle_spline_func = CubicSpline(xs, y)
        angular_velocity = angle_spline_func(xs, der)
        joint_angles_der_rep[:, _] = angular_velocity

    return joint_angles_der_rep


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
