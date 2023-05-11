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

from assemble_C_matrix import assemble_C_matrix


def evaluate_translation_revolution_joint(nCoordinates, constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    Function computes and assigns the contributions of the translation revolute joint constraint equations between 
    two vectors to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic and dynamic analysis.

    Parameters:
    nCoordinates        :   int
                            Model total number of coordinates
    nConstraintByType   :   int
                            Number of constraints by type
    dataConst           :   numpy.ndarray
                            Constants matrix
    q                   :   numpy.ndarray
                            model coordinates vector
    qpto                :   numpy.ndarray
                            Velocity coordinates vector
    Phi                 :   numpy.ndarray
                            Model constraints vector
    dPhidq              :   numpy.ndarray
                            Model Jacobian matrix
    niu                 :   numpy.ndarray
                            right hand side velocity equations vector
    gamma               :   numpy.ndarray
                            right hand side acceleration equations vector

    Returns:
        {'Phi':phi,'dPhidq':dPhidq, 'niu':niu, 'gamma':gamma} : dictionary
                                                                Dictionary of numpy.ndarrays with the following
                                                                keys 'Phi', 'dPhidq', 'niu', 'gamma' and respective
                                                                values for Translation Joint Constraint.
    """

    # Row Idx to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    #constraintRowIdxs = [dataConst[constraintByType, 1], dataConst[constraintByType, 1] + 1]
    constraintRowIdxs = [rowIn, rowIn + 1]

    # Rigid bodies model number
    parentBodyNumber = int(dataConst[constraintByType, 2])
    childBodyNumber = int(dataConst[constraintByType, 3])

    # parentBody and childBody Local Coordinates
    # Point 'point1' belongs to parent body
    point1LocCoords = dataConst[constraintByType, 6:8]

	# Points 'point2' and 'point3' belong to child body
    point2LocCoords = dataConst[constraintByType, 8:10]
    point3LocCoords = dataConst[constraintByType, 10:12]
    
    # Create bodies 'C' Matrix
    # Parent Body
    point1_CMatrix  = assemble_C_matrix(point1LocCoords)

    # Child Body
    point2_CMatrix  = assemble_C_matrix(point2LocCoords)
    point3_CMatrix  = assemble_C_matrix(point3LocCoords)

    # Create Parent and Child Rigid Body 'q' Coordinates
    parentQVec = q[4*(parentBodyNumber-1):4*(parentBodyNumber-1)+4]
    childQVec  = q[4*(childBodyNumber-1) :4*(childBodyNumber-1)+4]

    # Create 'u' and 'v' normalized vectors
    uVector = np.dot(point1_CMatrix, parentQVec) - np.dot(point2_CMatrix, childQVec)
    vVector = np.dot(point3_CMatrix, childQVec) - np.dot(point2_CMatrix, childQVec)

    uVector = uVector/np.linalg.norm(uVector)
    vVector = vVector/np.linalg.norm(vVector)

    # Create 'u' and 'v' vectors Length
    uLength = dataConst[constraintByType, 4]
    vLength = dataConst[constraintByType, 5]

    # Create vector perpendicular to 'u' and 'v' vector
    uVectorPerp = np.array([-uVector[1], uVector[0]])
    vVectorPerp = np.array([-vVector[1], vVector[0]])

    # Translation Revolution joint constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVectorPerp, vVector) #- uLength*vLength*np.sin(0)

    # Translation Revolution joint constraint contribution to jacobian matrix
    # Parent Rigid Body
    # Define Parent Rigid Body Columns and childBody Columns in jacobian matrix
    parentColsIdxes = [4*(parentBodyNumber-1), 4*(parentBodyNumber-1)+ 4]
    childColsIdxes  = [4*(childBodyNumber-1) , 4*(childBodyNumber-1) + 4]

    R90 = np.array([[0, -1],
                    [1, 0]])

    C32 = point3_CMatrix - point2_CMatrix

    f = np.linalg.multi_dot((point1_CMatrix.T,R90.T,C32)).T

    # dPhidq[constraintRowIdx, parentColsIdxes[0]: parentColsIdxes[-1]] = -np.linalg.multi_dot((childQVec,(point1_CMatrix.T,R90.T,C32).T))
    dPhidq[constraintRowIndex, parentColsIdxes[0]: parentColsIdxes[-1]] = -np.linalg.multi_dot((childQVec,f))
    dPhidq[constraintRowIndex, childColsIdxes[0] : childColsIdxes[-1]] = np.linalg.multi_dot((childQVec,point2_CMatrix.T,R90.T,C32))

    # Revolute translation joint constraint contribution to 'niu' vector
    niu[constraintRowIndex]     = 0

    # Revolute translation joint constraint contribution to 'gamma' vector
    gamma[constraintRowIndex]   = -2*(np.linalg.norm(uVector))

    return {'Phi':phi,'dPhidq':dPhidq, 'niu':niu, 'gamma':gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
