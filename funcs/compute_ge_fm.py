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

import numpy as np

from assemble_C_matrix import assemble_C_matrix


def compute_ge_fm(muscle_info, fmP):
    
    """
	
	Function computes the vector of forces for every force applied in 
	every point of every muscle 
	
	
    Parameters:
    muscle_info        : dictionary
                         information about every muscle of the model 
    fmP                : dictionary
                         Vectorial passive muscle force component for all the 
                         application points of the muscles
        
    Returns:
    ge_fm              : dictionary 
                         ge_fm force vector for every force applied in every point
                         of every muscle 
               
    """
    # Initialize ge_fm 
    ge_fm = {}
    
    # Initialize c_matrix dictionary
    c_matrix = {}
    
    # Complete c_matrix dictionary with the CMp values for every point in every muscle
    # Go through every muscle 
    for muscle_idx in range(0,len(muscle_info.keys())):
        # muscle name
        muscle_name = muscle_idx

        # Get list of muscle via points
        muscle_via_points_labels = [x for x in muscle_info[muscle_idx].keys() if x.startswith('vp')]

        # muscle points
        muscle_points = ['origin'] + muscle_via_points_labels + ['insertion']
        
        # Initialize ge_fm 
        ge_fm[muscle_idx] = {}
        
        # Initialize c_matrix_p dictionary
        c_matrix_p = {}

        p_idx = 0
        # Go through every point

        for p in muscle_points:#.keys():
            body = muscle_info[muscle_idx][str(p)]['body']
            pointP = muscle_info[muscle_idx][str(p)]['coords']
            Cmatrix = assemble_C_matrix(pointP)

            c_matrix_p[p_idx] = [body, Cmatrix]
            p_idx += 1

        c_matrix[muscle_name] = c_matrix_p
       
    # Go through every muscle to 
    for m in range(0, len(fmP.keys())):
        muscle_name = m

        for i in range(0, len(fmP[muscle_name].keys())):
            body1 = c_matrix[muscle_name][i][0]
            body2 = c_matrix[muscle_name][i+1][0]

            c_matrix1 = c_matrix[muscle_name][i][1]
            c_matrix2 = c_matrix[muscle_name][i+1][1]

            fmP_column1 =[[fmP[muscle_name][i][0][0]],[fmP[muscle_name][i][0][1]]]
            fmP_column2 =[[fmP[muscle_name][i][1][0]],[fmP[muscle_name][i][1][1]]]

            ge_value1 = c_matrix1.T * np.matrix(fmP_column1)
            ge_value2 = c_matrix2.T * np.matrix(fmP_column2)

            if body1 in ge_fm[muscle_name]:
                ge_fm[muscle_name][body1].append(ge_value1)
            else:
                ge_fm[muscle_name][body1] = [ge_value1]

            if body2 in ge_fm[muscle_name]:
                ge_fm[muscle_name][body2].append(ge_value2)
            else:
                ge_fm[muscle_name][body2] = [ge_value2]

    return ge_fm
	
	
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)