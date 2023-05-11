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
from compute_joints_angles_inverse import compute_joints_angles_inverse
from eval_kinematic_constraints import evaluate_kinematic_constraints

def inverse_kinematic_analysis(frame,
                               t,
                               erroMax,
                               nRigidBodies,
                               nCoordinates,
                               nConstraintsByType,
                               modeling_file,
                               q,
                               qp,
                               dataSplineFuncs,
                               Phi,
                               dPhidq,
                               niu,
                               gamma,
                               W,
                               widget):
    """

    Function performs the inverse kinematic analysis of a multibody system.

    Parameters :
    frame               :   int
                            current frame of the kinematic analysis
    t                   :   float
                            time instant of the analysis
    q                   :   numpy.array
                            vector of generalized coordinates of the multibody system
    qp                  :   numpy.array
                            vector of generalized velocities of the multibody system
    erroMax             :   float
                            maximum admissible error for the Newton-Raphson method during the kinematic analysis
    nRigidBodies        :   int
                            number of rigid bodies of the multibody system
    nCoordinates        :   int
                            number of generalized coordinates of the multibody system
    nConstraintsByType  :   int
                            total number of kinematic constraints of the modeling file
    modeling_file       :   numpy.array
                            modeling file of the multibody system
    Phi                 :   numpy.array
                            vector of kinematic constraints of the multibdy system
    dPhidq              :   numpy.array
                            jacobian matrix of the kinematic constraints of the multibody system
    niu                 :   numpy.array
                            right hand side vector of the velocities constraint equations of the multibody system
    gamma               :   numpy.array
                            right hand side vector of the accelerations constraint equations of the multibody system
    dataSplineFuncs     :   dictionary
                            knots, coefficients and spline order of input spline and respective first and second spline derivative
    W                   :   numpy.array
                            weights matrix to be used during the kienamtci analysis
    widget              :   wx.TextBox
                            widget to print the kinematic analysis itertion and respective output

    Returns:
    modelKinematics     :   dictionary
                            Phi, dPhidq, niu and gamma vectors
    q                   :   numpy.array
                            vector of consistent generalized coordinates of the multibody system
    qp                  :   numpy.array
                            vector of consistent generalized velocities of the multibody system
    qpp                 :   numpy.array
                            vector of consistent generalized accelerations of the multibody system
    """

    erro = erroMax
    it = 0

    # Kinematic Analysis
    while erro >= erroMax:
        widget.AppendText('Kinematic Analysis: ' + 'Frame: ' + str(frame) +
                          ', Iteration: ' + str(it) + ', Error: ' + str(np.format_float_scientific(erro, 3)) + '\n')

        # Evaluate functions: const, Jacobian matrix and vectors niu and gamma
        modelKinematics = evaluate_kinematic_constraints(t,
                                                         nRigidBodies,
                                                         nCoordinates,
                                                         nConstraintsByType,
                                                         modeling_file,
                                                         q,
                                                         qp,
                                                         Phi,
                                                         dPhidq,
                                                         niu,
                                                         gamma,
                                                         dataSplineFuncs
                                                         )

        Aw = W.dot(modelKinematics['dPhidq'])
        Bw = W.dot(-modelKinematics['Phi'])

        # Solution
        dq = np.linalg.lstsq(Aw, Bw, rcond=None)[0]

        # Calculate error. Dot product between two vectors returns a scalar
        erro = np.sqrt(np.dot(dq, dq))

        it += 1

        # Update positions with residual value
        q = q + dq

    # Compute and assign model generalized velocities to report variable
    qp = np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['niu'], rcond=None)[0]

    # Compute and assign model generalized accelerations to report variable
    qpp = np.linalg.lstsq(modelKinematics['dPhidq'], modelKinematics['gamma'], rcond=None)[0]

    return modelKinematics, q, qp, qpp

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)