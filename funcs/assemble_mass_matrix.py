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

def assemble_mass_matrix(nBodies, dataConst, inertial_parameters):
    """
    Create mass matrix for multibody system.

    Parameters:
    nBodies					: 	int
                                multibody system total number of bodies
    dataConst               :   numpy.ndarray
                                Constants matrix
    inertial_parameters     :   dictionary
                                inertial parameters of each segment of the multibody model

    Returns:
    mass_matrix :  numpy.ndarray
                   Multibody system mass matrix
    """

    # Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    model_bodies_numbers = [int(x[2]) for x in dataConst if x[0]==1]

    n_mixed_angular_drivers = []

    for _ in dataConst:
        if _[0] == 12 or _[0] == 13 or _[0] == 14 or _[0] == 15:
            n_mixed_angular_drivers.append(_[13])

    if len(n_mixed_angular_drivers) > 0:
        n_angular_drivers = int(max(n_mixed_angular_drivers))
    else:
        n_angular_drivers = 0

    # Create empty mass matrix with correct dimension
    massMatrix = np.zeros((nBodies * 4 + n_angular_drivers, nBodies * 4 + n_angular_drivers))
		
    # Assign body mass to mass matrix
    for body in range(1, nBodies+1):
        mass_idxs     = [4 * (body - 1)    , 4 * (body - 1) + 1]
        for idx in mass_idxs:
            massMatrix[idx,idx] = inertial_parameters[body]['Mass']

    # Assign body inertia to mass matrix
        inertia_idxs  = [4 * (body - 1) + 2, 4 * (body - 1) + 3]
        for idx in inertia_idxs:
            massMatrix[idx,idx] = inertial_parameters[body]['Moment_Inertia']

    # Assign body products of inertia to mass matrix (upper right)
        rows = [4 * (body - 1)    , 4 * (body - 1) + 1]
        cols = [4 * (body - 1) + 2, 4 * (body - 1) + 3]
        massMatrix[rows[0], cols[0]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordX']
        massMatrix[rows[0], cols[1]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordY']
        massMatrix[rows[1], cols[0]] = inertial_parameters[body]['Mass'] * -inertial_parameters[body]['CoM_LocCoordY']
        massMatrix[rows[1], cols[1]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordX']

    # Assign body products of inertia to mass matrix (lower left)
        rows = [4 * (body - 1) + 2, 4 * (body - 1) + 3]
        cols = [4 * (body - 1)    , 4 * (body - 1) + 1]
        massMatrix[rows[0], cols[0]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordX']
        massMatrix[rows[0], cols[1]] = inertial_parameters[body]['Mass'] * - inertial_parameters[body]['CoM_LocCoordY']
        massMatrix[rows[1], cols[0]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordY']
        massMatrix[rows[1], cols[1]] = inertial_parameters[body]['Mass'] * inertial_parameters[body]['CoM_LocCoordX']

    return massMatrix

if __name__ == "__main__":
    import doctest
	
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

    from file2dataConst import file2dataConst
    from read_inertial_parameters import read_inertial_parameters
    import os

    MC_modeling_file_fpath = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\test_data_files\trial_0003_1passagem_MC\Modeling_File.mod'
    FCC_modeling_file_fpath = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\test_data_files\trial_0003_1passagem_FCC\Modeling_File.mod'
    inertial_parameters_fpath = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\test_data_files\trial_0003_1passagem_FCC\inertial_parameters.mp'

    MC_modeling_file_data = file2dataConst(MC_modeling_file_fpath)
    FCC_modeling_file_data = file2dataConst(FCC_modeling_file_fpath)

    inertial_parameters = read_inertial_parameters(inertial_parameters_fpath)

    mass_matrix_FCC = assemble_mass_matrix(12, FCC_modeling_file_data, inertial_parameters)
    mass_matrix_MC = assemble_mass_matrix(12, MC_modeling_file_data, inertial_parameters)

    print('mass_matrix_FCC', mass_matrix_FCC.shape)
    print('mass_matrix_MC', mass_matrix_MC.shape)