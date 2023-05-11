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

__author__ 		= 'Ivo_Roupa'
__copyright__ 	= "Copyright (C) 2023 Ivo Roupa"
__email__ 		= "iroupa@gmail.com"
__license__ 	= "Apache 2.0"

import csv

def read_gui_settings(fpath):
    """
    
    Function reads the EZ_Motion settings file.

    Parameters:
    fpath				    : 	str
                                absolute path to EZ_Motion settings file.

    Returns:
    gui_setting_parameters  :   dict
                                font_family, font_style, font_type and color of the gui panesl,
                                 sbSizers and static text widgets.
    """

    gui_setting_parameters = {}

    with open(fpath, 'r', newline='') as csvfile:
        filedata = csv.reader(csvfile, delimiter=' ')
        for row in filedata:
            if not row[0].startswith('#'):
                label, value = row[0].split(':')
                if len(value) > 3:
                    value = value.replace('(','').replace(')','')
                    value = tuple(map(int, value.split(',')))
                    gui_setting_parameters[label] = value
                else:
                    gui_setting_parameters[label] = int(value)

    return gui_setting_parameters
     
if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
    #
    # read_gui_settings(r'C:\Do
    # read_gui_settings(r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\preferences\preferences.txt')

