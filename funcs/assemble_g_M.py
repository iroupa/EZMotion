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


def assemble_g_M(nCoordinates, ge_bodies):
    """

    Function assembles the vector of generalized coordinates of the whole system for every muscle

    Parameters:
        nCoordinates    :   int
                            number of coordinates of the system
        ge_bodies       :   dictionary
                            ge_fm force vector for every body of every muscle muscle

    Returns:
        g_M             :   np.array
                            vector of the generalised coordinates of the whole
                            system for every muscle (each line is a different muscle)

    """
    
    # number of muscles
    n_muscles = len(ge_bodies.keys())
    
    # Initialize g_M
    g_M = np.zeros((n_muscles, nCoordinates)) 
    
    # Iterate over every muscle
    for muscle_idx in range(0, len(ge_bodies.keys())):
        # Muscle name 
        muscle_name = muscle_idx

        # Segments cossed by the muscle
        muscle = ge_bodies[muscle_name]
        
        # Initialize the vector of generalised coordinates of each muscle of the multibody system
        g_M_mn = np.zeros(nCoordinates)

        # Iterate over every body crossed by each muscle
        for body in muscle.keys():
            # Get the generalised coordinates of the muscle with respect to each body to which the muscle is attached
            g_body_mtx = muscle[body].tolist()

            # Initialize the vector of generalised coordinates of the muscle with respect to each body to which
            # the muscle is attached
            g_body = [g_body_mtx[0][0], g_body_mtx[1][0], g_body_mtx[2][0], g_body_mtx[3][0]]

            # Assign the generalised coordinates of each segment to which the muscle is attached to the vector
            # of generalised coordinates of the muscle
            g_M_mn[4 * (int(body) - 1): 4 * (int(body) - 1) + 4] = g_body

        # Assign generalised coordinates of each muscle to vector of generalised coordinates of the multibody system
        g_M[muscle_idx] = g_M_mn

    return g_M


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
