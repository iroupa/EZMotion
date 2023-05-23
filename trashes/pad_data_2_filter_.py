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


def pad_signal_(signal, slope_frames, start_idx, end_idx, nPads_begin, nPads_end):
    """

    Function returns augmented signal series in order to remove filter artifacts
    in the begin and in the end of the time series.

    Parameters:
        signal          :   numpy 1d array
                            signal to padding
        slope_frames    :   int
                            number of frames from original signal to use as regression
        start_idx       :   int

        end_idx         :   int

        nPads_begin     :   int

        nPads_end       :   int

    Returns:
                        :   numpy array
                            padded numpy array
    
    """

    signal_length = signal.shape[0]

    xs = np.arange(0, signal.shape[0])

    if nPads_begin > start_idx:
        nPads = start_idx - 1

    if nPads_end > (signal.shape[0] - end_idx):
        nPads_end = signal.shape[0] - end_idx

    y_init_func = np.polyfit(xs[start_idx:start_idx + slope_frames], signal[start_idx:start_idx+slope_frames], 1)
    y_init_estimated = np.polyval(y_init_func, xs[start_idx - nPads_begin:start_idx])

    y_end_func = np.polyfit(xs[end_idx-slope_frames:end_idx], signal[end_idx-slope_frames:end_idx], 1)
    y_end_estimated = np.polyval(y_end_func, xs[end_idx:end_idx + nPads_end])

    signal[start_idx - nPads_begin:start_idx-1] = y_init_estimated[1:]
    signal[end_idx:end_idx + nPads_end] = y_end_estimated

    return signal


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
