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


def update_G_vector(gVector, forceVector):
    """

    Function updates the vector of generalized external forces of the system.

    Parameters:
        gVector          :   numpy.array
                             vector of generalized forces of the multibody system
        forceVector      :   dictionary
                             body number and respective force

    Returns:
        gVector          :   numpy.ndarray
                             updated vector of generalized forces of the multibody system

    """

    # Assign input forces to generalized force vector
    for body, force in forceVector.items():
        idxs = [int(4*(body-1)), int(4*(body-1)+4)]
        gVector[idxs[0]: idxs[-1]] = gVector[idxs[0]: idxs[-1]] + force

    return gVector


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
