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
from eval_kinematic_constraints_FD import evaluate_kinematic_constraints_FD
from update_G_vector import update_G_vector
from compute_splined_forces_coords import compute_splined_forces_coords

# scipy.integrate.odeint
# y0, t

# scipy.integrate.ode
# t, y0


def solve_equations_of_motion(y0, t, nRigidBodies, massMatrix, nCoordinates, nConstraintsByType, dataConst, Phi,
                              dPhidq, niu, gamma, alpha, beta, gravitationalForces, forceSplineFuncs='',
                              sda_Parameters='', MomentsofForce=''):

    gVector = np.zeros(nRigidBodies * 4)

    gVector = update_G_vector(gVector, gravitationalForces)

    q = y0[0:int(nCoordinates)]
    qp = y0[int(nCoordinates):]

    modelKinematics = evaluate_kinematic_constraints_FD(q,
                                                        t,
                                                        nRigidBodies,
                                                        nCoordinates,
                                                        nConstraintsByType,
                                                        dataConst,
                                                        qp,
                                                        Phi,
                                                        dPhidq,
                                                        niu,
                                                        gamma,
                                                        )

    if len(forceSplineFuncs.items()) > 0:
        gVector = compute_splined_forces_coords(t, q, forceSplineFuncs, gVector)

    # Compute spring and damper forces, convert to generalized forces and applied it to respective body
    # if len(sda_Parameters.items()) > 0:
    #
    #     forcesVector = {}
    #
    #     for sda, parameters in sda_Parameters.items():
    #         sdaForce = SpringDamperActuatorForce(q, qp, parameters)
    #         for body in sdaForce.keys():
    #             if body not in forcesVector:
    #                 forcesVector[body] = sdaForce[body]
    #             else:
    #                 forcesVector[body] = forcesVector[body] + sdaForce[body]
    #
    #     gVector = updateGVector(gVector, forcesVector)
    #
    # Compute interpolated moment of force, convert it to generalized forces and applied it to respective body
    # if len(MomentsofForce.items()) > 0:
    #     for body, moment in MomentsofForce.items():
    #         moment = splev(t, MomentsofForce[body]['splPos'], der=0)
    #         generalizedForce = moment2forceCouple(q, body, -moment*100)
    #         gVector = updateGVector(gVector, generalizedForce)
    #         print 'time',t,'moments',moment,'generalizedForce ',generalizedForce

    massMatrix_rows, massMatrix_cols = massMatrix.shape
    dPhidq_rows, dPhidq_cols = dPhidq.shape
    dPhidq_T_rows, dPhidq_T_cols = dPhidq.T.shape

    # Initialize mass matrix of the system
    M = np.zeros((massMatrix_rows + dPhidq_rows, massMatrix_cols + dPhidq_T_cols))

    # Assign mass matrix to 'M' matrix
    M[0:massMatrix_rows, 0:massMatrix_cols] = massMatrix

    # Assign dPhidq matrix to 'M' matrix
    M[massMatrix_rows:massMatrix_rows + dPhidq_rows, 0:dPhidq_cols] = dPhidq

    # Assign dPhidq.T matrix to 'M' matrix
    M[0: dPhidq_T_rows, massMatrix_cols:massMatrix_cols + dPhidq_T_cols] = dPhidq.T

    gammaBaumgarte = modelKinematics['gamma'] - 2 * alpha * (
                np.dot(modelKinematics['dPhidq'], qp) - modelKinematics['niu']) - (beta ** 2) * modelKinematics['Phi']

    b = np.concatenate((gVector, gammaBaumgarte))

    x = np.linalg.solve(M, b)

    qpp = x[0:nCoordinates]

    dydt = np.concatenate((qp, qpp))

    return dydt


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
