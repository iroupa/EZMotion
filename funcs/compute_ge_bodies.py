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


def compute_ge_bodies(ge_fm):
    """
    Function computes the vector of forces for every body of every muscle

    Parameters:
        ge_fm           : dictionary
                          ge_fm force vector for every force applied in every point
                          of every muscle
                     
    Returns:
        ge_bodies          : dictionary
                             ge_fm force vector for every body of every muscle

    """
    
    # Initialize g_bodies
    ge_bodies = {}
 
    # Go through every muscle 
    for m in range(0, len(ge_fm.keys())):
        # muscle name
        muscle_name = list(ge_fm.keys())[m]
        muscle = ge_fm[muscle_name]
        
        # Initialize g_muscle
        g_muscle = {}
        
        # Iterate through all bodies
        for body in muscle.keys():
            g_vectors = muscle[body]
            
            # # Initialize g_body as a numpy array of zeros with shape (4, 1)
            g_body = np.zeros((4, 1))

            # Compute the sum of all g_vectors for the current body
            for i in range(0, len(g_vectors)):
                g_aux = g_body + g_vectors[i]
                g_body = g_aux

            # Assign the computed g_body to the current body in g_muscle dictionary
            g_muscle[body] = g_body

        # Assign the g_muscle dictionary to the current muscle in ge_bodies dictionar
        ge_bodies[muscle_name] = g_muscle
        
    # Return the ge_bodies dictionary
    return ge_bodies


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
