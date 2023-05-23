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


def compute_fmP(muscle_info, force):
    """

    Function computes the muscle force components (CE or PE) for all the
    force application points of the muscles


    Parameters:
        muscle_info        : dictionary
                             information about every muscle of the model
        force              : list
                             contractile (CE) or passive (PE) force values for all
                             the muscles

    Returns:
        fmP                : dictionary
                             Vectorial (CE or PE) muscle force component for all the
                             force application points of the muscles

    """
    
    # Initialize fmP vectorial (passive or contractile elements)
    fmP = {}

    # Go through every muscle
    for muscle_idx in range(0, len(muscle_info.keys())):
        muscle_n_points = muscle_info[muscle_idx]['n_via_points'] + 2

        nb_vectors = muscle_n_points - 1

        # Get the passive or contractile forces for this muscle
        fm = force[muscle_idx]
        
        # Initialize 
        fmP_inner_dic = {}

        for i in range(0, nb_vectors):
            if nb_vectors == 1:
                # Get the coordinates of the points
                [x1, y1] = muscle_info[muscle_idx]['origin']['coords']
                [x2, y2] = muscle_info[muscle_idx]['insertion']['coords']
            elif nb_vectors == 2:
                if int(i) == 0:
                    # Get the coordinates of the points
                    [x1, y1] = muscle_info[muscle_idx]['origin']['coords']
                    [x2, y2] = muscle_info[muscle_idx]['vp' + str(i + 1)]['coords']
                elif int(i) == muscle_n_points - 1:
                    # Get the coordinates of the points
                    [x1, y1] = muscle_info[muscle_idx]['vp' + str(i)]['coords']
                    [x2, y2] = muscle_info[muscle_idx]['insertion']['coords']
            elif nb_vectors > 2:
                if int(i) == 0:
                    # Get the coordinates of the points
                    [x1, y1] = muscle_info[muscle_idx]['origin']['coords']
                    [x2, y2] = muscle_info[muscle_idx]['vp' + str(i + 1)]['coords']
                elif int(i) == muscle_n_points - 2:
                    # Get the coordinates of the points
                    [x1, y1] = muscle_info[muscle_idx]['vp' + str(i)]['coords']
                    [x2, y2] = muscle_info[muscle_idx]['insertion']['coords']
                else:
                    # Get the coordinates of the points
                    [x1, y1] = muscle_info[muscle_idx]['vp' + str(i)]['coords']
                    [x2, y2] = muscle_info[muscle_idx]['vp' + str(i + 1)]['coords']

            # Compute the direction vector
            vector = [x2 - x1, y2 - y1]
            vector_norm = (vector[0]**2 + vector[1]**2)**(1/2)
            direction_vector = [a/vector_norm for a in vector]

            # Compute the force vector
            fmP_aux = [direction * fm for direction in direction_vector]

            # Update inner dictionary
            fmP_inner_dic[i] = [fmP_aux, list(-np.array(fmP_aux))]

        # Update dictionary
        fmP[muscle_idx] = fmP_inner_dic

    return fmP


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
