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


def glob_2_loc(pointP, origin, vector):
    """

    Function converts the global coordinates of point 'P' to local coordinates with respect to the
    local reference frame of a specific segment of the multibody system.

    Parameters:
        pointP            :   numpy.array
                              global coordinates of point 'P'
        origin            :   numpy.array
                              global coordinates of the origin of the local reference frame of body 'i'
        vector             :  numpy.ndarray
                              body 'i' orientation unitary vector

    Returns:
        local_coordinates :   numpy.array
                              local coordinates of point 'P' with respect to the local reference frame of
                              body 'i'

    """

    norm_vector = vector

    r90 = np.array([[0, -1],
                    [1, 0]])

    perp_vector = np.dot(r90, norm_vector)

    basis = np.array([[norm_vector[0], perp_vector[0]],
                      [norm_vector[1], perp_vector[1]]])

    local_coordinates = np.dot(basis.T, (pointP - origin))

    return local_coordinates


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
