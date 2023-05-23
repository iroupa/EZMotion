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

from scipy import signal


def butter_filter(y, fs, fc, filter_order):
    """
    
    Function filters a time seris sing the butteworth filter.
    
    Parameters:
        y               :   numpy.array
                            input signal
        fs              :   int
                            signal sampling frequency
        fc              :   float
                            cuttof frequency in Hertz
        filter_order    :   int
                            order of the filter
    Returns:
                        :   numpy.array
                            input signal filtered
    
    """
    # Normalized frequency
    w = fc / (fs / 2)

    # Numerator (b) and denominator (a) polynomials of the IIR filter.
    b, a = signal.butter(filter_order, w, 'low')

    # Filtered signal
    return signal.filtfilt(b, a, y)


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
