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

def read_angular_driver_info(row, idx, ang_drivers_info):
    """

    Function compiles the information about the angular driving constraint equations of
    the multibody system.


    Parameters:
    row                 :   numpy.array
                            info about each angular driving constraint equation of the multibody system.
    idx                 :   int
                            type of each angular driving constraint equation of the multibody system
    ang_drivers_info    :   dictionary
                            empty dictionary .

    Returns:
    ang_drivers_info    :   dictionary
                            info (n_bodies, bodies and type of constraint) of each
                            driver of the multibody system.
    """

    if idx in [2,4, 13, 15]:
        n_bodies = 2
    elif idx in [3, 5, 12, 14]:
        n_bodies = 1

    if idx in [2, 3, 12, 13]:
        product_type = 'dot_idx'
    elif idx in [4, 5, 14, 15]:
        product_type = 'cross_idx'

    if idx in [2, 4, 13, 15]:
        body_1_label = 'body_1'
        body_2_label = 'body_2'
    elif idx in [3, 5, 12, 14]:
        body_1_label = 'body_1'
        body_2_label = 'unit_vec_dir'

    if row[0] == idx:
        n_angular_driver = int(row[13])
        n_body_1 = row[2]
        n_body_2 = row[3]
        if body_2_label == 'body_2':
            body_1_value = int(n_body_1)
            body_2_value = int(n_body_2)
        elif body_2_label == 'unit_vec_dir':
            body_1_value = int(n_body_1)
            body_2_value = np.array([row[8],row[9]])
        if n_angular_driver not in ang_drivers_info.keys():
            ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                  body_1_label: body_1_value,
                                                  body_2_label: body_2_value,
                                                  product_type: int(row[1])
                                                  }
        elif n_angular_driver in ang_drivers_info.keys():
            ang_drivers_info[n_angular_driver].update({product_type: int(row[1])
                                                       })

    return ang_drivers_info

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)