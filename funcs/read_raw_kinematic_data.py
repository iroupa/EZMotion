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

import pandas as pd


def read_raw_kinematic_data(y, drivers_info):
    """
    
    Function computes the knots, coefficients and spline order for raw kinematic data
    and first and second spline derivatives.

    Parameters:
        y   			:   Pandas.dataframe
                        model drivers data
        drivers_info  	:   dictionary
                        dictionary with all model drivers number and respective
                        data to be splined
    
    Returns:
        output_data     : dictionary
                        knots, coefficients and spline order for raw data and
                        first and second spline derivatives
    
    """

    # Empty dictionary to store raw data and spline and derivatives parameters (knots, coefficients and spline order )
    output_data = {}

    # Iterate through driversNumberAndName and add data to dictionary
    for dofNumber, dofLabel in drivers_info.items():
        variableLength = len(y[dofLabel])
        output_data[dofNumber] = {'RawData': y[dofLabel],
                                  'splPos': pd.Series([0 for x in range(variableLength)]),
                                  'splVel': pd.Series([0 for x in range(variableLength)]),
                                  'splAcc': pd.Series([0 for x in range(variableLength)])}

    return output_data


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
