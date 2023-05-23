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


def compute_export_model_loc_coords(fpath, export_fpath):
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

    model_segments_loc_coords = {}

    # Load modeling file data
    dataConst = np.loadtxt(fpath, dtype='float', delimiter=',')

    for row in dataConst:
        if row[0] == 9:
            moving_body_1 = row[2]
            moving_body_2 = row[3]
            moving_body_1_loc_coords = [row[6], row[7]]
            moving_body_2_loc_coords = [row[8], row[9]]

            if moving_body_1 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_1] = moving_body_1_loc_coords
            elif moving_body_1 in model_segments_loc_coords.keys():
                loc_coords = str(model_segments_loc_coords[moving_body_1])
                if str(moving_body_1_loc_coords).replace('[', '').replace(']', '') in loc_coords:
                    pass
                else:
                    model_segments_loc_coords[moving_body_1] = model_segments_loc_coords[moving_body_1] + \
                                                               moving_body_1_loc_coords

            if moving_body_2 not in model_segments_loc_coords.keys():
                model_segments_loc_coords[moving_body_2] = moving_body_2_loc_coords
            elif moving_body_2 in model_segments_loc_coords.keys():
                loc_coords = str(model_segments_loc_coords[moving_body_2])
                if str(moving_body_2_loc_coords).replace('[', '').replace(']', '') in loc_coords:
                    pass
                else:
                    model_segments_loc_coords[moving_body_2] = model_segments_loc_coords[
                                                                   moving_body_2] + moving_body_2_loc_coords

    # find the max number of local variables of each segment of the model
    maxlength = 0
    for _ in range(0, len(model_segments_loc_coords.keys())):
        length = len(model_segments_loc_coords[_ + 1])
        if length > maxlength:
            maxlength = length

    # normalize the length of the list of local variables of each segment of the model
    for _ in range(0, len(model_segments_loc_coords.keys())):
        length = len(model_segments_loc_coords[_ + 1])
        if length < maxlength:
            model_segments_loc_coords[_ + 1] = model_segments_loc_coords[_ + 1] + [0, 0]

    # Convert dictionary with the local variables of each segment of the model
    # to pandas dataframe
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
