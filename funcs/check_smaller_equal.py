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

import wx
import wx.xrc

def check_smaller_equal(widget_1, widget_2):
    """
    Function checks if the value of widget 1 is smaller or equal than the value of widget 2.

    widget_1: wx.classe

    widget_2: wx.classe

    msg: str
         message to return in case the value of widget 1 is smaler than the value of widget 2.

    Return: Boolean
            True if widget_input_1 is smaller that widget_input_2
    """
    value_1 = widget_1.GetValue()
    value_2 = widget_2.GetValue()

    if value_1 >= value_2:
        wx.MessageBox('Please select an initial frame smaller than the final frame', "Error")
        widget_1.SetBackgroundColour("pink")
        widget_1.SetFocus()
        widget_1.Refresh()
        widget_2.SetBackgroundColour("pink")
        widget_2.SetFocus()
        widget_2.Refresh()
        return False
    else:
        widget_1.SetBackgroundColour((255, 255, 255))
        widget_1.Refresh()
        widget_2.SetBackgroundColour((255, 255, 255))
        widget_2.Refresh()
        return True

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)