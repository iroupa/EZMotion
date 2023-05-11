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

def evaluate_unit_vector(nCoordinates, nConstraintByType, dataConst, q, qpto, phi, dPhidq, niu, gamma, rowIn):
    """
    
    Function computes and assigns the contributions of the unit vector constraint equation to Phi vector, 
    dPhidq (Jacobian matrix), niu vector and gamma vector for kinematic and dynamic analysis.

    Parameters
    nCoordinates        :   int
                            Model total number of coordinates
    nConstraintByType   :   int
                            number of constraints by type
    dataConst           :   numpy.ndarray
                            Constants matrix
    q                   :   numpy.ndarray
                            model coordinates vector
    qpto                :   numpy.ndarray
                            Velocity coordinates vector
    Phi                 :   numpy.ndarray
                            Model constraints vector
    dPhidq              :   numpy.ndarray
                            model Jacobian matrix
    niu                 :   numpy.ndarray
                            right hand side velocity equations vector
    gamma               :   numpy.ndarray
                            right hand side acceleration equations vector

    Returns
                        :   dictionary
                            Dictionary of numpy.ndarrays with the following
                            keys 'Phi', 'dPhidq', 'niu', 'gamma' and respective
                            values for unit vector constraint.
    """
   
    # Row index to insert constraint contribution in 'Phi', 'Jacobian', 'niu' and 'gamma'
    # constraintRowIndex = int(dataConst[nConstraintByType][1])
    constraintRowIndex = rowIn

    # Rigid body model number
    bodyNumber = dataConst[nConstraintByType][2]

    # Vector 'u' components; and velcity
    uVector    =    q[int(4*(bodyNumber-1)+2):int(4*(bodyNumber-1)+4)]
    uVectorpto = qpto[int(4*(bodyNumber-1)+2):int(4*(bodyNumber-1)+4)]

    # Vector 'u' Length;
    uLength = dataConst[nConstraintByType][4]

    # Rigid Body Constraint contribution to 'phi' vector
    phi[constraintRowIndex] = np.dot(uVector, uVector) - uLength**2.0

    # Rigid Body Constraint contribution to jacobian matrix
    cols = [int(4*(bodyNumber-1)+2), int(4*(bodyNumber-1)+3)]

    dPhidq[constraintRowIndex, cols] = 2*uVector

    # Rigid Body Constraint contribution to 'niu' vector
    niu[constraintRowIndex] = 0.0

    # Rigid Body Constraint contribution to 'gamma' vector
    gamma[constraintRowIndex] = -2*np.dot(uVectorpto,uVectorpto)

    return {'Phi':phi,'dPhidq':dPhidq, 'niu':niu, 'gamma':gamma, 'rowOut': rowIn + 1}

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
