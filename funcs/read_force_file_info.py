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


def read_force_file_info(fpath):
    """
    
    Function loads the time, force, coords, on_off and coords_type of each
    force to be applied in the multibody system during the analysis.

    Parameters:
        fpath       :   string
                        file containing the forces to be applied in the model during the analysis

    Returns:
        force_dict  :   dictionary
                        time, force, coords, on_off and coords_type of the forces to be applied
                        in the multibody system during the analysis.

    """

    force_data = np.loadtxt(fpath, dtype='float', delimiter=",", comments='#', skiprows=1)

    coordinates_type = linecache.getline(fpath, 1).split(":")

    # Iterate through driversNumberAndName and add data to dictionary
    rigid_body_number = int(force_data[0, 6])

    # Empty dictionary to store raw data and spline and derivatives parameters (knots,
    # coefficients and spline order )
    force_dict = {rigid_body_number: {'force': [],
                                      'coords_type': '',
                                      'time': [],
                                      'coords': [],
                                      'on_off': []}}

    force_dict[rigid_body_number]['time'] = force_data[:, 0]
    force_dict[rigid_body_number]['force'] = force_data[:, [1, 2]]
    force_dict[rigid_body_number]['coords'] = force_data[:, [3, 4]]
    force_dict[rigid_body_number]['on_off'] = force_data[:, 5]
    force_dict[rigid_body_number]['coords_type'] = coordinates_type[1].replace('\n', '').lower().strip()

    return force_dict


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
