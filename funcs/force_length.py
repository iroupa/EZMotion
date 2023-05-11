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

import math

def compute_force_length_component(muscle_info, l_m, muscle_type):
    """
    
    Function computes the force-length component of each muscle of the biomechanical model, 
    for a given time instance.
    
    Parameters
    muscle_info        : dictionary
                         muscle parameters database (fo, alfa, lo, lt, points) of the biomechanical model 
    l_m                : list 
                         muscle fibers length of every muscle of the model  
                         
    Return
    fl_component       : list
                         force-length component of each muscle of the biomechanical model, 
                         for a certain time instance
    """
    
    # Initialize fl_component list 
    fl_component = []
    
    # Iterate through every muscle
    for muscle_idx in range(0, len(muscle_info.keys())):
        # maximum isometric force
        fo = muscle_info[muscle_idx]['fo']

        # optimal muscle fiber length
        lo = muscle_info[muscle_idx]['lm']

        # muscle fiber length
        lm = l_m[muscle_idx]

        # Compute force_length component
        if muscle_type.lower() == 'hill':
            fl_muscle = fo * math.exp(-((9/4)*((lm/lo) - (19/20)))**4 - (1/4)*((9/4)*((lm/lo) - (19/20)))**2)
        else:
            fl_muscle = fo

        fl_component.append(fl_muscle)

    return fl_component
        
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)