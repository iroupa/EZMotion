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

import math

import numpy as np


def compute_wrapping_points(Q_angle, T_angle, wrapping_direction, nPoints, radius):
    """
	Function computes the local coordinates of point 'Q' and 'T' 
	
    Parameters:
	Q_angle				: float
						angle between point 'Q' and global reference frame
	T_angle				: float
						angle between point 'T' and global reference frame
	wrapping_direction	: str 
						wrapping direction (cw - anterior / ccw - posterior)	
	nPoints				: int
						number of points used to discretize the wrapping muscle path between point 'Q' and point 'T' 	
	radius				: float
						radius of the obstacle
	Returns
						:list of lists	
						local coordinates of the wrapping points between point 'Q' and point 'T'
    """
    if wrapping_direction == 'cw':
        if (T_angle > Q_angle):
            T_angle = T_angle - 2 * math.pi
        step = (T_angle - Q_angle) / (nPoints)
        # Angles of the points in between
        wrapping_range = np.arange(Q_angle, T_angle, step)
    elif wrapping_direction == 'ccw':
        if (T_angle < Q_angle):
            T_angle = T_angle + 2 * math.pi
        step = (T_angle - Q_angle) / (nPoints)
        # Angles of the points in between
        wrapping_range = np.arange(Q_angle, T_angle, step)

    return [[np.cos(x)*radius, np.sin(x)*radius] for x in wrapping_range]

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)