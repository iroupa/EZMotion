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
import string
import os


class DirObjectValidator(wx.Validator):
    """ This validator is used to ensure that the user has entered something
        into the text object editor dialog's text field.
    """

    def __init__(self, flag):
        """ Standard constructor.
        """
        wx.Validator.__init__(self)
        self.flag = flag
        # self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        """
        Standard cloner.
            Note that every validator must implement the Clone() method.
        """
        return DirObjectValidator(self.flag)

    def Validate(self, win):
        """
        Validate the contents of the given text control.
        """
        dirCtrl = self.GetWindow()
        path = dirCtrl.GetPath()
        if self.flag == 'file':
            if not os.path.isfile(path):
                wx.MessageBox("Please select a valid input file!", "Error")
                dirCtrl.GetTextCtrl().SetBackgroundColour("pink")
                dirCtrl.SetFocus()
                dirCtrl.Refresh()
                return False
            else:
                dirCtrl.GetTextCtrl().SetBackgroundColour((255, 255, 255))
                dirCtrl.Refresh()
                return True
        if self.flag == 'dir':
            if not os.path.isfile(path):
                wx.MessageBox("Please select a valid directory!", "Error")
                dirCtrl.GetTextCtrl().SetBackgroundColour("pink")
                dirCtrl.SetFocus()
                dirCtrl.Refresh()
                return False
            else:
                dirCtrl.GetTextCtrl().SetBackgroundColour((255, 255, 255))
                dirCtrl.Refresh()
                return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
