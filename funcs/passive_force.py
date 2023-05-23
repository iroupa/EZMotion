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


def compute_passive_element(muscle_info, l_m, f_pe_mode):
    """
    
    Function computes the passive element force for a certain time instance.
    
    Parameters:
        muscle_info         : dictionary
                              information about every muscle of the model
        l_m                 : list
                              muscle fibers length of every muscle of the model
        f_pe_mode           :

    Returns:
        f_pe                : list
                              passive force element for every muscle
    
    """
    
    # Initialize f_ce list
    f_pe = []
    
    # Go through every muscle
    for muscle_idx in range(0, len(muscle_info.keys())):
        # maximum isometric force
        fo = muscle_info[muscle_idx]['fo']

        # resting length
        lo = muscle_info[muscle_idx]['lm']

        # segment_length
        lm = l_m[muscle_idx]

        if lm < lo:
            f_pe_muscle = 0
        elif lo <= lm <= 1.63 * lo:
            f_pe_muscle = 8 * (fo/lo) * (lm - lo)**3
        elif 1.63 * lo < lm:
            f_pe_muscle = 2 * fo

        if f_pe_mode.lower() == 'on':
            f_pe.append(f_pe_muscle)
        elif f_pe_mode.lower() == 'off':
            f_pe.append(0)
        else:
            raise

    return f_pe


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
