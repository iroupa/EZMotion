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


def assemble_W_matrix(dataConst, dPhidq, trajectory_drivers_weight):
    """
    
    Function creates weight matrix W to perform weighted least square kinematic analysis

    Parameters
    dataConst                   :   list of floats
                                    local coordinates of arbitrary point 'P'
    dPhidq                      :   numpy.array
                                    jacobian matrix  of the system
    trajectory_drivers_weight   :   float
                                :   weight of each trajectory driver of the model

    Returns                     :  numpy.array
                                    matrix of weights to use in the weighted least square approach
                                    during the kinematic analysis
    """

    # Get the type of all kinematic constraints of the model
    constraint_types = dataConst[:, 0]

    # Create weights matrix ('W')
    W = np.ones(dPhidq.shape[0])

    # Update weights matrix in case of Mixed Coordinates are used
    if (12 or 13 or 14 or 15) in constraint_types:
        # trajectory_drivers_weight = 1.e-4
        trajectory_drivers_idxs = []
        for row in dataConst:
            if int(row[0]) == 6:
                trajectory_drivers_idxs.append(int(row[1]))
                trajectory_drivers_idxs.append(int(row[1]) + 1)

        for idx in trajectory_drivers_idxs:
            W[idx] = trajectory_drivers_weight
        W = np.diag(W)
    else:
        W = np.diag(W)

    return W


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
