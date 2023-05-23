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


def check_non_negative(widget_input, msg):
    """

    Function checks if widget input is negative.

    Parameters:
        widget_input    :   float
                            widget input
        msg             :   str
                            message to return

    Returns:
                        :   boolean
                            True if widget_input is empty or False is widget_input is not empty

    """

    res = True

    if float(widget_input) < 0:
        wx.MessageBox(msg, 'Error',
                      wx.OK | wx.ICON_ERROR)
        raise
    else:
        return res


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
