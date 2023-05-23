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


def initializeDataConst(nConstraintsByType):
    """
    
    Function ....
    
    
    Parameters:
        nConstraintsByType  :   int
                                number of constraints of the multibody system

    Returns:
                            :   numpy.ndarray
                            
    """

    # Create an empty row with placeholder values for each constraint line
    dataConstEmptyRow = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

    # Create the dataConst array by repeating the empty row for each constraint
    dataConst = np.array([dataConstEmptyRow for _ in range(nConstraintsByType)])

    # Return dataConst
    return dataConst


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
