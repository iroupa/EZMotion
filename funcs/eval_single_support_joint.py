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


def evaluate_single_support_joint(nCoordinates, constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assigns the contributions of the single support joint constraint equations to phi vector,
    dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic and dynamic analysis.

    Parameters
    nCoordinates        :   int
                            Model total number of coordinates
    constraintByType    :   int
                            number of constraints by type
    dataConst           :   numpy.ndarray
                            Constants matrix
    q                   :   numpy.ndarray
                            model coordinates vector
    qpto                :   numpy.ndarray
                            model velocity coordinates vector
    phi                 :   numpy.ndarray
                            Model constraints vector
    dPhidq              :   numpy.ndarray
                            model Jacobian matrix
    niu                 :   numpy.ndarray
                            right hand side velocity equations vector
    gamma               :   numpy.ndarray
                            right hand side acceleration equations vector

    Return
                        :   Dictionary
                            Dictionary of numpy.ndarrays with the following
                            keys 'Phi', 'dPhidq', 'niu', 'gamma' and respective
                            values for Single Support constraint.
    """

    # Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIdx = int(dataConst[constraintByType,1])
    constraintRowIndex = rowIn

    # Rigid bodies model number
    movingBodyNumber = int(dataConst[constraintByType, 2])

    # Constraint Direction
    # 0 - x
    # 1 - y
    constraintDirection = int(dataConst[constraintByType, 3])

    # parentBody and childBody Local Coordinates
    movingLocCoords = dataConst[constraintByType, 6:8]
    supportCoords = dataConst[constraintByType, 8:10]

    # Create bodies 'C' Matrix
    movingCMatrix = assemble_C_matrix(movingLocCoords)

    # Create moving and Child Rigid Body 'q' Coordinates
    movingQVec = q[4*(movingBodyNumber-1):4*(movingBodyNumber-1)+4]

    # Single support constraint contribution to 'phi' vector
    # Row index must be constraintRowIdx -> to -> constraintRowIdx+2 due to slicing operation in Python. With
    # these idxs data will be inserted from row 'constraintRowIdx' to row 'constraintRowIdx + 1'
    phi[constraintRowIndex] = np.dot(movingCMatrix, movingQVec)[constraintDirection] - \
                              supportCoords[constraintDirection]

    # Single support constraint contribution to jacobian matrix
    # moving Rigid Body

    # Define moving Rigid Body Columns in jacobian matrix
    movingColsIdxs = [4*(movingBodyNumber-1), 4*(movingBodyNumber-1)+4]

    # Row index must be [constraintRowIdx : constraintRowIdx + 2] due to slicing operation in Python. With
    # these idxs data will be inserted from row 'constraintRowIdx' to row 'constraintRowIdx + 1'
    dPhidq[constraintRowIndex, movingColsIdxs[0]:movingColsIdxs[1]] = movingCMatrix[constraintDirection, :]

    # Single support  constraint contribution to 'niu' vector
    niu[constraintRowIndex] = 0.0

    # Single support  constraint contribution to 'gamma' vector
    gamma[constraintRowIndex] = 0.0

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
