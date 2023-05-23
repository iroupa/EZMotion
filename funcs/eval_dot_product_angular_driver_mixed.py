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


def evaluate_dot_product_angular_driver_mixed(nRigidBodies, nCoordinates, constraintByType, dataConst, q, qpto, phi,
                                              dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assigns the contributions of the dot product angular constraint between two vectors
    (support and moving) to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic and 
    dynamic analysis.
    
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
                            : dictionary
                                Dictionary of numpy.ndarrays with the following
                                keys 'Phi', 'dPhidq', 'niu', 'gamma' and respective
                                values for Dot Product Angular  Constraint.
    
    """

    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIndex = int(dataConst[constraintByType,1])
    constraintRowIndex = rowIn

    # Rigid bodies model number
    parentBodyNumber = int(dataConst[constraintByType, 2])
    childBodyNumber = int(dataConst[constraintByType, 3])

    # Degree of Freedom number
    dof = int(dataConst[constraintByType, 13])

    # Vector 'u' components;
    # Moving Body 'x', and 'y' values ;
    uVector = q[4 * (parentBodyNumber - 1) + 2: 4 * (parentBodyNumber - 1) + 4]
    uVectorpto = qpto[4 * (parentBodyNumber - 1) + 2: 4 * (parentBodyNumber - 1) + 4]

    # Vector 'u' Length;
    uLength = dataConst[constraintByType, 4]

    # Vector 'v' components;
    # Ground body orientation
    vVector = q[4 * (childBodyNumber - 1) + 2: 4 * (childBodyNumber - 1) + 4]
    vVectorpto = qpto[4 * (childBodyNumber - 1) + 2: 4 * (childBodyNumber - 1) + 4]

    # Vector 'v' Length;
    vLength = dataConst[constraintByType, 5]

    # Theta
    # -1 Because Python starts at 0
    # Plus 'dof' to 'dof' idx greater than 1
    theta = q[4 * nRigidBodies - 1 + dof]

    # Thetap
    # Thetap == dTheta/dt  -> Newton's notation vs Leibnitz notation
    thetap = qpto[4 * nRigidBodies - 1 + dof]

    # Dot Product Angular Constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVector, vVector) - np.cos(theta)

    # Dot Product Angular Constraint to jacobian matrix
    parentColsIdxs = [4 * (parentBodyNumber - 1) + 2, 4 * (parentBodyNumber - 1) + 3]
    childColsIdxs = [4 * (childBodyNumber - 1) + 2, 4 * (childBodyNumber - 1) + 3]
    dofColIdx = 4 * nRigidBodies - 1 + dof

    # Dot Product Angular Constraint to jacobian matrix
    dPhidq[constraintRowIndex, parentColsIdxs] = vVector
    dPhidq[constraintRowIndex, childColsIdxs] = uVector
    dPhidq[constraintRowIndex, dofColIdx] = np.sin(theta)

    # Dot Product Angular Constraint to 'niu' vector
    niu[constraintRowIndex] = 0.0

    # Dot Product Angular Constraint to 'gamma' vector
    gamma[constraintRowIndex] = -(2 * np.dot(uVectorpto, vVectorpto) + np.cos(theta) * (thetap ** 2))

    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 1}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
