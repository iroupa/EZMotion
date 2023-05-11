# -*- coding: utf-8 -*-

import wx
import wx.xrc
import string

class TextObjectValidator(wx.Validator):
    """ This validator is used to ensure that the user has entered something
        into the text object editor dialog's text field.
    """

    def __init__(self, flag):
        """ Standard constructor.
        """
        wx.Validator.__init__(self)
        self.flag = flag
        # self.msg = msg
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        """ Standard cloner.

            Note that every validator must implement the Clone() method.
        """
        return TextObjectValidator(self.flag)

    def Validate(self, win):
        """ Validate the contents of the given text control.
        """
        # event.Skip()
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len(text) == 0:
            wx.MessageBox('Please insert a valid input ', "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour((255,255,255))
                # wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def OnChar(self, event):
        keycode = int(event.GetKeyCode())
        if keycode < 256:
            key = chr(keycode)
            if self.flag == 'no-alpha' and key in string.ascii_letters:
                return
            if self.flag == 'no-digit' and key in string.ascii_digits:
                return
        event.Skip()

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)