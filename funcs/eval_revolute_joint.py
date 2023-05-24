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


def evaluate_revolute_joint(nCoordinates, constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assigns the contributions of the revolute joint constraint equations to phi vector,
    dphidq (Jacobian matrix), niu vector and gamma vector for kinematic and dynamic analysis.

    Parameters
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

    Return
            {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}:  dictionary
                                                                                            Contributions of Revolute
                                                                                            Joint Constraint to phi,
                                                                                            dPhidq, niu and gamma
                                                                                            vectors and the ending index
                                                                                            of such contributions
    
    """

    # Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIdxs = [int(dataConst[constraintByType,1]), int(dataConst[constraintByType,1]+1)]
    constraintRowIdxs = [rowIn, rowIn + 1]

    # Rigid bodies model number
    parentBodyNumber = int(dataConst[constraintByType, 1])
    childBodyNumber = int(dataConst[constraintByType, 2])

    # parentBody and childBody Local Coordinates
    parentLocCoords = dataConst[constraintByType, 3:5]
    childLocCoords = dataConst[constraintByType, 5:7]

    # Create bodies 'C' Matrix
    parentCMatrix = assemble_C_matrix(parentLocCoords)
    childCMatrix = assemble_C_matrix(childLocCoords)

    # Create Parent and Child Rigid Body 'q' Coordinates
    parentQVec = q[4 * (parentBodyNumber - 1): 4 * (parentBodyNumber - 1) + 4]
    childQVec = q[4 * (childBodyNumber - 1): 4 * (childBodyNumber - 1) + 4]

    # Revolute joint constraint contribution to 'phi' vector
    phi[constraintRowIdxs] = np.dot(parentCMatrix, parentQVec) - np.dot(childCMatrix, childQVec)

    # Revolute joint constraint contribution to jacobian matrix
    # Define parent body columns and childBody columns in jacobian matrix
    parentColsIdxs = [4 * (parentBodyNumber - 1), 4 * (parentBodyNumber - 1) + 4]
    childColsIdxs = [4 * (childBodyNumber - 1), 4 * (childBodyNumber - 1) + 4]
    dPhidq[constraintRowIdxs, parentColsIdxs[0]: parentColsIdxs[-1]] = parentCMatrix
    dPhidq[constraintRowIdxs, childColsIdxs[0]:childColsIdxs[-1]] = -childCMatrix

    # Revolute joint constraint contribution to 'niu' vector
    niu[constraintRowIdxs] = 0.0

    # Revolute joint constraint contribution to 'gamma' vector
    gamma[constraintRowIdxs] = 0.0

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 2}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
