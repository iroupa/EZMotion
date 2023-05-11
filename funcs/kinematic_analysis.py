#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:35:04 2019

@author: ritapeneque
"""

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