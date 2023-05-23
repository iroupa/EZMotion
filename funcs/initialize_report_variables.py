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


def initialize_report_variables(nFrames, nCoordinates, angDriversConstraints):
    """
    
    Function initializes the vectors and matrices used to report the outputs of the kinematic analysis.
    
    Parameters:
        nFrames                             :   int
                                                total number of acquisition frames
        nCoordinates                        :   int
                                                total number of coordinates
        angDriversConstraints               :   int
                                                total number of angular drivers constraints

    Returns:
        t_rep                   :   numpy.ndarray
                                    vector of generalized coordinates of the multibody system
        qp_rep                  :   numpy.ndarray
                                    vector of generalized velocities of the multibody system
        qpp_rep                 :   numpy.ndarray
                                    vector of generalized accelerations of the multibody system
        Phi_rep                 :   numpy.ndarray
                                    vector of constraint equations of the multibody system
        erro_rep                :   numpy.ndarray
                                    vector of Newton Raphson iteration error matrix during kinematic analysis
        theta_rep               :   numpy.ndarray
                                    angle of each revolute joint of the the multibody system
    """

    # t0 -> tf
    t_rep = np.array([0] * nFrames)

    # matrix [nFrames x len(q)]
    q_rep = np.zeros((nFrames, nCoordinates))

    # matrix [nFrames x len(qp)]
    qp_rep = np.zeros((nFrames, nCoordinates))

    # matrix [nFrames x len(qpp)]
    qpp_rep = np.zeros((nFrames, nCoordinates))

    # matrix [nFrames x len(phi)]
    phi_rep = np.zeros((nFrames, nCoordinates))

    # matrix [nFrames x len(erro)]
    erro_rep = np.zeros((nFrames, nCoordinates))

    # matrix [nFrames x len(theta_rep)]
    theta_rep = np.zeros((nFrames, angDriversConstraints))

    return t_rep, q_rep, qp_rep, qpp_rep, phi_rep, erro_rep, theta_rep


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
