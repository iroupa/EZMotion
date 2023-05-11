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
from scipy import interpolate

def interpolate_1D_data(y, nPoints):
    """
    
    Function interpolates a time series to a specific number of points.
        
    Parameters
    y       : numpy.array
            time series to interpolate   

    nPoints :   int
                number of points
    Return
    ynew    :   numpy.array
                time series interpolated
    """
    
    x = np.arange(0, y.shape[0], 1)

    f = interpolate.interp1d(x, y)

    xnew = np.arange(x[0], x[-1], (x[-1] - x[0])/nPoints)

    ynew = f(xnew)  # use interpolation function returned by `interp1d`

    return ynew
    
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
