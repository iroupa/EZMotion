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
from classes.Dialog import MyDialog


class MyMenuBar(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self, style=0)

        self.m_menu_file = wx.Menu()
        self.m_menu_exit = wx.MenuItem(self.m_menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_file.Append(self.m_menu_exit)

        self.Append(self.m_menu_file, u"File")

        self.m_menu_edit = wx.Menu()

        self.m_menu_model_plot_lims = wx.MenuItem(self.m_menu_edit, wx.ID_ANY, u"Model Axes Values",
                                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_edit.Append(self.m_menu_model_plot_lims)

        self.m_menu_variable_plot_lims = wx.MenuItem(self.m_menu_edit, wx.ID_ANY, u"Variable Axes Values",
                                                     wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_edit.Append(self.m_menu_variable_plot_lims)

        self.Append(self.m_menu_edit, u"Edit")

        self.m_menu_view = wx.Menu()

        self.m_menu_CoM = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Model CoM", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_CoM)

        self.m_menu_model_segments_axes = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Segments Axes",
                                                      wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_model_segments_axes)

        self.m_menu_model_markers = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Model Markers",
                                                wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_model_markers)

        self.m_menu_grfs = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"GRFs", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_grfs)

        self.m_menu_grid = wx.MenuItem(self.m_menu_view, wx.ID_ANY, u"Model Grid", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_view.Append(self.m_menu_grid)

        self.Append(self.m_menu_view, u"View")

        self.m_menu_help = wx.Menu()
        self.m_menu_info = wx.MenuItem(self.m_menu_help, wx.ID_ANY, u"Info", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu_help.Append(self.m_menu_info)

        self.Append(self.m_menu_help, u"Help")

        # Connect Events
        self.Bind(wx.EVT_MENU, self.m_menu_exitOnMenuSelection, id=self.m_menu_exit.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_model_plot_limsOnMenuSelection, id=self.m_menu_model_plot_lims.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_variable_plot_limsOnMenuSelection, id=self.m_menu_variable_plot_lims.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_CoMOnMenuSelection, id=self.m_menu_CoM.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_model_segments_axesOnMenuSelection, id=self.m_menu_model_segments_axes.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_model_markersOnMenuSelection, id=self.m_menu_model_markers.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_grfsOnMenuSelection, id=self.m_menu_grfs.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_infoOnMenuSelection, id=self.m_menu_info.GetId())
        self.Bind(wx.EVT_MENU, self.m_menu_gridOnMenuSelection, id=self.m_menu_grid.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_menu_exitOnMenuSelection(self, event):
        self.Parent.Close()

    def m_menu_gridOnMenuSelection(self, event):
        try:
            if self.Parent.m_panel_visualization.m_plot_panel.show_grid:
                self.Parent.m_panel_visualization.m_plot_panel.show_grid = False
            elif not self.Parent.m_panel_visualization.m_plot_panel.show_grid:
                self.Parent.m_panel_visualization.m_plot_panel.show_grid = True
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_model_plot_limsOnMenuSelection(self, event):
        try:
            dlg = MyDialog(None, 'Model')
            result = dlg.ShowModal()
            if result:
                y_lims = [dlg.plot_y_axis_min, dlg.plot_y_axis_max]
                x_lims = [dlg.plot_x_axis_min, dlg.plot_x_axis_max]
                dlg.Destroy()
                self.Parent.m_panel_visualization.m_plot_panel.model_plot_ax.set_ylim(y_lims)
                self.Parent.m_panel_visualization.m_plot_panel.model_plot_ax.set_xlim(x_lims)
                self.Parent.m_panel_visualization.m_plot_panel.figure.canvas.draw()
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_variable_plot_limsOnMenuSelection(self, event):
        try:
            dlg = MyDialog(None, 'Variable')
            result = dlg.ShowModal()
            if result:
                y_lims = [dlg.plot_y_axis_min, dlg.plot_y_axis_max]
                x_lims = [dlg.plot_x_axis_min, dlg.plot_x_axis_max]
                dlg.Destroy()
                self.Parent.m_panel_visualization.m_plot_panel.variable_plot_ax.set_ylim(y_lims)
                self.Parent.m_panel_visualization.m_plot_panel.variable_plot_ax.set_xlim(x_lims)
                self.Parent.m_panel_visualization.m_plot_panel.figure.canvas.draw()
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_CoMOnMenuSelection(self, event):
        try:
            if self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = False
            elif not self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_CoM = True
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_model_segments_axesOnMenuSelection(self, event):
        try:
            if self.Parent.m_panel_visualization.m_plot_panel.show_model_refs:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = False
            elif not self.Parent.m_panel_visualization.m_plot_panel.show_model_refs:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_refs = True
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_model_markersOnMenuSelection(self, event):
        try:
            if self.Parent.m_panel_visualization.m_plot_panel.show_model_markers:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_markers = False
            elif not self.Parent.m_panel_visualization.m_plot_panel.show_model_markers:
                self.Parent.m_panel_visualization.m_plot_panel.show_model_markers = True
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_grfsOnMenuSelection(self, event):
        try:
            if self.Parent.m_panel_visualization.m_plot_panel.show_grfs:
                self.Parent.m_panel_visualization.m_plot_panel.show_grfs = False
            elif not self.Parent.m_panel_visualization.m_plot_panel.show_grfs:
                self.Parent.m_panel_visualization.m_plot_panel.show_grfs = True
        except Exception as e:
            dlg = wx.MessageDialog(None, str(e.__class__.__name__) + " : " + str(e), '', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pass

    def m_menu_infoOnMenuSelection(self, event):
        event.Skip()


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
