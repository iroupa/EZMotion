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


def compute_spline_knots_coeffs_degree(time, y, splineDegree=3):
    """

    Function computes the vector of knots, the B-spline coefficients, and the degree of a spline.

    Parameters:
    time            :   Pandas.Series
                        original data time vector
    y       	    :   numpy.ndarray
                        data array to spline
    splineDegree    :   int
                        spline degree

    Returns:
    (t,c,k)          :  tuple
                        contains the vector of knots, the B-spline coefficients, and the degree of the spline.

    """
    
    from scipy.interpolate import splrep

    # Create cubic spline function for 'x' and 'y' values
    return splrep(time, y, s=0, k=splineDegree)


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
