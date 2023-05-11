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

def compute_eom_constraints(x, generalized_forces_vector, dPhidq, massMatrix, qpp, nCoordinates, g_M_pe, g_M_ce):
    """

      Function computes the equation of motion in the homogeneous form.

      Parameters:
      x                         :   numpy.array
                                    solution of the static optimization problem
      generalized_forces_vector :   numpy.array
                                    vector of generalized external forces of the multibody system
      dPhidq                    :   numpy.array
                                    jacobian matrix of the multibody system
      massMatrix                :   numpy.array
                                    mass matrix of the multibody system
      qpp                       :   numpy.array
                                    vector of generalized accelerations of the multibody system
      nCoordinates              :   int
                                    number of generalized coordinates of the multibody system
      g_M_pe                    :   numpy.array
                                    vector of generalized coordinates of the passive force of whole system for every muscle
      g_M_ce                    :   numpy.array
                                    vector of generalized coordinates of the contractile force of whole system for every muscle

      Returns:
      f_eq                      :   numpy.array
                                    equation of motion in the homogeneous form.

      """

    g_PE = np.zeros(nCoordinates)
    for g_pe in g_M_pe:
        g_PE += g_pe

    dPhidq_chi = np.append(dPhidq.T, - g_M_ce.T, axis=1)

    f_eq = massMatrix.dot(qpp) + dPhidq_chi.dot(x) - generalized_forces_vector - g_PE
    # print('f_eq', np.max(f_eq))
    return f_eq

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)