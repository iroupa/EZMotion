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


def count_model_DoF(x):
    """

    Function returns the number of grounded, angular, trajectory, mixed
    and the total number of degrees of freedom of the multibody system.

    Parameters:
        x       :   numpy array
                    column of modeling file containing the type of each
    Returns:
                :   dictionary
                    number of grounded, angular, trajectory, mixed and the total
                    number of degrees of freedom of the multibody system

    """
    grounded_dofs = 0
    angular_dofs = []
    trajectory_dofs = 0
    mixed_dofs = []
    total_DoF = 0

    for row in x:
        if row[0] in [3, 5]:
            angular_dofs.append(row[13])
            grounded_dofs += 1
            total_DoF += 1
        if row[0] in [2, 4]:
            angular_dofs.append(row[13])
            total_DoF += 1
        elif row[0] in [6]:
            total_DoF += 2
            trajectory_dofs += 1
        elif row[0] in [12, 13, 14, 15]:
            total_DoF += 1
            mixed_dofs.append(row[13])

    if mixed_dofs == []:
        mixed_dofs = 0
    else:
        mixed_dofs = int(np.max(mixed_dofs))

    return {'total_dofs': total_DoF,
            'trajectory_dofs': trajectory_dofs,
            'mixed_dofs': mixed_dofs,
            'angular_dofs': list(set(angular_dofs))}


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
