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

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal, stats, interpolate


def residual_analysis(data, fs, R2=0.9):
    """
    
    Function filters the data using the cut off frequency 
    defined by a regression analysis    

    Parameters:
        data    :  float
                    data to be filtered
        fs      :   int
                    sampling frequency
        R2      :   float
                    correlation coeficcient used during the linear regression
                    step of the residual analysis

    Returns:
        output  :   float
                    data filtered
        fcutoff :   float
                    cutoff frequency

    """

    # Range of cutt-off frequencies
    CutOffRange = np.arange(1, 0.2 * fs, 0.2)
    
    # Length of the data and frequencies
    nfreq = len(CutOffRange)
    ndata = len(data)
    
    # Allocates memory for the residual
    Residual = np.zeros(len(CutOffRange))
    
    # Goes through all frequencies and computes the residual
    for idx, fc in enumerate(CutOffRange):
        
        # Defines the cut-off frequency
        w = fc / (fs / 2)  # Normalize the frequency
        
        # Butterworth parameters
        b, a = signal.butter(2, w, 'low')
        
        # Filtering of the data with a zero phase lag filter
        fdata = signal.filtfilt(b, a, data)
        
        # Computation of the residual
        Residual[idx] = np.sqrt(np.sum(np.square(data - fdata)) / ndata)

    # Fits a line into the plot and finds the cut-off frequency         
    # Initial residual
    curResidual = 0

    # Index data
    Idxdata = 0

    # Debug mode
    Debug = 1
    # Increases the index data until the residual is larger than what was asked
    counter = 0
    while curResidual < R2:
        
        # Linear interpolation to the data
        slope, intercept, r_value, p_value, std_err = stats.linregress(CutOffRange[Idxdata::], Residual[Idxdata::])
        
        # Updates the residual
        curResidual = r_value**2
        
        # Increases the index
        Idxdata += 1

        # print(Idxdata)
        # If in debug mode, it plots the evolution of the regression
        if Debug == 0:
            plt.clf()
            plt.plot(CutOffRange, Residual, '-k', CutOffRange, slope*CutOffRange + intercept, '--b')

            fpath = r'Fig_0027_Chapter_04_residual_analysis_scheme_' + str(Idxdata) + '.png'
            plt.ylim([25, 45])
            plt.savefig(fpath, dpi=600, format="png")
            plt.pause(0.05)
       
    # Novel approach: Even though being likely less accurate, it should be
    # more stable. It finds the interval in which the residual is and
    # interpolates the data in between the points.    
    Idxdata = 1  # It should start in the second entry of the array
    freqint = -1  # Interval in which the frequency is defined
    while Idxdata < nfreq and freqint == -1:
        if Residual[Idxdata - 1] >= intercept and Residual[Idxdata] < intercept:
            freqint = Idxdata
        Idxdata += 1
    
    # Defines the cut-off frequency in Hz
    if freqint == -1:
        fcutoff = 0.5
    else:
        fcutoff = interpolate.interp1d([Residual[freqint - 1], Residual[freqint]], 
                                       [CutOffRange[freqint - 1], CutOffRange[freqint]])(intercept)
       
    # Final filtering of the data
    wf = fcutoff / (fs / 2)  # Normalize the frequency
        
    # Butterworth parameters
    b, a = signal.butter(2, wf, 'low')
            
    # Filtering of the data with a zero phase lag filter
    output = signal.filtfilt(b, a, data)
    
    if Debug == 0:
        plt.clf()
        plt.plot(np.arange(0, len(data), 1), data, '-', color='black'),
        plt.plot(np.arange(0, len(data), 1), output, '--', color='cornflowerblue')
        plt.show()
    
    return output, fcutoff


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
