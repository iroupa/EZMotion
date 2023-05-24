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


def evaluate_trajectory_driver(nCoordinates, constraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assigns the contributions of the trajectory driver to Phi vector, dPhidq (Jacobian matrix), 
    niu vector and gamma vector for kinematic and dynamic analysis.

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
                                                                                            Contributions of Trajectory
                                                                                            Driver Constraint to phi,
                                                                                            dPhidq, niu and gamma
                                                                                            vectors and the ending index
                                                                                            of such contributions
    
    """

    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    constraintRowIdxs = [rowIn, rowIn + 1]

    # Rigid bodies model number
    BodyNumber = int(dataConst[constraintByType, 1])

    # Create Parent and Child Rigid Body 'q' Coordinates
    bodyQVec = q[4 * (BodyNumber - 1): 4 * (BodyNumber - 1) + 4]

    # Point 'P' Local Coordinates wrt Moving Body
    PointPLocCoords = dataConst[constraintByType, 4:6]

    # Point 'P' Local Coordinates wrt Moving Body
    pointPCMatrix = assemble_C_matrix(PointPLocCoords)

    # Prescribed Position = position_prescribed
    position_prescribed = dataConst[constraintByType, 6:8]

    # Moving Rigid Body Constraint contribution to 'phi' vector
    phi[constraintRowIdxs] = np.dot(pointPCMatrix, bodyQVec) - position_prescribed

    # Moving Rigid Body Constraint contribution to jacobian matrix
    bodyColsIdxs = [4 * (BodyNumber - 1), 4 * (BodyNumber - 1) + 4]
    dPhidq[constraintRowIdxs, bodyColsIdxs[0]:bodyColsIdxs[-1]] = pointPCMatrix

    # PrescribedVelocity
    velocity_prescribed = dataConst[constraintByType, 8:10]

    # Moving Rigid Body Constraint contribution to 'niu' vector
    niu[constraintRowIdxs] = velocity_prescribed

    # Prescribed Acceleration
    acceleration_prescribed = dataConst[constraintByType, 10:12]

    # Moving Rigid Body Constraint contribution to 'gamma' vector
    gamma[constraintRowIdxs] = acceleration_prescribed

    # Return
    return {'Phi': phi, 'dPhidq': dPhidq, 'niu': niu, 'gamma': gamma, 'rowOut': rowIn + 2}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
