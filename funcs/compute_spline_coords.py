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

from compute_spline_der import compute_cubic_spline_derivative
from compute_spline_knots_coeffs import compute_spline_knots_coeffs_degree


def compute_spline_coords(time, y, splineDegree=3):
    """
    
    Function computes the spline knots and coefficients of the input spline and
    respective first and second derivative.

    Parameters:
        time                    :   Pandas.Series
                                    original time vector
        y       				:   dictionary
                                    dictionary with driver number and label of selected data
        splineDegree    		:   int
                                    spline degree

    Returns:
        dofsplKnotsCoeffsDegree :   dictionary
                                    knots, coefficients and spline order of input spline and respective
                                    first and second spline derivative.
    
    """

    # Empty dictionary to be filled with spline Knots Coeffs and Degree for each data column in 'y'
    dofsplKnotsCoeffsDegree = {}

    # Calculate spline, first and second derivative knots, coefficients and degree
    for dof in y.keys():
        tck = compute_spline_knots_coeffs_degree(time, y[dof]['RawData'], splineDegree=splineDegree)
        dofsplKnotsCoeffsDegree[dof] = {'splPos': tck,
                                        'splVel': compute_cubic_spline_derivative(tck, 1),
                                        'splAcc': compute_cubic_spline_derivative(tck, 2)}

    return dofsplKnotsCoeffsDegree


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
