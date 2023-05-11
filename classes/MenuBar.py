# -*- coding: utf-8 -*-

import wx
import wx.xrc
from classes.Dialog import MyDialog

# class MyMenuBar_(wx.MenuBar):
#
#     def __init__(self):
#         wx.MenuBar.__init__(self, style=0)
#
#         self.m_menu_file = wx.Menu()
#         self.m_menu_exit = wx.MenuItem(self.m_menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
#         self.m_menu_file.Append(self.m_menu_exit)
#
#         self.Append(self.m_menu_file, u"File")
#
#         self.m_menu_view = wx.Menu()
#         self.m_menu_CoM = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"View / Hide CoM", wx.EmptyString, wx.ITEM_NORMAL)
#         self.m_menu_view.Append(self.m_menu_CoM)
#
#         self.m_menu_axes = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"View / Hide Axes", wx.EmptyString, wx.ITEM_NORMAL)
#         self.m_menu_view.Append(self.m_menu_axes)
#
#         # self.m_menu_powers = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Joint Power", wx.EmptyString, wx.ITEM_NORMAL)
#         # self.m_menu_view.Append(self.m_menu_powers)
#
#         self.Append(self.m_menu_view, u"View")
#
#         self.m_menu_help = wx.Menu()
#         self.m_menu_info = wx.MenuItem(self.m_menu_help, wx.ID_ANY, u"Info", wx.EmptyString, wx.ITEM_NORMAL)
#         self.m_menu_help.Append(self.m_menu_info)
#
#         self.Append(self.m_menu_help, u"Help")
#
#         # Connect Events
#         self.Bind(wx.EVT_MENU, self.m_menu_infoOnMenuSelection, id=self.m_menu_exit.GetId())
#         self.Bind(wx.EVT_MENU, self.m_menu_infoOnMenuSelection, id=self.m_menu_CoM.GetId())
#         self.Bind(wx.EVT_MENU, self.m_menu_infoOnMenuSelection, id=self.m_menu_axes.GetId())
#
#     def __del__(self):
#         pass
#
#     # Virtual event handlers, overide them in your derived class
#     def m_menu_infoOnMenuSelection(self, event):
#         id = event.GetId()
#         if id == self.m_menu_exit.GetId():
#             self.Parent.Close()
#         if id == self.m_menu_CoM.GetId():
#             if self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM == True:
#                 self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = False
#             elif self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM == False:
#                 self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = True
#         if id == self.m_menu_axes.GetId():
#             if self.Parent.m_panel_visualization.m_plot_panel.show_model_refs == True:
#                 self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = False
#             elif self.Parent.m_panel_visualization.m_plot_panel.show_model_refs == False:
#                 self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = True
#         # event.Skip()


class MyMenuBar(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self, style=0)

        self.m_menu_file = wx.Menu()
        self.m_menu_exit = wx.MenuItem(self.m_menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_file.Append(self.m_menu_exit)

        self.Append(self.m_menu_file, u"File")

        self.m_menu_edit = wx.Menu()
        self.m_menu_ax1_lims = wx.MenuItem(self.m_menu_edit, wx.ID_ANY, u"Axis 1", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_edit.Append(self.m_menu_ax1_lims)

        self.m_menu_ax2_lims = wx.MenuItem(self.m_menu_edit, wx.ID_ANY, u"Axis 2", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_edit.Append(self.m_menu_ax2_lims)

        self.Append(self.m_menu_edit, u"Edit")

        self.m_menu_view = wx.Menu()
        self.m_menu_CoM = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"CoM", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_CoM)

        self.m_menu_axes = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Axes", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_axes)

        self.Append(self.m_menu_view, u"View")

        self.m_menu_help = wx.Menu()
        self.m_menu_info = wx.MenuItem(self.m_menu_help, wx.ID_ANY, u"Info", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_help.Append(self.m_menu_info)

        self.Append(self.m_menu_help, u"Help")

        # Connect Events
        self.Bind(wx.EVT_MENU, self.m_menu_exitOnMenuSelection, id=self.m_menu_exit.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_ax1_limsOnMenuSelection, id=self.m_menu_ax1_lims.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_ax2_limsOnMenuSelection, id=self.m_menu_ax2_lims.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_CoMOnMenuSelection, id=self.m_menu_CoM.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_axesOnMenuSelection, id=self.m_menu_axes.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_infoOnMenuSelection, id=self.m_menu_info.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_menu_exitOnMenuSelection(self, event):
        # event.Skip()
        self.Parent.Close()

    def m_menu_ax1_limsOnMenuSelection(self, event):
        # event.Skip()
        dlg = MyDialog(None)
        result = dlg.ShowModal()
        if result:
            y_lims = [dlg.y_axis_min, dlg.y_axis_max]
            x_lims = [dlg.x_axis_min, dlg.x_axis_max]
            dlg.Destroy()
            self.Parent.m_panel_visualization.m_plot_panel.ax1.set_ylim(y_lims)
            self.Parent.m_panel_visualization.m_plot_panel.ax1.set_xlim(x_lims)
            self.Parent.m_panel_visualization.m_plot_panel.figure.canvas.draw()
        # else:
        #     dlg.EndModal()

    def m_menu_ax2_limsOnMenuSelection(self, event):
        # event.Skip()
        dlg = MyDialog(None)
        result = dlg.ShowModal()
        if result:
            y_lims = [dlg.y_axis_min, dlg.y_axis_max]
            x_lims = [dlg.x_axis_min, dlg.x_axis_max]
            dlg.Destroy()
            self.Parent.m_panel_visualization.m_plot_panel.ax2.set_ylim(y_lims)
            self.Parent.m_panel_visualization.m_plot_panel.ax2.set_xlim(x_lims)
            self.Parent.m_panel_visualization.m_plot_panel.figure.canvas.draw()
        # else:
        #     dlg.EndModal()

    def m_menu_CoMOnMenuSelection(self, event):
        # event.Skip()
        if self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM == True:
            self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = False
        elif self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM == False:
            self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = True

    def m_menu_axesOnMenuSelection(self, event):
        # event.Skip()
        if self.Parent.m_panel_visualization.m_plot_panel.show_model_refs == True:
            self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = False
        elif self.Parent.m_panel_visualization.m_plot_panel.show_model_refs == False:
            self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = True

    def m_menu_infoOnMenuSelection(self, event):
        event.Skip()


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)