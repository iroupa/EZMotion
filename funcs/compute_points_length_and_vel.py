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


def compute_points_length_and_velocity(point_m_coords, point_m_body, point_n_coords, point_n_body, q, qp):
    """

    Function computes the length and velocity of each segment of each muscle of the biomechanical model.

    Parameters:
        point_m_coords	:   list
                            local coordinates of point 'm' with respect to body 'm'
        point_m_body	:   int
                            number of body 'm'
        point_n_coords	:   list
                            local coordinates of point 'n' with respect to body 'm'
        point_n_body	:   int
                            number of body 'n'
        q				:   numpy.array
                            vector of generalized coordinates of the multibody system
        qp				:   numpy.array
                            vector of generalized velocities of the multibody system


    Returns:
        r_mn			: float
                        length of each segment of each muscle of the biomechanical model.
        rp_mn			: float
                        contraction velocity of each segment of each muscle of the biomechanical model.

    """

    # Compute matrix C of points 'm' and 'n'
    Cmatrix_m = assemble_C_matrix(point_m_coords)
    Cmatrix_n = assemble_C_matrix(point_n_coords)

    # Obtain generalized coordinates of bodies 'm' and point 'n'
    qvector_m = q[4 * (int(point_m_body) - 1): 4 * (int(point_m_body) - 1) + 4]
    qvector_n = q[4 * (int(point_n_body) - 1): 4 * (int(point_n_body) - 1) + 4]

    # Obtain generalized velocities of bodies 'm' and 'n'
    qpvector_m = qp[4 * (int(point_m_body) - 1): 4 * (int(point_m_body) - 1) + 4]
    qpvector_n = qp[4 * (int(point_n_body) - 1): 4 * (int(point_n_body) - 1) + 4]

    # Compute global coords of points 'm' and 'n'
    r_m = Cmatrix_m.dot(qvector_m)
    r_n = Cmatrix_n.dot(qvector_n)

    # Compute velocities of points 'm' and 'n'
    rp_m = Cmatrix_m.dot(qpvector_m)
    rp_n = Cmatrix_m.dot(qpvector_n)

    # Compute element length and append it to segment length and velocity
    r_mn = np.linalg.norm(r_m - r_n)

    # Compute element velocity and append it to segment length and velocity
    rp_mn = ((r_m - r_n).dot(rp_m - rp_n)) / np.linalg.norm(r_m - r_n)

    return r_mn, rp_mn


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
