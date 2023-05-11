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

from math import atan
from math import pi 

def compute_force_velocity_component(muscle_info, v_m, muscle_type):
    """
    
    Function computes the force-length component of each muscle of the biomechanical model, 
    for a given time instance.
    
    Parameters
    muscle_info          :  dictionary
                            information about every muscle of the model
    v_m                  :  list
                            velocity of every muscle, for a certain time instance
                         
    Return
    fv_component         :  list
                            force-velocity component of each muscle of the biomechanical model, for a certain time instance
    """
    
    # Initialize fl_component list 
    fv_component = []
    
    # Go through every muscle
    for muscle_idx in range(0,len(muscle_info.keys())):
        # maximum isometric force
        fo = muscle_info[muscle_idx]['fo']

        # resting length
        lo = muscle_info[muscle_idx]['lm']

        # maximum contractile velocity
        vo = 10 * lo

        # muscle velocity
        vm = v_m[muscle_idx]

        if vm < -vo:
            fv_muscle = 0
        elif -vo <= vm <= 0.2 * vo:
            fv_muscle = -(fo/atan(5)) * atan(-5 * (vm/vo)) + fo
        elif 0.2 * vo < vm:
            fv_muscle = + ((pi * fo)/(4 * atan(5))) + fo

        if muscle_type.lower() == 'hill':
            fv_component.append(fv_muscle)
        else:
            fv_component.append(fo)

    return fv_component
    
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)