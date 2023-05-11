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

def initialize_analysis_variables(nCoordinates, totalNumberConstraints):
    """
    
    Function initializes the vectors and matrices used during the kinematic analysis.
   

    Parameters:
    nCoordinates            :   int
                                system total number of coordinates
    totalNumberConstraints  :   int
                                system total number of constraints

    Return:
    q       :   numpy.ndarray
                vector of generalized coordinates of the multibody system
    qp      :   numpy.ndarray
                vector of generalized velocities of the multibody system
    qpp     :   numpy.ndarray
                vector of generalized acceleration of the multibody system
    Phi     :   numpy.ndarray
                vector of kinematic constraint equations of the multibody system
    niu     :   numpy.ndarray
                vector of right hand side of velocity contraint equations of the multibody system
    gamma   :   numpy.ndarray
                vector of right hand side of acceleration contraint equations of the multibody system
    dPhidq  :   numpy.ndarray
                jacobian matrix of the multibody system

    """
    # Kinematic Analysis

    value = 0.0

    # Model Coordinates vector
    q = np.array([value] * nCoordinates)

    # Velocity coordinates vector
    qp = np.array([value] * nCoordinates)

    # Acceleration coordinates vector
    qpp = np.array([value] * nCoordinates)

    # Constraints vector
    Phi = np.array([value] * totalNumberConstraints)

    # 'niu' vector
    niu = np.array([value] * totalNumberConstraints)

    # 'gamma' vector
    gamma = np.array([value] * totalNumberConstraints)

    # Jacobian matrix
    dPhidq = np.zeros((totalNumberConstraints, nCoordinates))

    return q, qp, qpp, Phi, niu, gamma, dPhidq

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)