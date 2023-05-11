# -*- coding: utf-8 -*-

import wx
import wx.xrc
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons


# class MyDialog(wx.Dialog):
#
#     def __init__(self, parent):
#         wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Set Axis limits", pos=wx.DefaultPosition,
#                            size=wx.Size(414, 175), style=wx.DEFAULT_DIALOG_STYLE)
#
#         self.y_axis_min = 0
#         self.y_axis_max = 0
#         self.x_axis_min = 0
#         self.x_axis_max = 0
#
#         self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
#
#         bSizer_root = wx.BoxSizer(wx.VERTICAL)
#
#         bSizer_11 = wx.BoxSizer(wx.HORIZONTAL)
#
#         self.m_static_axis_label = wx.StaticText(self, wx.ID_ANY, u"Axes", wx.DefaultPosition, wx.DefaultSize,
#                                                  wx.ALIGN_CENTRE)
#         self.m_static_axis_label.Wrap(-1)
#         self.m_static_axis_label.SetMinSize(wx.Size(50, -1))
#
#         bSizer_11.Add(self.m_static_axis_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
#
#         self.m_static_axis_label_min = wx.StaticText(self, wx.ID_ANY, u"Minimum", wx.DefaultPosition, wx.Size(100, -1),
#                                                      wx.ALIGN_CENTRE)
#         self.m_static_axis_label_min.Wrap(-1)
#         self.m_static_axis_label_min.SetMinSize(wx.Size(50, -1))
#
#         bSizer_11.Add(self.m_static_axis_label_min, 1, wx.ALL | wx.EXPAND, 5)
#
#         self.m_static_axis_label_max = wx.StaticText(self, wx.ID_ANY, u"Maximum", wx.DefaultPosition, wx.Size(100, -1),
#                                                      wx.ALIGN_CENTRE)
#         self.m_static_axis_label_max.Wrap(-1)
#         self.m_static_axis_label_max.SetMinSize(wx.Size(50, -1))
#
#         bSizer_11.Add(self.m_static_axis_label_max, 1, wx.ALL | wx.EXPAND, 5)
#
#         bSizer_root.Add(bSizer_11, 0, wx.EXPAND, 5)
#
#         bSizer_1 = wx.BoxSizer(wx.HORIZONTAL)
#
#         self.m_static_y_axis = wx.StaticText(self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
#         self.m_static_y_axis.Wrap(-1)
#         self.m_static_y_axis.SetMinSize(wx.Size(50, -1))
#
#         bSizer_1.Add(self.m_static_y_axis, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
#
#         self.m_textCtrl_y_axis_min = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
#                                                  0)
#         self.m_textCtrl_y_axis_min.SetMinSize(wx.Size(50, -1))
#
#         bSizer_1.Add(self.m_textCtrl_y_axis_min, 1, wx.ALL | wx.EXPAND, 5)
#
#         self.m_textCtrl_y_axis_max = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
#                                                  0)
#         bSizer_1.Add(self.m_textCtrl_y_axis_max, 1, wx.ALL | wx.EXPAND, 5)
#
#         bSizer_root.Add(bSizer_1, 0, wx.EXPAND, 5)
#
#         bSizer_2 = wx.BoxSizer(wx.HORIZONTAL)
#
#         self.m_static_x_axis = wx.StaticText(self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
#         self.m_static_x_axis.Wrap(-1)
#         self.m_static_x_axis.SetMinSize(wx.Size(50, -1))
#
#         bSizer_2.Add(self.m_static_x_axis, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
#
#         self.m_textCtrl_x_axis_min = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
#                                                  0)
#         bSizer_2.Add(self.m_textCtrl_x_axis_min, 1, wx.ALL | wx.EXPAND, 5)
#
#         self.m_textCtrl_x_axis_max = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
#                                                  0)
#         bSizer_2.Add(self.m_textCtrl_x_axis_max, 1, wx.ALL | wx.EXPAND, 5)
#
#         bSizer_root.Add(bSizer_2, 0, wx.EXPAND, 5)
#
#         bSizer3 = wx.BoxSizer(wx.VERTICAL)
#
#         self.m_button_apply_limits = wx.Button(self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0)
#
#         self.m_button_apply_limits.SetMinSize(wx.Size(-1, 25))
#
#         bSizer3.Add(self.m_button_apply_limits, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
#
#         bSizer_root.Add(bSizer3, 1, wx.EXPAND, 5)
#
#         self.SetSizer(bSizer_root)
#         self.Layout()
#
#         self.Centre(wx.BOTH)
#
#         # Connect Events
#         self.m_button_apply_limits.Bind(wx.EVT_BUTTON, self.m_button_apply_limitsOnButtonClick)
#
#     def __del__(self):
#         pass
#
#     # Virtual event handlers, overide them in your derived class
#     def m_button_apply_limitsOnButtonClick(self, event):
#         self.y_axis_min = float(self.m_textCtrl_y_axis_min.GetValue())
#         self.y_axis_max = float(self.m_textCtrl_y_axis_max.GetValue())
#         self.x_axis_min = float(self.m_textCtrl_x_axis_min.GetValue())
#         self.x_axis_max = float(self.m_textCtrl_x_axis_max.GetValue())
#         self.EndModal(True)


class MyDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Set Axis limits", pos=wx.DefaultPosition,
                           size=wx.Size(414, 173), style=wx.CAPTION | wx.CLOSE_BOX | wx.DEFAULT_DIALOG_STYLE)

        self.y_axis_min = None
        self.y_axis_max = None
        self.x_axis_min = None
        self.x_axis_max = None

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer_root = wx.BoxSizer(wx.VERTICAL)

        bSizer_11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_axis_label = wx.StaticText(self, wx.ID_ANY, u"Axes", wx.DefaultPosition, wx.DefaultSize,
                                                 wx.ALIGN_CENTRE)
        self.m_static_axis_label.Wrap(-1)
        self.m_static_axis_label.SetMinSize(wx.Size(50, -1))

        bSizer_11.Add(self.m_static_axis_label, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_static_axis_label_min = wx.StaticText(self, wx.ID_ANY, u"Minimum", wx.DefaultPosition, wx.Size(100, -1),
                                                     wx.ALIGN_CENTRE)
        self.m_static_axis_label_min.Wrap(-1)
        self.m_static_axis_label_min.SetMinSize(wx.Size(50, -1))

        bSizer_11.Add(self.m_static_axis_label_min, 1, wx.ALL | wx.EXPAND, 5)

        self.m_static_axis_label_max = wx.StaticText(self, wx.ID_ANY, u"Maximum", wx.DefaultPosition, wx.Size(100, -1),
                                                     wx.ALIGN_CENTRE)
        self.m_static_axis_label_max.Wrap(-1)
        self.m_static_axis_label_max.SetMinSize(wx.Size(50, -1))

        bSizer_11.Add(self.m_static_axis_label_max, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_root.Add(bSizer_11, 0, wx.EXPAND, 5)

        bSizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_y_axis = wx.StaticText(self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_static_y_axis.Wrap(-1)
        self.m_static_y_axis.SetMinSize(wx.Size(50, -1))

        bSizer_1.Add(self.m_static_y_axis, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_y_axis_min = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
                                                 0)
        self.m_textCtrl_y_axis_min.SetMinSize(wx.Size(50, -1))

        bSizer_1.Add(self.m_textCtrl_y_axis_min, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_y_axis_max = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
                                                 0)
        bSizer_1.Add(self.m_textCtrl_y_axis_max, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_root.Add(bSizer_1, 0, wx.EXPAND, 5)

        bSizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_x_axis = wx.StaticText(self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_static_x_axis.Wrap(-1)
        self.m_static_x_axis.SetMinSize(wx.Size(50, -1))

        bSizer_2.Add(self.m_static_x_axis, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl_x_axis_min = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
                                                 0)
        bSizer_2.Add(self.m_textCtrl_x_axis_min, 1, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_x_axis_max = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1),
                                                 0)
        bSizer_2.Add(self.m_textCtrl_x_axis_max, 1, wx.ALL | wx.EXPAND, 5)

        bSizer_root.Add(bSizer_2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_apply_limits_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_apply_limits_ok.SetMinSize(wx.Size(-1, 25))

        bSizer3.Add(self.m_button_apply_limits_ok, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        self.m_button_apply_limits_no = wx.Button(self, wx.ID_ANY, u"CANCEL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_apply_limits_no.SetMinSize(wx.Size(-1, 25))

        bSizer3.Add(self.m_button_apply_limits_no, 0, wx.ALIGN_LEFT | wx.ALL, 5)

        bSizer_root.Add(bSizer3, 0, wx.ALIGN_RIGHT, 5)

        self.SetSizer(bSizer_root)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_apply_limits_ok.Bind(wx.EVT_BUTTON, self.m_button_apply_limits_okOnButtonClick)
        self.m_button_apply_limits_no.Bind(wx.EVT_BUTTON, self.m_button_apply_limits_noOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_button_apply_limits_okOnButtonClick(self, event):
        # event.Skip()
            self.y_axis_min = float(self.m_textCtrl_y_axis_min.GetValue())
            self.y_axis_max = float(self.m_textCtrl_y_axis_max.GetValue())
            self.x_axis_min = float(self.m_textCtrl_x_axis_min.GetValue())
            self.x_axis_max = float(self.m_textCtrl_x_axis_max.GetValue())
            self.EndModal(True)

    def m_button_apply_limits_noOnButtonClick(self, event):
        # event.Skip()
        self.EndModal(False)

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)