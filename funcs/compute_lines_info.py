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

from assemble_C_matrix import assemble_C_matrix
from read_model_loc_coords import read_model_loc_coords


def compute_lines_info(fpath, q):
    """

    Function compiles the data of each line of the multibody system to be plotted

    Parameters
    fpath		    :   str
                        absolute path of the file containing the local coordinates of ech sehgment to plot
    q				:   numpy.array
                        vector of generalized coordinates of the multibody system

    Return
    lines_info	    :   dictionary
                        body number and respective global coordinates of the model to plot

    """

    # Compiles data of each line of the multibody system to be plotted

    linesData = read_model_loc_coords(fpath)

    lines_info = {}

    if len(linesData.keys()) > 0:
        for body_number, loc_coords in linesData.items():
            joint_coords = {}
            for loc_coords_idx in range(0, len(loc_coords)):
                bodyCMatrix = assemble_C_matrix(loc_coords[loc_coords_idx])
                for _ in range(q.shape[0]):
                    bodyQVec = q[_, 4 * (body_number - 1):4 * (body_number - 1) + 4]
                    # joint = bodyCMatrix.dot(bodyQVec)
                    if _ in joint_coords:
                        joint_coords[_].update({'joint_' + str(loc_coords_idx + 1): bodyCMatrix.dot(bodyQVec)})
                    else:
                        joint_coords[_] = {'joint_' + str(loc_coords_idx + 1): bodyCMatrix.dot(bodyQVec)}
            lines_info[body_number] = joint_coords

    return lines_info


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
