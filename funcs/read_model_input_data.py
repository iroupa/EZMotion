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
from filter_signal import butter_filter
from residual_analysis import residual_analysis


def read_model_input_data(fpath, filter_data='', fs=100, R2=0.9, fc=8, order=4):
    """
    
    Function reads and filter the model drivers data from file using 
    the residual analysis method proposed by Winter.

    Parameters:
        fpath       :   string
                        Absolute acquisition data file path
        filter_data :   string
                        filter model drivers data using the residual method ('residual_analysis')
                        or the butterworth ('butter) lowpass filter
        fs          :   float
                        data sampling frequency
        R2          :   float
                        coefficient of correlation between raw and filtered data
        fc          :   float
                        cutoff frequency
        order       :   int
                        order of the low pass butterworth filter used to filter the data

    Returns:
        result      :   pandas.DataFrame
                        model drivers data
    
    """

    result = pd.read_csv(fpath, delimiter=',', comment="#")
    
    header_labels = list(result.columns)

    if filter_data.lower() == 'residual_analysis':
        for column in header_labels:
            result[column], fcutoff = residual_analysis(result[column].to_numpy(), fs, R2=R2)
    elif filter_data.lower() == 'butter':
        for column in header_labels:
            result[column] = butter_filter(result[column].to_numpy(), fs, fc, order)
    elif filter_data.lower() == 'no':
        for column in header_labels:
            result[column] = result[column]

    return result


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
