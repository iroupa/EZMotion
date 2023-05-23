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

import wx
import wx.xrc


def set_sbSizer_foregroundcolour(widget, color, font_size, font_family, font_style, font_type):
    """
    
    Function sets the color, size, family, style and type of the 
    foregroundcolour of the sbSizer widget.
    
    Parameters:
        widget      :   class
                        widget to
        color       :   list
                        color of the font of the label of the widget
        font_size   :   int
                        color of the font of the label of the widget
                        size of the font of the widget label
        font_family :   string
                        family font of the widget label
        font_style  :   string
                        style of font of the widget label
        font_type   :   string
                        type of font of the widget label

    Returns:

    """ 

    sbSizer_input_files_box = widget.GetStaticBox()
    sbSizer_input_files_box.SetForegroundColour(color)
    sbSizer_input_files_box.SetFont(wx.Font(font_size, font_family, font_style, font_type, False, wx.EmptyString))


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
