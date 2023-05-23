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
from eval_kinematic_constraints import evaluate_kinematic_constraints


def kinematic_analysis(t, nRigidBodies, nCoordinates, nConstraintsByType, dataConst, q, qp, Phi, dPhidq, niu, gamma, erro, dataSplineFuncs):

    # Evaluate functions: const, Jacobian matrix and vectors niu and gamma
    modelKinematics = evaluate_kinematic_constraints(t, nRigidBodies, nCoordinates, nConstraintsByType, dataConst, q, qp, Phi, dPhidq, niu, gamma, dataSplineFuncs)
    
    dPhidq = modelKinematics['dPhidq']
    dPhidq_T = dPhidq.T
    Phi = modelKinematics['Phi']
        
    # Solution
    dq = np.linalg.solve(np.dot(dPhidq_T,dPhidq), np.dot(dPhidq_T,-Phi))
    
    # Calculate error. Dot product between two vectors returns a scalar
    erro = np.sqrt(np.dot(dq, dq))
    
    # Update positions with residual value
    q = q + dq
    
    return modelKinematics, erro, q