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

import linecache
import numpy as np


def read_muscle_db(muscle_db_path, scaling_factor, rb_info, muscle_specific_tension, verbose):
    """
    
    Function reads and scales the local coordinates of the via points of each muscle.
    
    Parameters:
        muscle_db_path          :   str
                                    absolute path of the muscle database input file
        scaling_factor          :   float
                                    scaling factor to scale the local coordinates of each muscle
        rb_info                 :   dictionary

        muscle_specific_tension :   float
                                    muscle specific tension
        verbose                 :   boolean
                                    True to print the parameters of each muscle of the
                                    biomechanical model
    
    Returns:
        muscle_info             :   dictionary
                                    contains all the muscle parameters
    
    """
    file_header = linecache.getline(muscle_db_path, 1).split(',')

    # To open Workbook
    muscle_db_data = np.loadtxt(muscle_db_path, dtype='str', delimiter=',', skiprows=1)

    # Initialize dictionary
    muscle_info = {}

    muscle_idx = 0

    # Add values to the variables
    for row in muscle_db_data:
        muscle_name = row[0]
        muscle_on_off = int(float(row[1]))
        muscle_element = int(float(row[2]))
        muscle_type = row[3]
        muscle_n_via_points = int(float(row[4]))
        muscle_wrapping_body = row[5]
        muscle_wrapping_point_P = row[6]
        muscle_wrapping_point_S = row[7]
        muscle_wrapping_direction = row[8]
        muscle_PCSA = float(row[9])
        muscle_opt_length = float(row[10])
        tendon_slack_length = float(row[11])
        muscle_pennation_angle = np.radians(float(row[13]))
        muscle_origin_LocCoord_X = float(row[17])
        muscle_origin_LocCoord_Y = float(row[18])
        muscle_origin_LocCoord_Z = float(row[19])
        muscle_Origin_Nb = str(row[20])
        muscle_insertion_LocCoord_X = float(row[21])
        muscle_insertion_LocCoord_Y = float(row[22])
        muscle_insertion_LocCoord_Z = float(row[23])
        muscle_insertion_Nb = str(row[24])

        if int(muscle_on_off) == 1:
            # print(muscle_name, float(muscle_PCSA * muscle_specific_tension))
            muscle_element_info = {'muscle': muscle_name,
                                   'on_off': int(muscle_on_off),  # muscle on (active) or off (inactive)
                                   'type': muscle_type,
                                   'element': muscle_element,
                                   'origin': {'body': rb_info[muscle_Origin_Nb],
                                              # AP coordinate
                                              'coords': [float(muscle_origin_LocCoord_X) * scaling_factor,
                                                         # Long coordinate
                                                         float(muscle_origin_LocCoord_Z) * scaling_factor]},
                                   'insertion': {'body': rb_info[muscle_insertion_Nb],  # Body number
                                                 # AP coordinate
                                                 'coords': [float(muscle_insertion_LocCoord_X * scaling_factor),
                                                            # Long coordinate
                                                            float(muscle_insertion_LocCoord_Z) * scaling_factor]},
                                   # Muscle MVC force
                                   'fo': float(muscle_PCSA * muscle_specific_tension),
                                   # Muscle pennation angle
                                   'alpha': float(muscle_pennation_angle),
                                   # Muscle resting length
                                   'lm': float(muscle_opt_length),
                                   # Tendon slack length
                                   'lt': float(tendon_slack_length),
                                   # Muscle number of via points
                                   'n_via_points': muscle_n_via_points
                                   }

            if str(muscle_type).lower().strip() == 'vp':
                vp_info = {}
                for vp_number in range(0, muscle_n_via_points):
                    start_idx = file_header.index('Insertion_Segment') + vp_number * 4
                    vp_info['vp' + str(vp_number + 1)] = {'body': rb_info[row[start_idx + 4].lower()],  # Body number
                                                          # AP coordinate
                                                          'coords': [float(row[start_idx + 1]) * scaling_factor,
                                                                     # ML coordinate
                                                                     # float(row[start_idx + 2]) * scaling_factor,
                                                                     # Long coordinate
                                                                     float(row[start_idx + 3]) * scaling_factor]}
                muscle_element_info.update(vp_info)

            elif str(muscle_type).lower().strip() == 'bc':
                vp_info = {}
                for vp_number in range(0, muscle_n_via_points):
                    start_idx = file_header.index('Insertion_Segment') + vp_number * 4
                    vp_info['vp' + str(vp_number + 1)] = {'body':
                                                          # Body number
                                                          rb_info[row[start_idx + 4].lower()],
                                                          'coords':
                                                          # AP coordinate
                                                          [float(row[start_idx + 1]) * scaling_factor,
                                                           # ML coordinate
                                                           # float(row[start_idx + 2]) * scaling_factor,
                                                           # Long coordinate
                                                           float(row[start_idx + 3]) * scaling_factor]}

                muscle_element_info.update(vp_info)

                wrapping_vp_info = {'wrap_point_P': muscle_wrapping_point_P,  # Wrappping Point 0 label
                                    'wrap_point_S': muscle_wrapping_point_S,  # Wrappping Point 0 label
                                    'wrap_direction': muscle_wrapping_direction,  # Wrappping direction
                                    'wrap_obstacle_body': muscle_wrapping_body,  # Wrappping obstacle body
                                    }

                muscle_element_info.update(wrapping_vp_info)

            muscle_info[muscle_idx] = muscle_element_info

            muscle_idx += 1

    if verbose:
        for idx in range(0, len(muscle_info.keys())):
            print(muscle_info[idx]['muscle'], idx)

    return muscle_info


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
