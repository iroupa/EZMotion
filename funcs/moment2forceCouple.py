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
from assemble_C_matrix import assemble_C_matrix


def moment2forceCouple(q, bodyNumber, moment_of_force):
    """
    
    Function converts a moment of force to a couple of forces.

    Parameters:
        q				    :   np.array()
                                vector of body 'i' generalized coordinates
        bodyNumber		    :   int
                                body number
        moment_of_force     :   float
                                Moment magnitude

    Returns:
        bodyforce           :   numpy.array
                                spring force applied to body 'i' centre of mass coordinate
    """

    # Force 1 local coordinates
    f1_locCoords = np.array([0, 0])

    # Force 2 local coordinates
    f2_locCoords = np.array([1, 0])

    f1_cMatrix = assemble_C_matrix(f1_locCoords)
    f2_cMatrix = assemble_C_matrix(f2_locCoords)

    R90 = np.array([[0, -1],
                    [1, 0]])

    body_orientation = q[4 * (bodyNumber - 1) + 2: bodyNumber + 4]

    f1_orientation = np.dot(R90, body_orientation)
    f2_orientation = np.dot(-R90, body_orientation)

    force_magnitude = moment_of_force / 2.0

    f1_vector = np.dot(force_magnitude, f1_orientation)
    f2_vector = np.dot(-force_magnitude, f2_orientation)

    force = np.dot(f1_cMatrix.T, f1_vector) + np.dot(f2_cMatrix.T, f2_vector)

    return {bodyNumber: force.reshape(4,)}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
