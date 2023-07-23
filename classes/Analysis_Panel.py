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
import wx
import wx.xrc
import os
import numpy as np
import csv
from collections import Counter
import time
from read_gui_settings import read_gui_settings
from set_sbSizer_foreground_color import set_sbSizer_foregroundcolour
from set_staticText_foreground_color import set_staticText_foregroundcolour
from run_inverse_analysis import run_inverse_analysis
from run_forward_analysis import run_forward_analysis
from check_smaller_equal import check_smaller_equal
from classes.TextValidator import TextObjectValidator
from classes.DirValidator import DirObjectValidator
from read_model_outputs import read_model_outputs
from compute_lines_info import compute_lines_info
from compute_axis_limits import compute_axis_limits


class Analysis_Panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(528, 745),
                          style=wx.TAB_TRAVERSAL)

        bSizer_root = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow.SetScrollRate(5, 5)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_2 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_2.SetMinSize(wx.Size(-1, 15))
        sbSizer1_2_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Analysis Type"), wx.VERTICAL)

        bSizer1_2_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_analysis_type = wx.StaticText(sbSizer1_2_1.GetStaticBox(), wx.ID_ANY, u"Analysis",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_analysis_type.Wrap(-1)
        self.m_static_analysis_type.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_analysis_type.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_analysis_type.SetMinSize(wx.Size(150, -1))

        bSizer1_2_1_1.Add(self.m_static_analysis_type, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        m_comboBox_analysis_typeChoices = [u"Kinematic", u"Inverse Dynamic", u"Forward Dynamic", u"Musculoskeletal"]
        self.m_comboBox_analysis_type = wx.ComboBox(sbSizer1_2_1.GetStaticBox(), wx.ID_ANY, u"Kinematic",
                                                    wx.DefaultPosition, wx.DefaultSize, m_comboBox_analysis_typeChoices,
                                                    0)
        self.m_comboBox_analysis_type.SetSelection(0)
        bSizer1_2_1_1.Add(self.m_comboBox_analysis_type, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_2_1.Add(bSizer1_2_1_1, 1, wx.EXPAND, 5)

        bSizer1_2.Add(sbSizer1_2_1, 1, wx.ALL | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_2, 1, wx.EXPAND, 5)

        bSizer1_4 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_4_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Input Files Folder"),
                                         wx.VERTICAL)

        bSizer1_4_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_input_files_folder = wx.StaticText(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, u"Input Files Folder",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_input_files_folder.Wrap(-1)
        self.m_static_input_files_folder.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_input_files_folder.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_input_files_folder.SetMinSize(wx.Size(150, -1))

        bSizer1_4_1_1.Add(self.m_static_input_files_folder, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_dirPicker_input_files_folder = wx.DirPickerCtrl(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                               u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                               wx.DIRP_DEFAULT_STYLE, validator=DirObjectValidator('dir'))

        bSizer1_4_1_1.Add(self.m_dirPicker_input_files_folder, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_4_1.Add(bSizer1_4_1_1, 1, wx.EXPAND, 5)

        bSizer1_4.Add(sbSizer1_4_1, 1, wx.ALL | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_4, 1, wx.EXPAND, 5)

        bSizer1_6 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_6_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Input Files"), wx.VERTICAL)

        bSizer1_6_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_modeling_file = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Modeling File",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_modeling_file.Wrap(-1)
        self.m_static_modeling_file.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_modeling_file.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_modeling_file.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_1.Add(self.m_static_modeling_file, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_modeling_file = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                            u"Select a file", u"*.*", wx.DefaultPosition,
                                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer1_6_1_1.Add(self.m_filePicker_modeling_file, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_1, 0, wx.EXPAND, 5)

        bSizer1_6_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_state_q = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Model State (q)",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_state_q.Wrap(-1)
        self.m_static_model_state_q.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_model_state_q.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_model_state_q.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_2.Add(self.m_static_model_state_q, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_model_state_q = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                            u"Select a file", u"*.*", wx.DefaultPosition,
                                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))
        bSizer1_6_1_2.Add(self.m_filePicker_model_state_q, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_2, 0, wx.EXPAND, 15)

        bSizer1_6_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_state_qp = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Model State (qp)",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_state_qp.Wrap(-1)
        self.m_static_model_state_qp.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_model_state_qp.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_model_state_qp.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_3.Add(self.m_static_model_state_qp, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_model_state_qp = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                             u"Select a file", u"*.*", wx.DefaultPosition,
                                                             wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer1_6_1_3.Add(self.m_filePicker_model_state_qp, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_3, 1, wx.EXPAND, 5)

        bSizer1_6_1_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_drivers_labels = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Drivers Labels",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_drivers_labels.Wrap(-1)
        self.m_static_model_drivers_labels.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_4.Add(self.m_static_model_drivers_labels, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_model_drivers_labels = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY,
                                                                   wx.EmptyString, u"Select a file", u"*.*",
                                                                   wx.DefaultPosition, wx.DefaultSize,
                                                                   wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer1_6_1_4.Add(self.m_filePicker_model_drivers_labels, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_4, 0, wx.EXPAND, 5)

        bSizer1_6_1_5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_data = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Model Data",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_data.Wrap(-1)
        self.m_static_model_data.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_5.Add(self.m_static_model_data, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_model_data = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                         u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                         wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer1_6_1_5.Add(self.m_filePicker_model_data, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_5, 1, wx.EXPAND, 5)

        bSizer1_6_1_6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_force_files = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Force Files Folder",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_force_files.Wrap(-1)
        self.m_static_force_files.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_6.Add(self.m_static_force_files, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_dirPicker_force_files = wx.DirPickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                        u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                        wx.DIRP_DEFAULT_STYLE, validator=DirObjectValidator('dir'))

        bSizer1_6_1_6.Add(self.m_dirPicker_force_files, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_6, 1, wx.EXPAND, 5)

        bSizer1_6_1_7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_inertial_parameters = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY,
                                                          u"Inertial Parameters", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_inertial_parameters.Wrap(-1)
        self.m_static_inertial_parameters.SetMinSize(wx.Size(150, -1))

        bSizer1_6_1_7.Add(self.m_static_inertial_parameters, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_inertial_parameters = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY,
                                                                  wx.EmptyString, u"Select a file", u"*.*",
                                                                  wx.DefaultPosition, wx.DefaultSize,
                                                                  wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer1_6_1_7.Add(self.m_filePicker_inertial_parameters, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer1_6_1_7, 1, wx.EXPAND, 5)

        bSizer_1_6_1_8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_msk_database = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"MSK Parameters",
                                                   wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_msk_database.Wrap(-1)
        self.m_static_msk_database.SetMinSize(wx.Size(150, -1))

        bSizer_1_6_1_8.Add(self.m_static_msk_database, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_filePicker_msk_database = wx.FilePickerCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                           u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize,
                                                           wx.FLP_DEFAULT_STYLE, validator=DirObjectValidator('file'))

        bSizer_1_6_1_8.Add(self.m_filePicker_msk_database, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_6_1.Add(bSizer_1_6_1_8, 1, wx.EXPAND, 5)

        bSizer1_6.Add(sbSizer1_6_1, 0, wx.ALL | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_6, 0, wx.EXPAND, 5)

        bSizer1_8 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_8_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Analysis Parameters"),
                                         wx.VERTICAL)

        bSizer1_8_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_init_time = wx.StaticText(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, u"Initial Time (s)",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_init_time.Wrap(-1)
        self.m_static_init_time.SetMinSize(wx.Size(150, -1))

        bSizer1_8_1_1.Add(self.m_static_init_time, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_textCtrl_init_time = wx.TextCtrl(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition,
                                                wx.DefaultSize, 0, validator=TextObjectValidator('no-alpha'))

        bSizer1_8_1_1.Add(self.m_textCtrl_init_time, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_8_1.Add(bSizer1_8_1_1, 0, wx.EXPAND | wx.TOP, 15)

        bSizer1_8_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_end_time = wx.StaticText(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, u"Final Time (s)",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_end_time.Wrap(-1)
        self.m_static_end_time.SetMinSize(wx.Size(150, -1))

        bSizer1_8_1_2.Add(self.m_static_end_time, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_textCtrl_end_time = wx.TextCtrl(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0, validator=TextObjectValidator('no-alpha'))
        bSizer1_8_1_2.Add(self.m_textCtrl_end_time, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_8_1.Add(bSizer1_8_1_2, 0, wx.EXPAND, 5)

        bSizer1_8_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_sampling_frequency = wx.StaticText(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY,
                                                         u"Sampling Frequency (Hz)", wx.DefaultPosition, wx.DefaultSize,
                                                         0)
        self.m_static_sampling_frequency.Wrap(-1)
        self.m_static_sampling_frequency.SetMinSize(wx.Size(150, -1))

        bSizer1_8_1_3.Add(self.m_static_sampling_frequency, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_textCtrl_sampling_frequency = wx.TextCtrl(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, u"100",
                                                         wx.DefaultPosition, wx.DefaultSize, 0, validator=TextObjectValidator('no-alpha'))
        bSizer1_8_1_3.Add(self.m_textCtrl_sampling_frequency, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_8_1.Add(bSizer1_8_1_3, 0, wx.EXPAND, 5)

        bSizer1_8_1_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_subject_bodymass = wx.StaticText(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY,
                                                       u"Subject Bodymass (Kg)", wx.DefaultPosition, wx.DefaultSize,
                                                       0)
        self.m_static_subject_bodymass.Wrap(-1)
        self.m_static_subject_bodymass.SetMinSize(wx.Size(150, -1))

        bSizer1_8_1_4.Add(self.m_static_subject_bodymass, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_textCtrl_subject_bodymass = wx.TextCtrl(sbSizer1_8_1.GetStaticBox(), wx.ID_ANY, u"1",
                                                       wx.DefaultPosition, wx.DefaultSize, 0,
                                                       validator=TextObjectValidator('no-alpha'))

        bSizer1_8_1_4.Add(self.m_textCtrl_subject_bodymass, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_8_1.Add(bSizer1_8_1_4, 0, wx.EXPAND, 5)

        bSizer1_8.Add(sbSizer1_8_1, 0, wx.ALL | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_8, 0, wx.EXPAND, 5)

        bSizer1_10 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_10_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Export Files"),
                                          wx.HORIZONTAL)

        bSizer1_10_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_outputs_folder = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Outputs Folder",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_outputs_folder.Wrap(-1)
        self.m_static_outputs_folder.SetMinSize(wx.Size(150, -1))

        bSizer1_10_1_1.Add(self.m_static_outputs_folder, 0, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        self.m_dirPicker_outputs_folder = wx.DirPickerCtrl(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                           u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                           wx.DIRP_DEFAULT_STYLE, validator=DirObjectValidator('dir'))

        bSizer1_10_1_1.Add(self.m_dirPicker_outputs_folder, 1, wx.LEFT | wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        sbSizer1_10_1.Add(bSizer1_10_1_1, 1, wx.EXPAND | wx.TOP, 15)

        bSizer1_10.Add(sbSizer1_10_1, 0, wx.ALL | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_10, 0, wx.EXPAND, 5)

        bSizer1_12 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_analysis = wx.Button(self.m_scrolledWindow, wx.ID_ANY, u"Run Analysis ", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_button_analysis.SetMinSize(wx.Size(-1, 50))
        self.m_button_analysis.SetMaxSize(wx.Size(-1, 50))

        bSizer1_12.Add(self.m_button_analysis, 1, wx.EXPAND, 10)

        bSizer1.Add(bSizer1_12, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 17)

        bSizer1_14 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_14_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Messages"), wx.VERTICAL)

        self.m_textCtrl_Messages = wx.TextCtrl(sbSizer1_14_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.m_textCtrl_Messages.SetMinSize(wx.Size(-1, 150))

        sbSizer1_14_1.Add(self.m_textCtrl_Messages, 0, wx.EXPAND, 10)

        self.m_button_Messages_clear = wx.Button(sbSizer1_14_1.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)

        sbSizer1_14_1.Add(self.m_button_Messages_clear, 0, wx.ALIGN_RIGHT | wx.ALL, 10)

        bSizer1_14.Add(sbSizer1_14_1, 0, wx.ALL | wx.BOTTOM | wx.EXPAND | wx.TOP, 12)

        bSizer1.Add(bSizer1_14, 0, wx.EXPAND, 5)

        self.m_scrolledWindow.SetSizer(bSizer1)
        self.m_scrolledWindow.Layout()
        bSizer1.Fit(self.m_scrolledWindow)
        bSizer_root.Add(self.m_scrolledWindow, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer_root)
        self.Layout()

        # gui_settings = read_gui_settings(r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\preferences\preferences.txt')
        gui_settings = read_gui_settings(r'.\settings\preferences.txt')

        self.SetBackgroundColour(gui_settings['panel_backgroundcolour'])

        # Set sbSizers Input Files labels foreground color and font type
        sbSizers_list = [sbSizer1_2_1,
                         sbSizer1_4_1,
                         sbSizer1_6_1,
                         sbSizer1_8_1,
                         sbSizer1_10_1,
                         sbSizer1_14_1]

        for _ in sbSizers_list:
            set_sbSizer_foregroundcolour(_,
                                         gui_settings['sbSizers_labels_color'],
                                         gui_settings['sbSizers_labels_font_size'],
                                         gui_settings['sbSizers_labels_font_family'],
                                         gui_settings['sbSizers_labels_font_style'],
                                         gui_settings['sbSizers_labels_font_type'])

        # Set static labels preferences
        staticText_list = [self.m_static_analysis_type,
                           self.m_static_input_files_folder,
                           self.m_static_modeling_file,
                           self.m_static_model_state_q,
                           self.m_static_model_state_qp,
                           self.m_static_model_drivers_labels,
                           self.m_static_model_data,
                           self.m_static_force_files,
                           self.m_static_inertial_parameters,
                           self.m_static_msk_database,
                           self.m_static_init_time,
                           self.m_static_end_time,
                           self.m_static_sampling_frequency,
                           self.m_static_subject_bodymass,
                           self.m_static_outputs_folder
                           ]

        for _ in staticText_list:
            set_staticText_foregroundcolour(_,
                                            gui_settings['static_labels_color'],
                                            gui_settings['static_labels_font_size'],
                                            gui_settings['static_labels_font_family'],
                                            gui_settings['static_labels_font_style'],
                                            gui_settings['static_labels_font_type'])

        # Set button color and font type
        self.m_button_analysis.SetFont(wx.Font(gui_settings['button_font_size'],
                                               gui_settings['sbSizers_labels_font_family'],
                                               gui_settings['sbSizers_labels_font_style'],
                                               gui_settings['sbSizers_labels_font_type'],
                                               False,
                                               wx.EmptyString))

        self.m_button_analysis.SetBackgroundColour(gui_settings['button_background_color'])
        self.m_button_analysis.SetForegroundColour(gui_settings['button_foreground_color'])

        self.m_static_model_state_qp.Hide()
        self.m_filePicker_model_state_qp.Hide()
        self.m_static_force_files.Hide()
        self.m_dirPicker_force_files.Hide()
        self.m_static_inertial_parameters.Hide()
        self.m_filePicker_inertial_parameters.Hide()
        self.m_static_msk_database.Hide()
        self.m_filePicker_msk_database.Hide()

        # Connect Events
        self.m_comboBox_analysis_type.Bind(wx.EVT_COMBOBOX, self.m_comboBox_analysis_typeOnCombobox)
        self.m_comboBox_analysis_type.Bind(wx.EVT_UPDATE_UI, self.m_comboBox_analysis_typeOnUpdateUI)
        self.m_dirPicker_input_files_folder.Bind(wx.EVT_DIRPICKER_CHANGED,
                                                 self.m_dirPicker_input_files_folderOnDirChanged)
        self.m_filePicker_modeling_file.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_modeling_fileOnFileChanged)
        self.m_filePicker_model_state_q.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_model_state_qOnFileChanged)
        self.m_filePicker_model_state_qp.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_model_state_qpOnFileChanged)
        self.m_filePicker_model_drivers_labels.Bind(wx.EVT_FILEPICKER_CHANGED,
                                                    self.m_filePicker_model_drivers_labelsOnFileChanged)
        self.m_filePicker_model_data.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_model_dataOnFileChanged)
        self.m_dirPicker_force_files.Bind(wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker_force_filesOnDirChanged)
        self.m_filePicker_inertial_parameters.Bind(wx.EVT_FILEPICKER_CHANGED,
                                                   self.m_filePicker_inertial_parametersOnFileChanged)
        self.m_filePicker_msk_database.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_msk_databaseOnFileChanged)
        self.m_dirPicker_outputs_folder.Bind(wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker_outputs_folderOnDirChanged)
        self.m_button_analysis.Bind(wx.EVT_BUTTON, self.m_button_analysisOnButtonClick)
        self.m_button_Messages_clear.Bind(wx.EVT_BUTTON, self.m_button_Messages_clearOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_comboBox_analysis_typeOnCombobox(self, event):
        # two tabs here
        try:
            if self.m_comboBox_analysis_type.GetValue() == 'Kinematic':
                self.m_static_modeling_file.Show()
                self.m_filePicker_modeling_file.Show()
                self.m_static_model_state_q.Show()
                self.m_filePicker_model_state_q.Show()
                self.m_static_model_state_qp.Hide()
                self.m_filePicker_model_state_qp.Hide()
                self.m_static_model_drivers_labels.Show()
                self.m_filePicker_model_drivers_labels.Show()
                self.m_static_model_data.Show()
                self.m_filePicker_model_data.Show()
                self.m_static_force_files.Hide()
                self.m_dirPicker_force_files.Hide()
                self.m_static_inertial_parameters.Hide()
                self.m_filePicker_inertial_parameters.Hide()
                self.m_static_msk_database.Hide()
                self.m_filePicker_msk_database.Hide()
                self.Layout()
            elif self.m_comboBox_analysis_type.GetValue() == 'Inverse Dynamic':
                self.m_static_modeling_file.Show()
                self.m_filePicker_modeling_file.Show()
                self.m_static_model_state_q.Show()
                self.m_filePicker_model_state_q.Show()
                self.m_static_model_state_qp.Hide()
                self.m_filePicker_model_state_qp.Hide()
                self.m_static_model_drivers_labels.Show()
                self.m_filePicker_model_drivers_labels.Show()
                self.m_static_model_data.Show()
                self.m_filePicker_model_data.Show()
                self.m_static_force_files.Show()
                self.m_dirPicker_force_files.Show()
                self.m_static_inertial_parameters.Hide()
                self.m_filePicker_inertial_parameters.Hide()
                self.m_static_msk_database.Hide()
                self.m_filePicker_msk_database.Hide()
                self.Layout()
            elif self.m_comboBox_analysis_type.GetValue() == 'Forward Dynamic':
                self.m_static_modeling_file.Show()
                self.m_filePicker_modeling_file.Show()
                self.m_static_model_state_q.Show()
                self.m_filePicker_model_state_q.Show()
                self.m_static_model_state_qp.Show()
                self.m_filePicker_model_state_qp.Show()
                self.m_static_model_drivers_labels.Hide()
                self.m_filePicker_model_drivers_labels.Hide()
                self.m_static_model_data.Hide()
                self.m_filePicker_model_data.Hide()
                self.m_static_force_files.Show()
                self.m_dirPicker_force_files.Show()
                self.m_static_inertial_parameters.Hide()
                self.m_filePicker_inertial_parameters.Hide()
                self.m_static_msk_database.Hide()
                self.m_filePicker_msk_database.Hide()
                self.Layout()
            elif self.m_comboBox_analysis_type.GetValue() == 'Musculoskeletal':
                self.m_static_modeling_file.Show()
                self.m_filePicker_modeling_file.Show()
                self.m_static_model_state_q.Show()
                self.m_filePicker_model_state_q.Show()
                self.m_static_model_state_qp.Hide()
                self.m_filePicker_model_state_qp.Hide()
                self.m_static_model_drivers_labels.Show()
                self.m_filePicker_model_drivers_labels.Show()
                self.m_static_model_data.Show()
                self.m_filePicker_model_data.Show()
                self.m_static_force_files.Show()
                self.m_dirPicker_force_files.Show()
                self.m_static_inertial_parameters.Hide()
                self.m_filePicker_inertial_parameters.Hide()
                self.m_static_msk_database.Show()
                self.m_filePicker_msk_database.Show()
                self.Layout()

            # Update path of the input files filePicker widgets
            # if self.m_dirPicker_input_files_folder.GetPath() != '':
            if os.path.isdir(self.m_dirPicker_input_files_folder.GetPath()):
                if self.m_comboBox_analysis_type.GetValue() == 'Kinematic':
                    input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                    self.m_filePicker_modeling_file.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.mod')][0])

                    self.m_filePicker_model_state_q.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.q')][0])

                    self.m_filePicker_model_drivers_labels.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.lbl')][0])

                    self.m_filePicker_model_data.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.data')][0])

                    self.m_dirPicker_outputs_folder.SetPath(os.path.join(self.m_dirPicker_input_files_folder.GetPath()))

                elif self.m_comboBox_analysis_type.GetValue() == 'Forward Dynamic':
                    input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                    self.m_filePicker_modeling_file.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.mod')][0])

                    self.m_filePicker_model_state_q.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.q')][0])

                    self.m_filePicker_model_state_qp.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.qp')][0])

                    self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                    # self.m_filePicker_inertial_parameters.SetPath(
                    #     [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                    #      x.endswith('.mp')][0])

                    self.m_dirPicker_outputs_folder.SetPath(os.path.join(self.m_dirPicker_input_files_folder.GetPath()))

                elif self.m_comboBox_analysis_type.GetValue() == 'Inverse Dynamic':
                    input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                    self.m_filePicker_modeling_file.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.mod')][0])

                    self.m_filePicker_model_state_q.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.q')][0])

                    self.m_filePicker_model_drivers_labels.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.lbl')][0])

                    self.m_filePicker_model_data.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.data')][0])

                    self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                    # self.m_filePicker_inertial_parameters.SetPath(
                    #     [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                    #      x.endswith('.mp')][0])

                    self.m_dirPicker_outputs_folder.SetPath(os.path.join(self.m_dirPicker_input_files_folder.GetPath()))

                elif self.m_comboBox_analysis_type.GetValue() == 'Musculoskeletal':
                    input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                    self.m_filePicker_modeling_file.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.mod')][0])

                    self.m_filePicker_model_state_q.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.q')][0])

                    self.m_filePicker_model_drivers_labels.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.lbl')][0])

                    self.m_filePicker_model_data.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.data')][0])

                    self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                    # self.m_filePicker_inertial_parameters.SetPath(
                    #     [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                    #      x.endswith('.mp')][0])

                    self.m_filePicker_msk_database.SetPath(
                        [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                         x.endswith('.msk')][0])

                    self.m_dirPicker_outputs_folder.SetPath(os.path.join(self.m_dirPicker_input_files_folder.GetPath()))

        # two tabs here
        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

    def m_comboBox_analysis_typeOnUpdateUI(self, event):
        event.Skip()

    def m_dirPicker_input_files_folderOnDirChanged(self, event):
        # two tabs here
        try:
            if self.m_comboBox_analysis_type.GetValue() == 'Kinematic':
                input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                self.m_filePicker_modeling_file.SetPath([os.path.join(input_files_folder_fpath, x)
                                                         for x in os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.mod')][0])

                self.m_filePicker_model_state_q.SetPath([os.path.join(input_files_folder_fpath, x) for x
                                                         in os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.q')][0])

                self.m_filePicker_model_drivers_labels.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                                os.listdir(input_files_folder_fpath) if
                                                                x.endswith('.lbl')][0])

                self.m_filePicker_model_data.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                      os.listdir(input_files_folder_fpath) if
                                                      x.endswith('.data')][0])

            elif self.m_comboBox_analysis_type.GetValue() == 'Forward Dynamic':
                input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                self.m_filePicker_modeling_file.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.mod')][0])

                self.m_filePicker_model_state_q.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.q')][0])

                self.m_filePicker_model_state_qp.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                          os.listdir(input_files_folder_fpath) if
                                                          x.endswith('.qp')][0])

                self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                # self.m_filePicker_inertial_parameters.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                # os.listdir(input_files_folder_fpath) if
                #               x.endswith('.mp')][0])

            elif self.m_comboBox_analysis_type.GetValue() == 'Inverse Dynamic':
                input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                self.m_filePicker_modeling_file.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.mod')][0])

                self.m_filePicker_model_state_q.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.q')][0])

                self.m_filePicker_model_drivers_labels.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                                os.listdir(input_files_folder_fpath) if
                                                                x.endswith('.lbl')][0])

                self.m_filePicker_model_data.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                     os.listdir(input_files_folder_fpath) if
                                                      x.endswith('.data')][0])

                self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                # self.m_filePicker_inertial_parameters.SetPath([os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                #               x.endswith('.mp')][0])

            elif self.m_comboBox_analysis_type.GetValue() == 'Musculoskeletal':
                input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()
                self.m_filePicker_modeling_file.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.mod')][0])

                self.m_filePicker_model_state_q.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                         os.listdir(input_files_folder_fpath) if
                                                         x.endswith('.q')][0])

                self.m_filePicker_model_drivers_labels.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                                os.listdir(input_files_folder_fpath) if
                                                                x.endswith('.lbl')][0])

                self.m_filePicker_model_data.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                      os.listdir(input_files_folder_fpath) if
                                                      x.endswith('.data')][0])

                self.m_dirPicker_force_files.SetPath(input_files_folder_fpath)

                # self.m_filePicker_inertial_parameters.SetPath([os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                #               x.endswith('.mp')][0])

                self.m_filePicker_msk_database.SetPath([os.path.join(input_files_folder_fpath, x) for x in
                                                        os.listdir(input_files_folder_fpath) if
                                                        x.endswith('.msk')][0])

            self.m_dirPicker_outputs_folder.SetPath(self.m_dirPicker_input_files_folder.GetPath())

            if self.m_comboBox_analysis_type.GetValue() != 'Forward Dynamic':
                try:
                    fpath = self.m_filePicker_model_data.GetPath()
                    data = np.loadtxt(fpath, dtype='float', delimiter=',', skiprows=1)
                    self.m_textCtrl_init_time.SetValue(str(np.round(data[0, 0], 3)))
                    self.m_textCtrl_end_time.SetValue(str(np.round(data[-1, 0], 3)))

                # four tabs here
                except Exception as e:
                    self.m_textCtrl_Messages.AppendText(str(e) + '\n')
                    pass

        # two tabs here
        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass
        # event.Skip()

    def m_filePicker_modeling_fileOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_model_state_qOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_model_state_qpOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_model_drivers_labelsOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_model_dataOnFileChanged(self, event):
        event.Skip()

    def m_dirPicker_force_filesOnDirChanged(self, event):
        event.Skip()

    def m_filePicker_inertial_parametersOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_msk_databaseOnFileChanged(self, event):
        event.Skip()

    def m_dirPicker_outputs_folderOnDirChanged(self, event):
        event.Skip()

    def m_button_analysisOnButtonClick(self, event):
        # Disable run analysis button until the end of the analysis
        self.m_button_analysis.Enable(False)

        input_files_ctrls_list = []

        analysis_parameters_ctrls_list = [self.m_textCtrl_init_time,
                                          self.m_textCtrl_end_time,
                                          self.m_textCtrl_sampling_frequency]

        # two tabs here
        try:
            if self.m_comboBox_analysis_type.GetValue() == 'Kinematic':
                input_files_ctrls_list = [self.m_filePicker_modeling_file,
                                          self.m_filePicker_model_state_q,
                                          self.m_filePicker_model_drivers_labels,
                                          self.m_filePicker_model_data]

                input_folder_ctrls_list = [self.m_dirPicker_input_files_folder,
                                           self.m_dirPicker_outputs_folder]

            elif self.m_comboBox_analysis_type.GetValue() == 'Forward Dynamic':
                input_files_ctrls_list = [self.m_filePicker_modeling_file,
                                          self.m_filePicker_model_state_q,
                                          self.m_filePicker_model_state_qp,
                                          # self.m_filePicker_inertial_parameters
                                          ]

                input_folder_ctrls_list = [self.m_dirPicker_input_files_folder,
                                           self.m_dirPicker_force_files,
                                           self.m_dirPicker_outputs_folder]

            elif self.m_comboBox_analysis_type.GetValue() == 'Inverse Dynamic':
                input_files_ctrls_list = [self.m_filePicker_modeling_file,
                                          self.m_filePicker_model_state_q,
                                          self.m_filePicker_model_drivers_labels,
                                          self.m_filePicker_model_data,
                                          # self.m_filePicker_inertial_parameters
                                          ]

                input_folder_ctrls_list = [self.m_dirPicker_input_files_folder,
                                           self.m_dirPicker_force_files,
                                           self.m_dirPicker_outputs_folder]

            elif self.m_comboBox_analysis_type.GetValue() == 'Musculoskeletal':
                input_files_ctrls_list = [self.m_filePicker_modeling_file,
                                          self.m_filePicker_model_state_q,
                                          self.m_filePicker_model_drivers_labels,
                                          self.m_filePicker_model_data,
                                          # self.m_filePicker_inertial_parameters,
                                          self.m_filePicker_msk_database
                                          ]

            for ctrl in input_files_ctrls_list:
                ctrl.GetValidator().Validate(ctrl)

            for ctrl in analysis_parameters_ctrls_list:
                ctrl.GetValidator().Validate(ctrl)

            # three tabs here
            try:
                fs = float(self.m_textCtrl_sampling_frequency.GetValue())
                t0 = float(self.m_textCtrl_init_time.GetValue())

                tf_fpath = self.m_filePicker_model_data.GetPath()

                if self.m_comboBox_analysis_type.GetValue() != 'Forward Dynamic':
                    data = np.loadtxt(tf_fpath, dtype='float', delimiter=',', skiprows=1)
                tf = float(self.m_textCtrl_end_time.GetValue())

                check_smaller_equal(self.m_textCtrl_init_time, self.m_textCtrl_end_time)

                # four tabs here
                try:
                    # Clear Messages Text Box
                    self.m_textCtrl_Messages.Clear()

                    # Run analysis
                    if self.m_comboBox_analysis_type.GetValue() == 'Kinematic':
                        model_output_fpath = run_inverse_analysis(self.m_comboBox_analysis_type.GetValue(),
                                                                  float(self.m_textCtrl_subject_bodymass.GetValue()),
                                                                  self.m_filePicker_modeling_file.GetPath(),
                                                                  self.m_filePicker_model_data.GetPath(),
                                                                  self.m_filePicker_model_state_q.GetPath(),
                                                                  self.m_filePicker_model_drivers_labels.GetPath(),
                                                                  '',
                                                                  '',
                                                                  self.m_dirPicker_outputs_folder.GetPath(),
                                                                  float(self.m_textCtrl_sampling_frequency.GetValue()),
                                                                  float(self.m_textCtrl_init_time.GetValue()),
                                                                  float(self.m_textCtrl_end_time.GetValue()),
                                                                  'gui',
                                                                  self.m_textCtrl_Messages
                                                                  )

                    elif self.m_comboBox_analysis_type.GetValue() == 'Forward Dynamic':
                        model_output_fpath = run_forward_analysis(self.m_comboBox_analysis_type.GetValue(),
                                                                  self.m_filePicker_modeling_file.GetPath(),
                                                                  self.m_filePicker_model_state_q.GetPath(),
                                                                  self.m_filePicker_model_state_qp.GetPath(),
                                                                  self.m_dirPicker_force_files.GetPath(),
                                                                  self.m_dirPicker_outputs_folder.GetPath(),
                                                                  float(self.m_textCtrl_sampling_frequency.GetValue()),
                                                                  float(self.m_textCtrl_init_time.GetValue()),
                                                                  float(self.m_textCtrl_end_time.GetValue()),
                                                                  'gui',
                                                                  self.m_textCtrl_Messages)

                    elif self.m_comboBox_analysis_type.GetValue() == 'Inverse Dynamic':
                        model_output_fpath = run_inverse_analysis(self.m_comboBox_analysis_type.GetValue(),
                                                                  float(self.m_textCtrl_subject_bodymass.GetValue()),
                                                                  self.m_filePicker_modeling_file.GetPath(),
                                                                  self.m_filePicker_model_data.GetPath(),
                                                                  self.m_filePicker_model_state_q.GetPath(),
                                                                  self.m_filePicker_model_drivers_labels.GetPath(),
                                                                  self.m_dirPicker_force_files.GetPath(),
                                                                  '',
                                                                  self.m_dirPicker_outputs_folder.GetPath(),
                                                                  float(self.m_textCtrl_sampling_frequency.GetValue()),
                                                                  float(self.m_textCtrl_init_time.GetValue()),
                                                                  float(self.m_textCtrl_end_time.GetValue()),
                                                                  'gui',
                                                                  self.m_textCtrl_Messages
                                                                  )

                    elif self.m_comboBox_analysis_type.GetValue() == 'Musculoskeletal':
                        model_output_fpath = run_inverse_analysis(self.m_comboBox_analysis_type.GetValue(),
                                                                  float(self.m_textCtrl_subject_bodymass.GetValue()),
                                                                  self.m_filePicker_modeling_file.GetPath(),
                                                                  self.m_filePicker_model_data.GetPath(),
                                                                  self.m_filePicker_model_state_q.GetPath(),
                                                                  self.m_filePicker_model_drivers_labels.GetPath(),
                                                                  self.m_dirPicker_force_files.GetPath(),
                                                                  self.m_filePicker_msk_database.GetPath(),
                                                                  self.m_dirPicker_outputs_folder.GetPath(),
                                                                  float(self.m_textCtrl_sampling_frequency.GetValue()),
                                                                  float(self.m_textCtrl_init_time.GetValue()),
                                                                  float(self.m_textCtrl_end_time.GetValue()),
                                                                  'gui',
                                                                  self.m_textCtrl_Messages
                                                                  )

                    self.m_button_analysis.Enable(True)

                # four tabs here
                except Exception as e:
                    self.m_button_analysis.Enable(True)
                    self.m_textCtrl_Messages.AppendText(str(e.__class__.__name__) + " : " + str(e) + '\n')
                    pass

            # three tabs here
            except Exception as e:
                self.m_button_analysis.Enable(True)
                self.m_textCtrl_Messages.AppendText(str(e.__class__.__name__) + " : " + str(e) + '\n')
                pass

        # two tabs here
        except Exception as e:
            self.m_button_analysis.Enable(True)
            self.m_textCtrl_Messages.AppendText(str(e.__class__.__name__) + " : " + str(e) + '\n')
            pass

    def m_button_Messages_clearOnButtonClick(self, event):
        self.m_textCtrl_Messages.Clear()


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)