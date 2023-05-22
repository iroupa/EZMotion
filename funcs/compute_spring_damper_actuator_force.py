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
from apply_force import apply_force
from assemble_C_matrix import assemble_C_matrix


def compute_spring_damper_actuator_force(q, qp, sda_parameters):
    """

    Function computes the spring damper actuator (SDA) forces associated with
    the segments of the multibody system to which the sda actuator is connected.

    Parameters:
        q                   :   numpy.array
                                generalized coordinates vector
        qp		            : 	numpy.array
                                generalized velocity coordinates vector
        sda_parameters      :   dictionary
                                spring, damper and actuator parameters

    Returns:
        springDamperforce   :   dictionary
                                body number and respective generalized SDA forces
    """

    # Assign spring damper and actuator parameters to variables
    body1Number = sda_parameters['body1']
    body2Number = sda_parameters['body2']
    locCoords1 = sda_parameters['locCoords1']
    locCoords2 = sda_parameters['locCoords2']
    spring_k = sda_parameters['k']
    spring_lo = sda_parameters['spring_lo']
    damper_coeff = sda_parameters['damper_coeff']

    # Calculate spring length and orientation vector
    spring_origin = np.dot(assemble_C_matrix(locCoords1), q[4*(body1Number-1):4*(body1Number-1)+4])
    spring_insertion = np.dot(assemble_C_matrix(locCoords2), q[4*(body2Number-1):4*(body2Number-1)+4])
    spring_length = np.linalg.norm(spring_origin - spring_insertion)
    spring_vector = spring_insertion - spring_origin

    # Calculate spring damper actuator orientation unitary vector
    sda_unit_vector = spring_vector / np.linalg.norm(spring_vector)

    # Calculate damper velocity vector
    damper_origin = np.dot(assemble_C_matrix(locCoords1), qp[4*(body1Number-1):4*(body1Number-1)+4])
    damper_insertion = np.dot(assemble_C_matrix(locCoords2), qp[4*(body2Number-1):4*(body2Number-1)+4])
    damper_vel = damper_origin - damper_insertion

    # Calculate spring force
    springForce = spring_k * (spring_length - spring_lo)

    # Calculate damper force
    damperForce = damper_coeff*damper_vel

    # Calculate spring damper actuator force
    sdaForce = (springForce + damperForce)*sda_unit_vector

    # Apply SDA force to each body generalized coordinates
    if spring_length < spring_lo:
        force1 = apply_force(sdaForce, locCoords1)
        force2 = -apply_force(sdaForce, locCoords2)
    else:
        force1 = -apply_force(sdaForce, locCoords1)
        force2 = apply_force(sdaForce, locCoords2)

    return {int(body1Number): force1,
            int(body2Number): force2}


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
