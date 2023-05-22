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


def compute_q_coords_labels(nRigidBodies, model_mixed_angular_drivers):
    """

    Function creates a list with the label of each generalized coordinate, including
    mixed coordinates if they exist of the model.

    Parameters:
        nRigidBodies                :   int
                                        number of rigid bodies of the multibody system
        model_mixed_angular_drivers :   numpy.array
                                        number of mixed angular drivers of the multibody system

    Returns:
        model_q_coordinates_labels  :   list
                                        labels of all generalized coordinates of the multibody system

    """

    model_q_coordinates_labels = []
    
    for _ in range(0, nRigidBodies):
        model_q_coordinates_labels += ['Body_' + str(_ + 1) + '_X']
        model_q_coordinates_labels += ['Body_' + str(_ + 1) + '_Y']
        model_q_coordinates_labels += ['Body_' + str(_ + 1) + '_Ux']
        model_q_coordinates_labels += ['Body_' + str(_ + 1) + '_Uy']
    for _ in range(0, model_mixed_angular_drivers):
        model_q_coordinates_labels += ['Mixed_Ang_Driver_' + str(_ + 1)]

    return model_q_coordinates_labels


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
