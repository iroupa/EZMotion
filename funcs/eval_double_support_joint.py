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
from assemble_C_matrix import assemble_C_matrix


def evaluate_double_support_joint(nCoordinates,  constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """

    Function computes and assigns the contributions of the double support joint constraint equations to phi vector,
    dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic and dynamic analysis.

    Parameters:
        nCoordinates        :   int
                                total number of generalized coordinates of the multibody system
        constraintByType    :   int
                                Number of kinematic constraints of the multibody system
        dataConst           :   numpy.ndarray
                                information describing the topology of the multibody system
        q                   :   numpy.ndarray
                                vector of generalized coordinates of the multibody system
        qpto                :   numpy.ndarray
                                vector of generalized velocities of the multibody system
        phi                 :   numpy.ndarray
                                vector of kinematic constraints of the multibody system
        dPhidq              :   numpy.ndarray
                                jacobian matrix of the multibody system
        niu                 :   numpy.ndarray
                                right hand side of the velocity vector of kinematic constraint equations
        gamma               :   numpy.ndarray
                                right hand side of the acceleration vector of kinematic constraint equations
        rowIn               :   int
                                number of line to insert kinematic constraint equation contribution in phi,
                                dPhidq, niu and gamma
    
    Returns:
            {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}:  dictionary
                                                                                            Contributions of Double
                                                                                            Support Constraint to phi,
                                                                                            dPhidq, niu and gamma
                                                                                            vectors and the ending index
                                                                                            of such contributions
    
    """

    # Get Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    constraintRowIdxs = [rowIn, rowIn + 1]

    # Get moving body number
    movingBodyNumber = int(dataConst[constraintByType, 2])

    # Assign moving and support bodies local coordinates
    movingLocCoords = dataConst[constraintByType, 6:8]
    supportCoords = dataConst[constraintByType, 8:10]
    supportVels = dataConst[constraintByType, 10:12]
    supportAcc = dataConst[constraintByType, 12:14]

    # Create moving body 'C' Matrix
    movingCMatrix = assemble_C_matrix(movingLocCoords)

    # Create moving rigid body 'q' coordinates
    movingQVec = q[4 * (movingBodyNumber - 1): 4 * (movingBodyNumber - 1) + 4]

    # Double support constraint contribution to 'phi' vector
    phi[constraintRowIdxs] = np.dot(movingCMatrix, movingQVec) - supportCoords

    # Double support constraint contribution to jacobian matrix
    # Define moving Rigid Body Columns in jacobian matrix
    movingColsIdxs = [4 * (movingBodyNumber - 1), 4 * (movingBodyNumber - 1) + 4]

    dPhidq[constraintRowIdxs, movingColsIdxs[0]:movingColsIdxs[1]] = movingCMatrix

    # Double support constraint contribution to 'niu' vector
    niu[constraintRowIdxs] = supportVels

    # Double support  constraint contribution to 'gamma' vector
    gamma[constraintRowIdxs] = supportAcc

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 2}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
