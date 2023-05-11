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

def assemble_gravitational_forces(dataConst, inertial_parameters):
    """

    Function assembles the vector of gravitational forces of the multibody system. 

    Parameters:
    dataConst             	:   numpy.ndarray
                                Constants matrix
    inertial_parameters     :   dictionary
                                Model segments inertial parameters

    Returns:
    gravitational_forces    :  dict
                               Dictionary containing all inertial forces for each body of multibody system 
    """

    # Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    bodies_numbers_list = [int(x[2]) for x in dataConst if x[0]==1]

    gravitational_forces = {}

    for body in bodies_numbers_list:
        gravitational_forces[body] = np.array([0, inertial_parameters[body]['Mass']*-9.81, 0, 0])

    return gravitational_forces

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
