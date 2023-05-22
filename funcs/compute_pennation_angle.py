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

import math


def compute_pennation_angle(muscle_info, l_mt):
    """
    Function computes the pennation angle for each muscle of the biomechanical model.

    Parameters:
    muscle_info       : dictionary
                        information about every muscle of the model
    l_mt              : list
                        musculotendon length of every muscle of the model
    Returns:
    pennation_angle   : list 
                        pennation angle for every muscle, for a given musculotendon length
    """
    
    # Initialize pennation_angle list
    pennation_angle = []

    # Iterate through each muscle
    for muscle_idx in range(0, len(muscle_info.keys())):

        # Optimal fiber length
        lo = muscle_info[muscle_idx]['lm']

        # Optimal pennation angle
        alfa_o = muscle_info[muscle_idx]['alpha']

        # Tendon slack length
        lt = muscle_info[muscle_idx]['lt']

        # Constant Isovolume Assumption
        muscle_width = lo * math.sin(alfa_o)

        pennation_angle.append(math.atan(muscle_width/(l_mt[muscle_idx] - lt)))

    return pennation_angle


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
