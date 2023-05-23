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
from scipy import interpolate


def interpolate_1D_data(y, nPoints):
    """
    
    Function interpolates a time series to a specific number of points.
        
    Parameters:
        y       : numpy.array
                time series to interpolate

        nPoints :   int
                    number of points
    Returns:
        ynew    :   numpy.array
                    time series interpolated
    
    """

    # Create numpy array 'x' with the length of 'y' array to use as interpolation 'xs'
    x = np.arange(0, y.shape[0], 1)

    # Create interpolation function for 'x' and 'y' arrays
    f = interpolate.interp1d(x, y)

    # Create numpy array with new 'xs' values to interpolate 'y' values
    xnew = np.arange(x[0], x[-1], (x[-1] - x[0])/nPoints)

    # Compute new 'y' values
    ynew = f(xnew)

    return ynew


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
