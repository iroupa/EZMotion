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

def compute_contractile_element(muscle_info, fl_component, fv_component, mode):
    """
    Function computes the contractile force for every muscle, for a certain time instance.
    
    Parameters:
    muscle_info         : dictionary
                          muscle parameters database (fo, alfa, lo, lt, points) of the biomechanical model 
    fl_component        : list
                          force-length component for every muscle, for a certain time instance
    fv_component        : list
                          force-velocity component for every muscle, for a certain time instance
                          
    Returns:
    f_ce                : list
                          contractile force element for every muscle
    """
    
    # Initialize f_ce list
    f_ce = []
    
    # Go through every muscle
    for muscle_idx in range(0,len(muscle_info.keys())):
        # maximum isometric force
        fo = muscle_info[muscle_idx]['fo']

        muscle_length = fl_component[muscle_idx]
        muscle_velocity = fv_component[muscle_idx]

        if mode.lower() == 'on':
            f_ce_muscle = (muscle_length * muscle_velocity)/fo
        elif mode.lower() == 'off':
            f_ce_muscle = fo
        else:
            raise

        # Add value to contractile force list
        f_ce.append(f_ce_muscle)
    
    return f_ce
			
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)