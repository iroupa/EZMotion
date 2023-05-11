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

def assemble_C_matrix(localCoordinates):
    """
    
    Function creates change of basis matrix for an arbitrary point 'P' belonging to an arbitrary 
	rigid body 'i' 

    Parameters
    localCoordinates    :   list of floats
                            local coordinates of arbitrary point 'P'

    Return
                        :   numpy.ndarray
                            Numpy array with change of basis 'C' matrix for point 'P' based on local
                            coordinates reference frame w.r.t rigid Body 'i'
    """
	
    return np.array([[1, 0, localCoordinates[0], -localCoordinates[1]],
                  [0, 1, localCoordinates[1], localCoordinates[0]]])

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)