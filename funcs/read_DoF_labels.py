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


def read_DoF_labels(fpath):
    """
    
    Function reads the file containing the number and label of each degree of freedom (DoF) of the system.

    Parameters:
        fpath       :   string
                        absolute path of the file containing the number and label of each Dof of the multibody system
    
    Returns:
        dofs_labels :   dictionary
                        number and label of each Dof of the multibody system

    """

    dofs = {}

    with open(fpath, 'r', newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            dofs[int(line[0])] = line[1]

    return dofs


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
