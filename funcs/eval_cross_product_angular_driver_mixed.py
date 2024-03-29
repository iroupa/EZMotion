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


def evaluate_cross_product_angular_driver_mixed(nRigidBodies, nCoordinates, constraintByType, dataConst, q, qpto, phi,
                                                dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assign contributions of dot product angular  constraint between two vectors
    (support and moving) to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic 
    and dynamic analysis.

    Parameters:
        nRigidBodies        :   int
                                model number of rigid bodies
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
                                                                                            Contributions of Cross
                                                                                            Product Angular Mixed
                                                                                            Constraint to phi, dPhidq,
                                                                                            niu and gamma vectors and
                                                                                            the ending index of such
                                                                                            contributions
    
    """

    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIndex = int(dataConst[constraintByType, 1])
    constraintRowIndex = rowIn

    # Rigid bodies model number
    parentBodyNumber = int(dataConst[constraintByType, 1])
    childBodyNumber = int(dataConst[constraintByType, 2])

    # Degree of Freedom number
    dof = int(dataConst[constraintByType, 13])

    # Vector 'u' components
    uVector = q[4 * (parentBodyNumber-1) + 2: 4 * (parentBodyNumber-1) + 4]
    uVectorpto = qpto[4 * (parentBodyNumber - 1) + 2: 4 * (parentBodyNumber-1) + 4]

    # Vector 'u' Length;
    # uLength = dataConst[constraintByType, 4]
    uLength = 1

    # Vector 'u' perpendicular;
    uVectorPerp = np.array([-uVector[1], uVector[0]])
    uVectorPerppto = np.array([-uVectorpto[1], uVectorpto[0]])

    # Vector 'v' components
    vVector = q[4 * (childBodyNumber-1) + 2: 4 * (childBodyNumber-1) + 4]
    vVectorpto = qpto[4 * (childBodyNumber-1) + 2: 4 * (childBodyNumber-1) + 4]

    # Vector 'v' Length
    # vLength = dataConst[constraintByType, 5]
    vLength = 1

    # Vector 'v' perpendicular;
    vVectorPerp = np.array([-vVector[1], vVector[0]])
    vVectorPerppto = np.array([-vVectorpto[1], vVectorpto[0]])

    # Vector 'vPerp' Length;
    vPerpLength = vLength

    # Theta
    # Plus 'dof' to 'dof' idx greater than 1
    theta = q[4 * nRigidBodies - 1 + dof]

    # Rigid Body Constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVectorPerp, vVector) - uLength * vLength * np.sin(theta)

    # Parent Rigid Body Constraint contribution to jacobian matrix
    parentCols = [4 * (parentBodyNumber-1) + 2, 4 * (parentBodyNumber - 1) + 3]
    childCols = [4 * (childBodyNumber-1) + 2, 4 * (childBodyNumber - 1) + 3]
    dofColIdx = 4 * nRigidBodies - 1 + dof

    dPhidq[constraintRowIndex, parentCols] = -vVectorPerp
    dPhidq[constraintRowIndex, childCols] = uVectorPerp
    dPhidq[constraintRowIndex, dofColIdx] = -np.cos(theta)

    # Rigid Body Constraint contribution to 'niu' vector
    niu[constraintRowIndex] = 0

    # Thetap
    thetap = qpto[4 * nRigidBodies - 1 + dof]

    # Rigid Body Constraint contribution to 'gamma' vector
    gamma[constraintRowIndex] = - (2 * np.dot(uVectorPerppto, vVectorpto) + np.sin(theta) * (thetap ** 2))

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
