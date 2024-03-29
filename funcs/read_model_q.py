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


def read_model_q(fpath):
    """

    Function reads the generalized coordinates vector (q) of the multibody system from the input file.

    Parameters
        fpath   :   str
                    absolute path of the file containing the generalized
                    coordinates of the the multibody system

    Returns:
        q       :   numpy.array
                    generalized coordinates of the multibody system

    """

    q = []

    with open(fpath, 'r', newline='') as f:
        for line in f.readlines():
            elements_list = line.split(',')
            for elem in elements_list:
                elem = elem.strip()
                try:
                    q.append(float(elem))
                except Exception as error:  # pylint: disable=broad-except
                    pass

    return np.array(q, dtype='f')


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
