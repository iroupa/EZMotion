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
from updateDataConst import updateDataConst


def evaluate_kinematic_constraints(t, nRigidBodies, nCoordinates, nConstraintByType, dataConst, q, qpto, Phi, dPhidq, niu, gamma, func):
    """
    
    Function computes the contribution of each constraint equation of the system and assigns its contribution 
    to Phi vector, dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic analysis and dynamic analysis.

    Parameters:
    t                   :   float64
                            time instant
    nRigidBodies        :   int
                            model number of rigid bodies
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
                        :   dictionary
                            Dictionary of arrays with the following keys 
                            'Phi', 'dPhidq', 'niu', 'gamma' and respective
                            values for all model constraints.
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
            dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_dot_product_angular_driver(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Dot Product Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 3:
            dataConst = updateDataConst(t, dataConst, func, constraint,0)
            data = evaluate_dot_product_angular_driver_grounded(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Cross Product Constraint
        elif dataConst[constraint,constraintColumnIdx] == 4:
            dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_cross_product_angular_driver(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Angular Driver Cross Product Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 5:
            dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_cross_product_angular_driver_grounded(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Trajectory Driver Constraint
        elif dataConst[constraint,constraintColumnIdx] == 6:
            dataConst = updateDataConst(t, dataConst, func, constraint, 1)
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
            dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_revolute_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Translation Revolution Joint Constraint
        elif dataConst[constraint,constraintColumnIdx] == 10:
            dataConst = updateDataConst(t, dataConst, func, constraint, 0)
            data = evaluate_translation_revolution_joint(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        ## Translation Joint Constraint
        # elif dataConst[constraint,constraintColumnIdx] == 11:
        #    data = evaluateTranslation(nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
        #    rowIn = data['rowOut']

        # Mixed Coordinates Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 12:
            data = evaluate_dot_product_angular_driver_grounded_mixed(nRigidBodies, nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        # Mixed Coordinates Constraint
        elif dataConst[constraint,constraintColumnIdx] == 13:
           data = evaluate_dot_product_angular_driver_mixed(nRigidBodies, nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
           rowIn = data['rowOut']

        # Mixed Coordinates Grounded Constraint
        elif dataConst[constraint,constraintColumnIdx] == 14:
           data = evaluate_cross_product_angular_driver_grounded_mixed(nRigidBodies, nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
           rowIn = data['rowOut']

        # Mixed Coordinates Constraint
        elif dataConst[constraint,constraintColumnIdx] == 15:
            data = evaluate_cross_product_angular_driver_mixed(nRigidBodies, nCoordinates,constraint,dataConst,q,qpto,Phi,dPhidq,niu,gamma, rowIn)
            rowIn = data['rowOut']

        else:
            print('Unknow constraint type !!!')

    return {'Phi': data['Phi'], 'dPhidq':data['dPhidq'], 'niu':data['niu'], 'gamma':data['gamma']}

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)