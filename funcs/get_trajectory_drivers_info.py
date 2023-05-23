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


def get_trajectory_drivers_info(fpath):
    """

    Function reads the modeling file and returns the idx of the trajectory drivers of the model


    Parameters:
        fpath							:	string
                                            absolute path of the modeling file

    Returns	:
        trajectory_drivers_idxs_info:	list
                                        indexes of trajectory drivers in jacobian matrix

    """

    trajectory_drivers_idxs_info = []

    modeling_file_data = np.loadtxt(fpath,
                                    dtype='float',
                                    delimiter=',',
                                    comments="#")

    for row in modeling_file_data:
        if row[0] == 6:
            trajectory_drivers_idxs_info.append(int(row[1]))
            trajectory_drivers_idxs_info.append(int(row[1]+1))

    return trajectory_drivers_idxs_info


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
