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


def evaluate_cross_product_angular_driver(nCoordinates, constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma,
                                          rowIn):
    """
    
    Function computes and assign the contributions of the dot product angular constraint between two vectors
    (support and moving) to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector.

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
         {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}:   dictionary
                                                                                            Contributions of Cross
                                                                                            Product Angular Driver
                                                                                            Constraint to phi, dPhidq,
                                                                                            niu and gamma vectors and
                                                                                            the ending index of such
                                                                                            contributions

    """

    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIndex = int(dataConst[constraintByType, 1])
    constraintRowIndex = rowIn

    # Rigid bodies model number
    parentBodyNumber = int(dataConst[constraintByType, 2])
    childBodyNumber = int(dataConst[constraintByType, 3])

    # Vector 'u' components
    uVector = q[4 * (parentBodyNumber-1) + 2: 4 * (parentBodyNumber-1) + 4]
    uVectorpto = qpto[4*(parentBodyNumber-1) + 2: 4 * (parentBodyNumber-1) + 4]

    # Vector 'u' Length;
    uLength = dataConst[constraintByType, 4]

    # Vector 'u' perpendicular;
    uVectorPerp = np.array([-uVector[1], uVector[0]])
    uVectorPerppto = np.array([-uVectorpto[1], uVectorpto[0]])

    # Vector 'v' components
    vVector = q[4 * (childBodyNumber-1) + 2: 4 * (childBodyNumber-1) + 4]
    vVectorpto = qpto[4 * (childBodyNumber - 1) + 2: 4 * (childBodyNumber - 1) + 4]

    # Vector 'v' Length
    vLength = dataConst[constraintByType, 5]

    # Vector 'v' perpendicular;
    vVectorPerp = np.array([-vVector[1], vVector[0]])

    # Vector 'vPerp' Length;
    vPerpLength = vLength

    # Theta
    theta = dataConst[constraintByType, 10]

    # Rigid Body Constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVectorPerp, vVector) - uLength*vLength*np.sin(theta)

    # Parent Rigid Body Constraint contribution to jacobian matrix
    parentCols = [4*(parentBodyNumber-1)+2, 4*(parentBodyNumber-1)+3]
    childCols = [4*(childBodyNumber-1)+2, 4*(childBodyNumber-1)+3]

    dPhidq[constraintRowIndex, parentCols] = -vVectorPerp
    dPhidq[constraintRowIndex, childCols] = uVectorPerp

    # Thetap
    # Thetap == dTheta/dt -> Newton's notation vs Leibnitz notation
    thetap = dataConst[constraintByType, 11]

    # Rigid Body Constraint contribution to 'niu' vector
    niu[constraintRowIndex] = uLength*vLength*np.cos(theta)*thetap

    # Thetapp
    # Thetapp == d2Theta/dt2 -> Newton's notation vs Leibnitz notation
    thetapp = dataConst[constraintByType, 12]

    # Rigid Body Constraint contribution to 'gamma' vector
    gamma[constraintRowIndex] = -uLength*vLength*(np.sin(theta*thetap**2 - np.cos(theta)*thetapp) -
                                                  2*np.dot(uVectorPerppto, vVectorpto))

    # Return
    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
