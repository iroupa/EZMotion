# -*- coding: utf-8 -*-

import wx
from classes.Input_Files_Panel import Input_Files_Panel
from classes.Plot_Panel import Plot_Panel
import matplotlib as mpl

class Visualizer_Panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_splitter = wx.SplitterWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D)
        self.m_splitter.Bind(wx.EVT_IDLE, self.m_splitterOnIdle)
        self.m_splitter.SetMinimumPaneSize(250)

        self.m_inputs_panel = Input_Files_Panel(self.m_splitter)

        self.m_plot_panel = Plot_Panel(self.m_splitter)

        self.m_splitter.SplitVertically(self.m_inputs_panel, self.m_plot_panel, 0)
        bSizer.Add(self.m_splitter, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

    def __del__(self):
        pass

    def m_splitterOnIdle(self, event):
        self.m_splitter.SetSashPosition(0)
        self.m_splitter.Unbind(wx.EVT_IDLE)

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)