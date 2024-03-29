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

import csv
import os
import numpy as np
import pandas as pd


def create_model_loc_coords_file(fpath, export_fpath):
    """
    
    Function exports the local coordinates of the points of interest of the multibody system to a .jt file
    that will be used to visualize the segments of the multibody system.

    Parameters:
        fpath                       :   string
                                        absolute path of the input file
        export_fpath                :   string
                                        absolute path of the output file

    Returns:
        model_segments_loc_coords   :   pandas.dataframe
                                        local coordinates of the points of interest of the multibody system

    """

    # Initialize the dictionary to store the local coordinates of model segments
    model_segments_loc_coords = {}

    # Load modeling file data
    dataConst = np.loadtxt(fpath, dtype='float', delimiter=',', comments='#')

    # Iterate through the rows of the data
    for row in dataConst:
        # Check if the kinematic constraint is a double support joint
        if row[0] == 1:
            moving_body_1 = row[1]

            if moving_body_1 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_1] = []

        elif row[0] == 8:
            # Get the number of the moving body
            moving_body_1 = row[1]

            # Get the local coordinates of the moving body
            moving_body_1_loc_coords = [row[2], row[3]]

            test_list_body_1 = model_segments_loc_coords[moving_body_1]
            sublist_body_1 = moving_body_1_loc_coords

            res = any(test_list_body_1[idx: idx + len(sublist_body_1)] == sublist_body_1
                      for idx in range(len(test_list_body_1) - len(sublist_body_1) + 1))

            if moving_body_1 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_1] = moving_body_1_loc_coords

            elif moving_body_1 in model_segments_loc_coords.keys():
                if not res:
                    model_segments_loc_coords[moving_body_1] = model_segments_loc_coords[
                                                                       moving_body_1] + moving_body_1_loc_coords

        # Check if the kinematic constraint is a revolute joint
        if row[0] == 9:
            moving_body_1 = row[1]
            moving_body_1_loc_coords = [row[3], row[4]]

            test_list_body_1 = model_segments_loc_coords[moving_body_1]
            sublist_body_1 = moving_body_1_loc_coords

            res = any(test_list_body_1[idx: idx + len(sublist_body_1)] == sublist_body_1
                      for idx in range(len(test_list_body_1) - len(sublist_body_1) + 1))

            # Update the model_segments_loc_coords dictionary for moving_body_1
            if moving_body_1 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_1] = moving_body_1_loc_coords

            elif moving_body_1 in model_segments_loc_coords.keys():
                if not res:
                    model_segments_loc_coords[moving_body_1] = model_segments_loc_coords[
                                                                       moving_body_1] + moving_body_1_loc_coords

            moving_body_2 = row[2]
            moving_body_2_loc_coords = [row[5], row[6]]
            test_list_body_2 = model_segments_loc_coords[moving_body_2]
            sublist_body_2 = moving_body_2_loc_coords

            res = any(test_list_body_2[idx: idx + len(sublist_body_2)] == sublist_body_2
                      for idx in range(len(test_list_body_2) - len(sublist_body_2) + 1))

            # Update the model_segments_loc_coords dictionary for moving_body_2
            if moving_body_2 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_2] = moving_body_2_loc_coords

            elif moving_body_2 in model_segments_loc_coords.keys():
                if not res:
                    model_segments_loc_coords[moving_body_2] = model_segments_loc_coords[
                                                                   moving_body_2] + moving_body_2_loc_coords

    for _ in sorted(model_segments_loc_coords.keys()):
        coords_length = len(model_segments_loc_coords[int(_)])
        model_segments_loc_coords[int(_)] = model_segments_loc_coords[int(_)] + [0]*(4 - coords_length)

    # Convert the dictionary with the local variables of each segment to a pandas dataframe
    data = pd.DataFrame.from_dict(model_segments_loc_coords).to_numpy()

    # Write the local variables of each segment into the output file
    with open(os.path.join(export_fpath.replace('\Outputs', ''), 'model_loc_coords.jt'), 'w', newline='') as f:
        write = csv.writer(f)
        for _ in range(0, len(model_segments_loc_coords.keys())):
            data_to_export = []
            data_to_export.append(_ + 1)
            for elem in model_segments_loc_coords[_ + 1]:
                data_to_export.append(elem)
            write.writerow(data_to_export)

    return pd.DataFrame.from_dict(model_segments_loc_coords)


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
