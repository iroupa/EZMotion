#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = 'Ivo_Roupa'
__version__ = '.001'
__date__ = '27_11_2017'

from eval_cross_product_angular_driver import evaluate_cross_product_angular_driver
from eval_cross_product_angular_driver_grounded import evaluate_cross_product_angular_driver_grounded
from eval_cross_product_angular_driver_grounded_mixed import evaluate_cross_product_angular_driver_grounded_mixed
from eval_cross_product_angular_driver_mixed import evaluate_cross_product_angular_driver_mixed
from eval_dot_product_angular_driver import evaluate_dot_product_angular_driver
from eval_dot_product_angular_driver_grounded import evaluate_dot_product_angular_driver_grounded
from eval_dot_product_angular_driver_grounded_mixed import evaluate_dot_product_angular_driver_grounded_mixed
from eval_dot_product_angular_driver_mixed import evaluate_dot_product_angular_driver_mixed
from eval_double_support_joint import evaluate_double_support_joint
from eval_revolute_joint import evaluate_revolute_joint
from eval_single_support_joint import evaluate_single_support_joint
from eval_trajectory_driver import evaluate_trajectory_driver
from eval_translation_revolution_joint import evaluate_translation_revolution_joint
from eval_unit_vector import evaluate_unit_vector

def evaluate_kinematic_constraints_FD(q, t, nRigidBodies, nCoordinates, nConstraintByType, dataConst, qpto, Phi, dPhidq, niu, gamma):
    """
    Function evaluates each system constraint type, calculates and assign it's contribution to Phi vector,
    dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic analysis.

    Parameters:
    t                   :   float64
                            time instant
    nCoordinates        :   int
                            number of coordinates
    nConstraintByTypes  :   int
                            number of constraints by type
    dataConst           :   numpy.ndarray
                            Constants matrix
    q                   :   numpy.ndarray
                            coordinates vector
    qpto                :   numpy.ndarray
                            coordinates velocity vector
    dPhidq              :   numpy.ndarray
                            Jacobian matrix
    niu                 :   numpy.ndarray
                            right hand side velocity equations vector
    gamma               :   numpy.ndarray
                            right hand side acceleration equations vector

    Returns:
    {'Phi': data['Phi'], 'dPhidq':data['dPhidq'], 'niu':data['niu'], 'gamma':data['gamma']} :   dictionary
                                                                                                Dictionary of arrays
                                                                                                with the following keys
                                                                                                'Phi', 'dPhidq', 'niu',
                                                                                                 'gamma' and respective
                                                                                                values for all model
                                                                                                constraints.
    """
    # Index of the contribution of the kinematic constraints
    rowIn = 0

    # Index of constraint type in dataConst Matrix
    constraintColumnIdx = 0

    for constraint in range(0, nConstraintByType):
        ## Unit vector
        if dataConst[constraint,constraintColumnIdx] == 1:
            data = evaluate_unit_vector(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Dot Product Constraint
        elif dataConst[constraint,constraintColumnIdx] == 2:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_dot_product_angular_driver(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Dot Product Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 3:
            # dataConst = updateDataConst(t, dataConst, func, constraint,0)
            data = evaluate_dot_product_angular_driver_grounded(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Cross Product Constraint
        elif dataConst[constraint,constraintColumnIdx] == 4:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_cross_product_angular_driver(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Cross Product Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 5:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_cross_product_angular_driver_grounded(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Trajectory Driver Constraint
        elif dataConst[constraint,constraintColumnIdx] == 6:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 1)
            data = evaluate_trajectory_driver(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Single Support Constraint
        elif dataConst[constraint,constraintColumnIdx] == 7:
            data = evaluate_single_support_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Double Support Constraint
        elif dataConst[constraint,constraintColumnIdx] == 8:
            data = evaluate_double_support_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Revolute Joint Constraint
        elif dataConst[constraint,constraintColumnIdx] == 9:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_revolute_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Translation Revolution Joint Constraint
        elif dataConst[constraint,constraintColumnIdx] == 10:
            # dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_translation_revolution_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Translation Joint Constraint
        # elif dataConst[constraint,constraintColumnIdx] == 11:
        #    data = evaluateTranslation(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
        #     rowIn = data['rowOut']

        # Mixed Cordinates Grounded Constraint
        elif dataConst[constraint, constraintColumnIdx] == 12:
            data = evaluate_dot_product_angular_driver_grounded_mixed(nRigidBodies, nCoordinates, constraint, dataConst, q, qpto, Phi,
                                                   dPhidq, niu, gamma, rowIn)
            rowIn = data['rowOut']

        # Mixed Cordinates Constraint
        elif dataConst[constraint, constraintColumnIdx] == 13:
            data = evaluate_dot_product_angular_driver_mixed(nRigidBodies, nCoordinates, constraint, dataConst, q, qpto, Phi,
                                                  dPhidq, niu, gamma, rowIn)
            rowIn = data['rowOut']

        # Mixed Cordinates Grounded Constraint
        elif dataConst[constraint, constraintColumnIdx] == 14:
            data = evaluate_cross_product_angular_driver_grounded_mixed(nRigidBodies, nCoordinates, constraint, dataConst, q, qpto, Phi,
                                                     dPhidq, niu, gamma, rowIn)
            rowIn = data['rowOut']

        # Mixed Cordinates Constraint
        elif dataConst[constraint, constraintColumnIdx] == 15:
            data = evaluate_cross_product_angular_driver_mixed(nRigidBodies, nCoordinates, constraint, dataConst, q, qpto, Phi,
                                                    dPhidq, niu, gamma, rowIn)
            rowIn = data['rowOut']

        else:
            print('Unknow constraint type !!!')

    return {'Phi': data['Phi'], 'dPhidq':data['dPhidq'], 'niu':data['niu'], 'gamma':data['gamma']}

if __name__ == '__main__':
    pass
    #doctest.testmod()
