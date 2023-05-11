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
import pandas as pd

from assemble_C_matrix import assemble_C_matrix


def compute_norm_muscle_lengths(model_q_data, muscles_info):
    """

    Function computes the normalized length of each muscle of the biomechanical model.

    Parameters
    model_q_data		:   numpy.array
                            generalized coordinates of the multibody system
    muscles_info		:   dictionary
                            muscle parameters database
    Returns
    muscles_norm_length	:   numpy.array
                            normalized length of each muscle of the biomechanical model.

    """

    muscles_norm_length = {}

    for q in model_q_data:
        for muscle in muscles_info.keys():
            muscle_label = muscles_info[muscle]['muscle']
            if muscles_info[muscle]['type'].lower() == 's':
                # Read muscle origin
                muscle_origin_nbody = int(muscles_info[muscle]['origin']['body'])
                muscle_origin_loc_coords = muscles_info[muscle]['origin']['coords']
                muscle_origin_glob_coords = assemble_C_matrix(muscle_origin_loc_coords).dot(
                    q[4 * (muscle_origin_nbody - 1): 4 * (muscle_origin_nbody - 1) + 4])

                # Read muscle insertion
                muscle_insertion_nbody = int(muscles_info[muscle]['insertion']['body'])
                muscle_insertion_loc_coords = muscles_info[muscle]['insertion']['coords']
                muscle_insertion_glob_coords = assemble_C_matrix(muscle_insertion_loc_coords).dot(
                    q[4 * (muscle_insertion_nbody - 1): 4 * (muscle_insertion_nbody - 1) + 4])

                lm_opt      = muscles_info[muscle]['lm']
                lt          = muscles_info[muscle]['lt']
                lm_total    = np.linalg.norm(muscle_origin_glob_coords - muscle_insertion_glob_coords)
                lm_norm     = (lm_total - lt)/lm_opt

                if muscle not in muscles_norm_length.keys():
                    muscles_norm_length[muscle] = {muscle_label: [lm_norm]}
                elif muscle in muscles_norm_length.keys():
                    muscles_norm_length[muscle][muscle_label] = muscles_norm_length[muscle][muscle_label] + [lm_norm]

            elif muscles_info[muscle]['type'].lower() == 'vp':
                muscle_path_coords = []

                element_n_via_points = muscles_info[muscle]['n_via_points']
                # Read muscle origin data
                muscle_origin_nbody = int(muscles_info[muscle]['origin']['body'])
                muscle_origin_loc_coords = muscles_info[muscle]['origin']['coords']
                muscle_origin_glob_coords = assemble_C_matrix(muscle_origin_loc_coords).dot(
                    q[4 * (muscle_origin_nbody - 1): 4 * (muscle_origin_nbody - 1) + 4])
                muscle_path_coords.append(muscle_origin_glob_coords)

                # Read muscle via points data
                for via_point in range(0, element_n_via_points):
                    muscle_via_point_nbody = int(muscles_info[muscle]['vp' + str(via_point + 1)]['body'])
                    muscle_via_point_loc_coords = muscles_info[muscle]['vp' + str(via_point + 1)]['coords']
                    muscle_via_point_glob_coords = assemble_C_matrix(muscle_via_point_loc_coords).dot(
                        q[4 * (muscle_via_point_nbody - 1): 4 * (muscle_via_point_nbody - 1) + 4])
                    muscle_path_coords.append(muscle_via_point_glob_coords)

                # Read muscle insertion data
                muscle_insertion_nbody = int(muscles_info[muscle]['insertion']['body'])
                muscle_insertion_loc_coords = muscles_info[muscle]['insertion']['coords']
                muscle_insertion_glob_coords = assemble_C_matrix(muscle_insertion_loc_coords).dot(
                    q[4 * (muscle_insertion_nbody - 1): 4 * (muscle_insertion_nbody - 1) + 4])
                muscle_path_coords.append(muscle_insertion_glob_coords)

                lm_opt = muscles_info[muscle]['lm']
                lt = muscles_info[muscle]['lt']
                lm_total = np.sum(np.linalg.norm(np.diff(np.array(muscle_path_coords), axis=0), axis=1))
                lm_norm = (lm_total - lt) / lm_opt

                if muscle not in muscles_norm_length.keys():
                    muscles_norm_length[muscle] = {muscle_label: [lm_norm]}
                elif muscle in muscles_norm_length.keys():
                    muscles_norm_length[muscle][muscle_label] = muscles_norm_length[muscle][muscle_label] + [lm_norm]

    muscle_norm_length_data     = np.zeros((model_q_data.shape[0], len(muscles_norm_length.keys())))
    muscle_norm_length_labels   = []

    for idx in sorted(muscles_norm_length.keys()):
        muscle_name = list(muscles_norm_length[idx].keys())[0]
        muscle_norm_length = muscles_norm_length[idx][muscle_name]
        muscle_norm_length_data[:,idx] = muscle_norm_length
        muscle_norm_length_labels.append(muscle_name)

    return muscle_norm_length_labels, muscle_norm_length_data


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
