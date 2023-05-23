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


def compute_axis_limits(xy_data, nRigidBodies, ax):
    """

    Function computes the 'x' and 'y' limits of the plot of the model.

    Parameters:
        xy_data         :   numpy.array
                            global cartesian coordinates of the extremities of the segments of the model

        nRigidBodies    :   int
                            number of rigid bodies of the model

    Returns:
        ax_xy_lims      :   list
                            'x' and 'y' limits of the plot

    """

    # Set threshold for max and min values of 'x' and 'y' xy data
    positive_scaling_factor = 0.75
    negative_scaling_factor = 1.25

    if xy_data.ndim > 1:
        axis_xlim = [np.amin(xy_data[:, 0::4]),
                     np.amax(xy_data[:, 0::4])]
        axis_ylim = [np.amin(xy_data[:, 1:nRigidBodies*4:4]),
                     np.amax(xy_data[:, 1:nRigidBodies*4:4])]
    elif xy_data.ndim < 2:
        axis_xlim = [0, xy_data.shape[0]]
        axis_ylim = [np.amin(xy_data),
                     np.amax(xy_data)]

    if ax.lower() == 'x':
        if axis_xlim[0] > 0:
            axis_xlim[0] = axis_xlim[0] * positive_scaling_factor
        if axis_xlim[0] < 0:
            axis_xlim[0] = axis_xlim[0] * negative_scaling_factor
        if axis_xlim[1] > 0:
            axis_xlim[1] = axis_xlim[1] * negative_scaling_factor
        if axis_xlim[1] < 0:
            axis_xlim[1] = axis_xlim[1] * positive_scaling_factor
    elif ax.lower() == 'y':
        if axis_ylim[0] > 0:
            axis_ylim[0] = axis_ylim[0] * positive_scaling_factor
        if axis_ylim[0] < 0:
            axis_ylim[0] = axis_ylim[0] * negative_scaling_factor
        if axis_ylim[1] > 0:
            axis_ylim[1] = axis_ylim[1] * negative_scaling_factor
        if axis_ylim[1] < 0:
            axis_ylim[1] = axis_ylim[1] * positive_scaling_factor
    elif ax.lower() == 'both':
        if axis_xlim[0] > 0:
            axis_xlim[0] = axis_xlim[0] * positive_scaling_factor
        if axis_xlim[0] < 0:
            axis_xlim[0] = axis_xlim[0] * negative_scaling_factor
        if axis_xlim[1] > 0:
            axis_xlim[1] = axis_xlim[1] * negative_scaling_factor
        if axis_xlim[1] < 0:
            axis_xlim[1] = axis_xlim[1] * positive_scaling_factor
        if axis_ylim[0] > 0:
            axis_ylim[0] = axis_ylim[0] * positive_scaling_factor
        if axis_ylim[0] < 0:
            axis_ylim[0] = axis_ylim[0] * negative_scaling_factor
        if axis_ylim[1] > 0:
            axis_ylim[1] = axis_ylim[1] * negative_scaling_factor
        if axis_ylim[1] < 0:
            axis_ylim[1] = axis_ylim[1] * positive_scaling_factor

    return axis_xlim, axis_ylim


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
