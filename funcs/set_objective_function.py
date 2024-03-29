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


def objective_function(x, nh, nm):
    """

    Function defines the cost function used in the static optimization.

    Parameters:
        x   :   numpy.array
                solution of the static optimization problem
        nh  :   int
                number of kinematic constraint equations
        nm  :   int
                number of muscles of the biomechanical model

    Returns:
        f0  :   float
                value of the objective function

    """

    a = x[nh:]

    fo = 0
    for m in range(nm):
        fo += a[m]**3

    return fo


def objective_function_der(x, nh, nm):
    """

    Function defines the cost function used in the static optimization.

    Parameters:
        x   :   numpy.array
                solution of the static optimization problem
        nh  :   int
                number of kinematic constraint equations
        nm  :   int
                number of muscles of the biomechanical model

    Returns:
        f0  :   numpy.array
                gradient of the objective function

    """

    gradient = np.zeros(nh+nm)

    for m in range(nh, nh+nm):
        gradient[m] = 3*(x[m]**2)

    return gradient


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
