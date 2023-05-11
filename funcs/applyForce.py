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

from assemble_C_matrix import assemble_C_matrix
import numpy as np
from typing import List

def applyForce(force: np.ndarray, locCoords: List[float]) -> np.ndarray:
    """
    Apply external force vector to generic body.

    Parameters:

    force    	:   numpy.array
    				force vector components wrt to body center of mass 
    locCoords	:   list
    				local coordinates of the application point of the applied force with respect to body 'i'
    
	Returns: 
    bodyforce   :   numpy.array
					force applied to point 'p' of body 'i' with local coordinates
    """

    cMatrix = assemble_C_matrix(locCoords)

    bodyforce = (cMatrix.T).dot(force)

    return bodyforce

if __name__ == '__main__':
    import doctest	

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)