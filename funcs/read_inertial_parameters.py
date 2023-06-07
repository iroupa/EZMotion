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


def read_inertial_parameters(fpath):
    """
    
    Function reads the inertial parameters of each segment of the model from the input file.

    Parameters:
        fpath				: 	str
                                absolute path to inertial parameters file

    Returns:
        inertial_parameters :   dict
                                inertial parameters (mass, moment of inertia, and local coordinates of
                                the origin of the local reference frame) of each segment of the multibody system.
    
    """

    model_inertial_parameters_info = {}

    modeling_file_data = np.loadtxt(fpath,
                                    dtype='float',
                                    delimiter=',')

    for row in modeling_file_data:
        if int(row[0]) == 1:
            model_inertial_parameters_info[int(row[1])] = {'Mass': float(row[2]),
                                                           'Moment_Inertia': float(row[3]),
                                                           'CoM_LocCoordX': float(row[4]),
                                                           'CoM_LocCoordY': float(row[5])}

    return model_inertial_parameters_info


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
