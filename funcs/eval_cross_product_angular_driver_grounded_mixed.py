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


def evaluate_cross_product_angular_driver_grounded_mixed(nRigidBodies, nCoordinates, constraintByType, dataConst, q,
                                                         qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    Function computes and assigns contributions of cross product mixed angular grounded constraint between two 
    vectors (support and moving) to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic 
    and dynamic analysis.

    Parameters:
        nRigidBodies        :   int
                                model number of rigid bodies
        nCoordinates        :   int
                                Model total number of coordinates
        constraintByType   :   int
                                Number of constraints by type
        dataConst           :   numpy.ndarray
                                Constants matrix
        q                   :   numpy.ndarray
                                model coordinates vector
        qpto                :   numpy.ndarray
                                Velocity coordinates vector
        phi                 :   numpy.ndarray
                                Model constraints vector
        dPhidq              :   numpy.ndarray
                                Model Jacobian matrix
        niu                 :   numpy.ndarray
                                right hand side velocity equations vector
        gamma               :   numpy.ndarray
                                right hand side acceleration equations vector
        rowIn               :   int
                                number of line to insert kinematic constraint equation contribution in phi,
                                dPhidq, niu and gamma
    Returns:
                            :   dictionary
                                Dictionary of numpy.ndarrays with the following
                                keys 'Phi', 'dPhidq', 'niu', 'gamma' and respective
                                values for Dot Product Angular Grounded Constraint.
    """

    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIndex = int(dataConst[constraintByType,1])
    constraintRowIndex = rowIn

    # Rigid bodies model number
    movingBodyNumber = int(dataConst[constraintByType, 2])

    # Degree of Freedom number
    dof = int(dataConst[constraintByType, 13])

    # Vector 'u' components;
    uVector = q[int(4 * (movingBodyNumber-1)+2): int(4*(movingBodyNumber-1) + 4)]
    uVectorpto = qpto[int(4*(movingBodyNumber-1)+2): int(4*(movingBodyNumber-1) + 4)]

    # Vector 'u' Length;
    uLength = dataConst[constraintByType, 4]

    # Vector 'u' perpendicular;
    uVectorPerp = np.array([-uVector[1], uVector[0]])
    uVectorPerppto = np.array([-uVectorpto[1], uVectorpto[0]])

    # Vector 'uPerp' Length;
    uPerpLength = uLength
    
    # Vector 'v' components;
    vVector = dataConst[constraintByType, 8:10]
    vVectorpto = np.array([0.0, 0.0])

    # Vector 'v' Length;
    vLength = dataConst[constraintByType, 5]

    # Vector 'v' perpendicular;
    vVectorPerp = np.array([-vVector[1], vVector[0]])

    # Theta
    theta = q[4*nRigidBodies-1+dof]

    # Cross Product Angular Grounded Constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVectorPerp, vVector) - uLength * vLength * np.sin(theta)

    # Cross Product Angular Grounded Constraint to jacobian matrix
    movingBodyCols = [4 * (movingBodyNumber-1) + 2, 4 * (movingBodyNumber-1) + 3]
    dofColIdx = 4 * nRigidBodies - 1 + dof

    dPhidq[constraintRowIndex, movingBodyCols] = -vVectorPerp
    dPhidq[constraintRowIndex, dofColIdx] = -np.cos(theta)

    # Cross Product Angular Grounded Constraint to 'niu' vector
    niu[constraintRowIndex] = 0

    # Thetap
    thetap = qpto[4 * nRigidBodies - 1 + dof]

    # Cross Product Angular Grounded Constraint to 'gamma' vector
    gamma[constraintRowIndex] = - 2 * np.dot(uVectorPerppto, vVectorpto) + np.sin(theta) * (thetap ** 2)

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
