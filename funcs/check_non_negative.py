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

    # Initialize the result variable as True
    res = True

    # Check if the widget input is less than 0
    if float(widget_input) < 0:
        # Display an error message box
        wx.MessageBox(msg, 'Error',
                      wx.OK | wx.ICON_ERROR)

        # Raise an exception to indicate the error
        raise

    else:

        # Return the result variable (True) if the input is non-negative
        return res


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
