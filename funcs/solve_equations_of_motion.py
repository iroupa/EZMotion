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
from scipy.interpolate import splev
from eval_kinematic_constraints_FD import evaluate_kinematic_constraints_FD
from update_G_vector import update_G_vector
from compute_splined_forces_coords import compute_splined_forces_coords
from compute_spring_damper_actuator_force import compute_spring_damper_actuator_force
from moment2forceCouple import moment2forceCouple


def solve_equations_of_motion(y0, t, nRigidBodies, massMatrix, nCoordinates, nConstraintsByType, dataConst, phi,
                              dPhidq, niu, gamma, alpha, beta, gravitationalForces, forceSplineFuncs='',
                              sda_Parameters='', MomentsofForce=''):
    """
       Solve the equations of motion for a multibody system.

       Parameters:
           y0                      :   numpy.array
                                       Initial state vector containing generalized coordinates and velocities
           t                       :   float
                                       Time instant at which to solve the equations of motion
           nRigidBodies            :   int
                                       Number of rigid bodies in the multibody system
           massMatrix              :   numpy.array
                                       Mass matrix of the multibody system
           nCoordinates            :   int
                                       Number of generalized coordinates of the multibody system
           nConstraintsByType      :   int
                                       Number of constraints of the multibody system
           dataConst               :   numpy.ndarray
                                       Array containing constant data for each constraint
           phi                     :   numpy.array
                                       Vector of constraint function values for each constraint
           dPhidq                  :   numpy.array
                                       Jacobian matrix of the constraint functions with respect to the
                                       generalized coordinates
           niu                     :   numpy.array
                                       Vector of constraint velocities for each constraint
           gamma                   :   float
                                       Damping coefficient
           alpha                   :   float
                                       Coefficient for Baumgarte stabilization
           beta                    :   float
                                       Coefficient for Baumgarte stabilization
           gravitationalForces     :   numpy.array
                                       Vector of gravitational forces acting on each rigid body
           forceSplineFuncs        :   str, optional
                                       Spline functions representing external forces acting on the system
           sda_Parameters          :   str, optional
                                       Parameters for Spring-Damper Actuators in the system
           MomentsofForce          :   str, optional
                                       Moments of force acting on the system

       Returns:
           dydt                    :   numpy.array
                                       Derivatives of the state vector with respect to time

       """

    # Calculate gravitational force vector
    gVector = np.zeros(nRigidBodies * 4)

    # Update vctor of external forces with gravitational forces
    gVector = update_G_vector(gVector, gravitationalForces)

    # Assign position initial state to vector 'q'
    q = y0[0:int(nCoordinates)]

    # Assign velocity initial state to vector 'qp'
    qp = y0[int(nCoordinates):]

    # Evaluate kinematic constraints
    modelKinematics = evaluate_kinematic_constraints_FD(q, t, nRigidBodies, nCoordinates, nConstraintsByType,
                                                        dataConst, qp, phi, dPhidq, niu, gamma)

    # print('gVector', gVector)
    # Check if external forces exist:
    if len(forceSplineFuncs.items()) > 0:
        # print('IFR')
        # Compute splined forces acting on the system
        gVector = compute_splined_forces_coords(t, q, forceSplineFuncs, gVector)
        # print('gVector', gVector)

    # Compute spring and damper forces, convert to generalized forces and applied it to respective body
    if len(sda_Parameters.items()) > 0:

        forcesVector = {}

        for sda, parameters in sda_Parameters.items():
            sdaForce = compute_spring_damper_actuator_force(q, qp, parameters)
            for body in sdaForce.keys():
                if body not in forcesVector:
                    forcesVector[body] = sdaForce[body]
                else:
                    forcesVector[body] = forcesVector[body] + sdaForce[body]

        gVector = update_G_vector(gVector, forcesVector)

    # Compute interpolated moment of force, convert it to generalized forces and applied it to respective body
    if len(MomentsofForce.items()) > 0:
        for body, moment in MomentsofForce.items():
            moment = splev(t, MomentsofForce[body]['splPos'], der=0)
            generalizedForce = moment2forceCouple(q, body, -moment*100)
            gVector = update_G_vector(gVector, generalizedForce)

    # Obtain number of rows and columns of mass matrix of the multibody system
    massMatrix_rows, massMatrix_cols = massMatrix.shape

    # Obtain number of rows and columns of jacobian of the multibody system
    dPhidq_rows, dPhidq_cols = dPhidq.shape

    # Obtain number of rows and columns of transpose of jacobian of the multibody system
    dPhidq_T_rows, dPhidq_T_cols = dPhidq.T.shape

    # Initialize mass matrix of the system
    M = np.zeros((massMatrix_rows + dPhidq_rows, massMatrix_cols + dPhidq_T_cols))

    # Assign mass matrix to 'M' matrix
    M[0:massMatrix_rows, 0:massMatrix_cols] = massMatrix

    # Assign dPhidq matrix to 'M' matrix
    M[massMatrix_rows:massMatrix_rows + dPhidq_rows, 0:dPhidq_cols] = dPhidq

    # Assign dPhidq.T matrix to 'M' matrix
    M[0: dPhidq_T_rows, massMatrix_cols:massMatrix_cols + dPhidq_T_cols] = dPhidq.T

    # Compute gamma vector according to Baumgarte method
    gammaBaumgarte = modelKinematics['gamma'] - 2 * alpha * (
                np.dot(modelKinematics['dPhidq'], qp) - modelKinematics['niu']) - (beta ** 2) * modelKinematics['Phi']

    # Concatenate vector of external generalized forces and Baumgarte gama vector
    b = np.concatenate((gVector, gammaBaumgarte))

    # Solve system of equations of motion
    x = np.linalg.solve(M, b)

    # Obtain vector fo generalized accelerations of the system
    qpp = x[0:nCoordinates]

    # Create the vector of derivatives of the state vector of the multibody system with respect to time
    dydt = np.concatenate((qp, qpp))

    # Return the vector of derivatives of the state vector of the multibody system with respect to time
    return dydt


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
