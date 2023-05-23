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


def read_model_rb_info(fpath):
    """
    
    Function reads the file containing the label of each segment of theHorsman muscle dataset and the number
     of that segment in the current model.

    Parameters:
        fpath       :   string
                        absolute path of the file containing the number and label of each Dof of the multibody system

    Returns:
        rb_info :   dictionary
                        number and label of each Dof of the multibody system
    
    """

    rb_info = {}

    with open(fpath, 'r', newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            if not line[0].startswith('#'):
                segment_label = line[0]
                rb_number = line[1]
                rb_info[segment_label] = rb_number

    return rb_info


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
