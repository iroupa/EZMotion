# -*- coding: utf-8 -*-

import wx
import wx.xrc
from classes.MenuBar import MyMenuBar
from classes.Analysis_Panel import Analysis_Panel
from classes.Visualizer_Panel import Visualizer_Panel

class EZMotion_2D(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"EZMotion_2D", pos=wx.DefaultPosition,
                          size=wx.Size(478, 829), style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, -1), wx.Size(-1, -1))

        self.m_statusBar = self.CreateStatusBar(1, 0, wx.ID_ANY)

        self.m_menubar = MyMenuBar()

        self.SetMenuBar(self.m_menubar)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook_base = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        self.m_panel_analysis = Analysis_Panel(self.m_notebook_base)

        self.m_notebook_base.AddPage(self.m_panel_analysis, u"Analysis", True)

        self.m_panel_visualization = Visualizer_Panel(self.m_notebook_base)

        self.m_notebook_base.AddPage(self.m_panel_visualization, u"Visualization", False)

        bSizer.Add(self.m_notebook_base, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = EZMotion_2D(None)
    app.SetTopWindow(frame)
    frame.Show(True)
    app.MainLoop()

