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

def read_model_loc_coords(fpath):
    """
    
    Function reads the local coordinates of the points of interest 
    of each segment of the model.
    
    Parameters:
    fpath                   :   string
                                absolute path of the input file 
    
    
    Returns:
    model_segments_coords   :   dictionary
                                local coordinates of the points of interest 
                                of each segments of the model.
    """

    model_segments_coords = {}
    
    # Load model drivers data fromm input file
    all_coords = np.loadtxt(fpath, dtype='float', delimiter=',')
    
    if all_coords.ndim > 1:
        for _ in range(0, all_coords.shape[0]):
            prox_coords = all_coords[_, 1:3].tolist()
            distal_coords = all_coords[_, 3:5].tolist()
            model_segments_coords[_ + 1] = [prox_coords, distal_coords]
    elif all_coords.ndim == 1:
        prox_coords = all_coords[1:3].tolist()
        distal_coords = all_coords[3:5].tolist()
        model_segments_coords[1] = [prox_coords, distal_coords]
    
    return model_segments_coords
   
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)