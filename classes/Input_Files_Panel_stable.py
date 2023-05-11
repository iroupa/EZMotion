# -*- coding: utf-8 -*-

import wx
import wx.xrc
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons
import csv
import os
from scipy import signal
import numpy as np
from collections import Counter
import os
import time
import numpy as np
from scipy.integrate import odeint
from assemble_C_matrix import assemble_C_matrix
from classes.Player import Player
from initialize_analysis_variables import initialize_analysis_variables
from file2dataConst import file2dataConst
from set_sbSizer_foreground_color import set_sbSizer_foregroundcolour
from set_staticText_foreground_color import set_staticText_foregroundcolour
from initialize_report_variables import initialize_report_variables
from read_inertial_parameters import read_inertial_parameters
from check_smaller import check_smaller_equal
from count_model_DoF import count_model_DoF
from read_model_input_data import read_model_input_data
from read_DoF_labels import read_DoF_labels
from raw2selectedData import raw2selectedData
from compute_spline_coords import compute_spline_coords
from read_force_file_info import read_force_file_info
from compute_splined_forces import compute_splined_forces
from assemble_mass_matrix import assemble_mass_matrix
from assemble_gravitational_forces import assemble_gravitational_forces
from update_G_vector import update_G_vector
from interpolate_series import interpolate_1D_data
from read_model_loc_coords import read_model_loc_coords
from read_model_outputs import read_model_outputs
from read_gui_settings import read_gui_settings
from compute_lines_info import compute_lines_info
from classes.TextValidator import TextObjectValidator
from classes.DirValidator import DirObjectValidator
from matplotlib.animation import FuncAnimation
from filter_signal import butter_filter
from compute_axis_limits import compute_axis_limits
class Input_Files_Panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(250, 250),
                          style=wx.TAB_TRAVERSAL)

        self.SetMinSize(wx.Size(250, 250))

        bSizer_root = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow.SetScrollRate(5, 5)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_1 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_1.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_1 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_1.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_1.SetMaxSize(wx.Size(-1, 15))

        bSizer1_1.Add(self.m_panel_dummy_1_1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_1, 0, wx.EXPAND, 5)

        bSizer1_2 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_2_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Input Files Folder"),
                                         wx.VERTICAL)

        bSizer1_2_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_inputs_file_folder = wx.StaticText(sbSizer1_2_1.GetStaticBox(), wx.ID_ANY, u"Input Files Folder",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_inputs_file_folder.Wrap(-1)
        self.m_static_inputs_file_folder.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_inputs_file_folder.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_inputs_file_folder.SetMinSize(wx.Size(150, -1))

        bSizer1_2_1_1.Add(self.m_static_inputs_file_folder, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dirPicker_input_files_folder = wx.DirPickerCtrl(sbSizer1_2_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                               u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                               wx.DIRP_DEFAULT_STYLE, validator = DirObjectValidator('dir'))
        bSizer1_2_1_1.Add(self.m_dirPicker_input_files_folder, 1, wx.ALL, 5)

        sbSizer1_2_1.Add(bSizer1_2_1_1, 0, wx.EXPAND, 15)

        bSizer1_2.Add(sbSizer1_2_1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer1_2, 0, wx.EXPAND, 5)

        bSizer1_3 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_3.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_3 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_3.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_3.SetMaxSize(wx.Size(-1, 15))

        bSizer1_3.Add(self.m_panel_dummy_1_3, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_3, 0, wx.EXPAND, 5)

        bSizer1_4 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_4_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Input Files"), wx.VERTICAL)

        bSizer1_4_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_modeling_file = wx.StaticText(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, u"Model File",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_modeling_file.Wrap(-1)
        self.m_static_modeling_file.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        self.m_static_modeling_file.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
        self.m_static_modeling_file.SetMinSize(wx.Size(150, -1))

        bSizer1_4_1_1.Add(self.m_static_modeling_file, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_filePicker_modeling_file = wx.FilePickerCtrl(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                            u"Select a file", u"*.*", wx.DefaultPosition,
                                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator = DirObjectValidator('file'))
        bSizer1_4_1_1.Add(self.m_filePicker_modeling_file, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer1_4_1.Add(bSizer1_4_1_1, 0, wx.EXPAND | wx.TOP, 15)

        bSizer1_4_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_outputs = wx.StaticText(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, u"Model Outputs",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_outputs.Wrap(-1)
        self.m_static_model_outputs.SetMinSize(wx.Size(150, -1))
        self.m_static_model_outputs.SetMaxSize(wx.Size(150, -1))

        bSizer1_4_1_2.Add(self.m_static_model_outputs, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_filePicker_model_outputs = wx.FilePickerCtrl(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                            u"Select a file", u"*.*", wx.DefaultPosition,
                                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator = DirObjectValidator('file'))
        bSizer1_4_1_2.Add(self.m_filePicker_model_outputs, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_4_1.Add(bSizer1_4_1_2, 0, wx.EXPAND, 5)

        bSizer1_4_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_markers = wx.StaticText(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, u"Markers File",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_markers.Wrap(-1)
        self.m_static_model_markers.SetMinSize(wx.Size(150, -1))
        self.m_static_model_markers.SetMaxSize(wx.Size(150, -1))

        bSizer1_4_1_3.Add(self.m_static_model_markers, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_filePicker_model_markers = wx.FilePickerCtrl(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                            u"Select a file", u"*.*", wx.DefaultPosition,
                                                            wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator = DirObjectValidator('file'))
        bSizer1_4_1_3.Add(self.m_filePicker_model_markers, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_4_1.Add(bSizer1_4_1_3, 0, wx.EXPAND, 5)

        bSizer1_4_1_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_model_loc_coords = wx.StaticText(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, u"Segments Local Coordinates",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_model_loc_coords.Wrap(-1)
        self.m_static_model_loc_coords.SetMinSize(wx.Size(150, -1))
        self.m_static_model_loc_coords.SetMaxSize(wx.Size(150, -1))

        bSizer1_4_1_4.Add(self.m_static_model_loc_coords, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_filePicker_model_loc_coords = wx.FilePickerCtrl(sbSizer1_4_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                               u"Select a file", u"*.*", wx.DefaultPosition,
                                                               wx.DefaultSize, wx.FLP_DEFAULT_STYLE, validator = DirObjectValidator('file'))
        bSizer1_4_1_4.Add(self.m_filePicker_model_loc_coords, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_4_1.Add(bSizer1_4_1_4, 0, wx.EXPAND, 5)

        bSizer1_4.Add(sbSizer1_4_1, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        bSizer1.Add(bSizer1_4, 0, wx.EXPAND, 5)

        bSizer1_5 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_5.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_5 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_5.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_5.SetMaxSize(wx.Size(-1, 15))

        bSizer1_5.Add(self.m_panel_dummy_1_5, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_5, 0, wx.EXPAND, 5)

        bSizer1_6 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_6_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Plot Data"), wx.VERTICAL)

        bSizer1_6_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_plot_variable = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Variable",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_plot_variable.Wrap(-1)
        self.m_static_plot_variable.SetMinSize(wx.Size(150, -1))
        self.m_static_plot_variable.SetMaxSize(wx.Size(150, -1))

        bSizer1_6_1_1.Add(self.m_static_plot_variable, 0, wx.ALL | wx.EXPAND, 5)

        m_comboBox_plot_dataChoices = [u"--"]
        self.m_comboBox_plot_data = wx.ComboBox(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Angle", wx.DefaultPosition,
                                                wx.DefaultSize, m_comboBox_plot_dataChoices, 0)
        self.m_comboBox_plot_data.SetSelection(0)
        self.m_comboBox_plot_data.SetMinSize(wx.Size(200, -1))
        self.m_comboBox_plot_data.SetMaxSize(wx.Size(200, -1))

        bSizer1_6_1_1.Add(self.m_comboBox_plot_data, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_6_1.Add(bSizer1_6_1_1, 0, wx.TOP, 15)

        bSizer1_6_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_plot_filter_choice = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Filter Data",
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_plot_filter_choice.Wrap(-1)
        self.m_static_plot_filter_choice.SetMinSize(wx.Size(150, -1))
        self.m_static_plot_filter_choice.SetMaxSize(wx.Size(150, -1))

        bSizer1_6_1_2.Add(self.m_static_plot_filter_choice, 0, wx.ALL | wx.EXPAND, 5)

        m_comboBox_plot_filter_choiceChoices = [u"No", u"Yes"]
        self.m_comboBox_plot_filter_choice = wx.ComboBox(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"No",
                                                         wx.DefaultPosition, wx.DefaultSize,
                                                         m_comboBox_plot_filter_choiceChoices, 0)
        self.m_comboBox_plot_filter_choice.SetSelection(0)
        self.m_comboBox_plot_filter_choice.SetMinSize(wx.Size(200, -1))
        self.m_comboBox_plot_filter_choice.SetMaxSize(wx.Size(200, -1))

        bSizer1_6_1_2.Add(self.m_comboBox_plot_filter_choice, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_6_1.Add(bSizer1_6_1_2, 0, 0, 5)

        bSizer1_6_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_plot_filter_freq = wx.StaticText(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, u"Filter Frequency (Hz)",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_plot_filter_freq.Wrap(-1)
        self.m_static_plot_filter_freq.SetMinSize(wx.Size(150, -1))
        self.m_static_plot_filter_freq.SetMaxSize(wx.Size(150, -1))

        bSizer1_6_1_3.Add(self.m_static_plot_filter_freq, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_plot_filter_freq = wx.TextCtrl(sbSizer1_6_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.Size(200, -1), wx.TE_RIGHT)
        self.m_textCtrl_plot_filter_freq.SetMinSize(wx.Size(200, -1))
        self.m_textCtrl_plot_filter_freq.SetMaxSize(wx.Size(200, -1))

        bSizer1_6_1_3.Add(self.m_textCtrl_plot_filter_freq, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_6_1.Add(bSizer1_6_1_3, 0, 0, 5)

        bSizer1_6.Add(sbSizer1_6_1, 0, wx.EXPAND | wx.RIGHT | wx.LEFT, 5)

        bSizer1.Add(bSizer1_6, 0, wx.EXPAND, 5)

        bSizer1_7 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_7.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_7 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_7.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_7.SetMaxSize(wx.Size(-1, 15))

        bSizer1_7.Add(self.m_panel_dummy_1_7, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_7, 0, wx.EXPAND, 5)

        bSizer1_8 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_show_model = wx.Button(self.m_scrolledWindow, wx.ID_ANY, u"Show Model", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_button_show_model.SetMinSize(wx.Size(-1, 50))
        self.m_button_show_model.SetMaxSize(wx.Size(-1, 50))

        bSizer1_8.Add(self.m_button_show_model, 1, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_8, 0, wx.EXPAND, 5)

        bSizer1_9 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_9.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_9 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_9.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_9.SetMaxSize(wx.Size(-1, 15))

        bSizer1_9.Add(self.m_panel_dummy_1_9, 1, wx.EXPAND | wx.ALL, 5)

        bSizer1.Add(bSizer1_9, 0, wx.EXPAND, 5)

        bSizer1_10 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_10_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Outputs"), wx.VERTICAL)

        bSizer1_10_1_1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_export_outputs = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Export Outputs",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_export_outputs.Wrap(-1)
        self.m_static_export_outputs.SetMinSize(wx.Size(100, -1))

        bSizer1_10_1_1.Add(self.m_static_export_outputs, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_comboBox_export_outputsChoices = [u"No", u"Yes"]
        self.m_comboBox_export_outputs = wx.ComboBox(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Yes",
                                                     wx.DefaultPosition, wx.DefaultSize,
                                                     m_comboBox_export_outputsChoices, 0)
        self.m_comboBox_export_outputs.SetSelection(0)
        self.m_comboBox_export_outputs.SetMinSize(wx.Size(150, -1))
        self.m_comboBox_export_outputs.SetMaxSize(wx.Size(150, -1))

        bSizer1_10_1_1.Add(self.m_comboBox_export_outputs, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_10_1.Add(bSizer1_10_1_1, 1, wx.TOP | wx.EXPAND, 15)

        bSizer1_10_1_2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_export_outputs_init_frame = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY,
                                                                u"Initial Frame", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_export_outputs_init_frame.Wrap(-1)
        self.m_static_export_outputs_init_frame.SetMinSize(wx.Size(100, -1))

        bSizer1_10_1_2.Add(self.m_static_export_outputs_init_frame, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_spinCtrl_export_outputs_init_frame = wx.SpinCtrl(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                                wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0,
                                                                10000, 0)
        bSizer1_10_1_2.Add(self.m_spinCtrl_export_outputs_init_frame, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_static_export_outputs_end_frame = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"End Frame",
                                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_export_outputs_end_frame.Wrap(-1)
        self.m_static_export_outputs_end_frame.SetMinSize(wx.Size(100, -1))

        bSizer1_10_1_2.Add(self.m_static_export_outputs_end_frame, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_spinCtrl_export_outputs_end_frame = wx.SpinCtrl(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                                wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0,
                                                                10000, 0)
        bSizer1_10_1_2.Add(self.m_spinCtrl_export_outputs_end_frame, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_10_1.Add(bSizer1_10_1_2, 1, wx.EXPAND, 5)

        bSizer1_10_1_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_export_outputs_normalized = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Normalized",
                                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_export_outputs_normalized.Wrap(-1)
        self.m_static_export_outputs_normalized.SetMinSize(wx.Size(100, -1))

        bSizer1_10_1_3.Add(self.m_static_export_outputs_normalized, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_checkBox_normalized_yes = wx.CheckBox(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Yes",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1_10_1_3.Add(self.m_checkBox_normalized_yes, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_checkBox_normalized_no = wx.CheckBox(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"No", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        bSizer1_10_1_3.Add(self.m_checkBox_normalized_no, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        sbSizer1_10_1.Add(bSizer1_10_1_3, 1, wx.EXPAND, 5)

        bSizer1_10_1_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_static_outputs_folder = wx.StaticText(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Outputs Folder",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_static_outputs_folder.Wrap(-1)
        self.m_static_outputs_folder.SetMinSize(wx.Size(100, -1))

        bSizer1_10_1_4.Add(self.m_static_outputs_folder, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_dirPicker_outputs_folder = wx.DirPickerCtrl(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                                           u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
                                                           wx.DIRP_DEFAULT_STYLE, validator = DirObjectValidator('dir'))
        bSizer1_10_1_4.Add(self.m_dirPicker_outputs_folder, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer1_10_1.Add(bSizer1_10_1_4, 1, wx.EXPAND, 5)

        bSizer1_10_1_5 = wx.BoxSizer(wx.VERTICAL)

        self.m_button_export_outputs = wx.Button(sbSizer1_10_1.GetStaticBox(), wx.ID_ANY, u"Export Outputs",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button_export_outputs.SetMinSize(wx.Size(-1, 50))
        self.m_button_export_outputs.SetMaxSize(wx.Size(-1, 50))

        bSizer1_10_1_5.Add(self.m_button_export_outputs, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer1_10_1.Add(bSizer1_10_1_5, 1, wx.EXPAND, 5)

        bSizer1_10.Add(sbSizer1_10_1, 0, wx.EXPAND, 5)

        bSizer1.Add(bSizer1_10, 1, wx.EXPAND, 5)

        bSizer1_11 = wx.BoxSizer(wx.VERTICAL)

        bSizer1_11.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_11 = wx.Panel(self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL)
        self.m_panel_dummy_1_11.SetMinSize(wx.Size(-1, 15))
        self.m_panel_dummy_1_11.SetMaxSize(wx.Size(-1, 15))

        bSizer1_11.Add(self.m_panel_dummy_1_11, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer1_11, 0, wx.EXPAND, 5)

        bSizer1_12 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1_12_1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindow, wx.ID_ANY, u"Messages"), wx.VERTICAL)

        self.m_textCtrl_Messages = wx.TextCtrl(sbSizer1_12_1.GetStaticBox(), wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        self.m_textCtrl_Messages.SetMinSize(wx.Size(-1, 150))
        self.m_textCtrl_Messages.SetMaxSize(wx.Size(-1, 150))

        sbSizer1_12_1.Add(self.m_textCtrl_Messages, 1, wx.ALL | wx.EXPAND, 5)

        self.m_button_Messages_clear = wx.Button(sbSizer1_12_1.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        sbSizer1_12_1.Add(self.m_button_Messages_clear, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer1_12.Add(sbSizer1_12_1, 0, wx.EXPAND, 5)

        bSizer1.Add(bSizer1_12, 0, wx.EXPAND, 5)

        self.m_scrolledWindow.SetSizer(bSizer1)
        self.m_scrolledWindow.Layout()
        bSizer1.Fit(self.m_scrolledWindow)
        bSizer_root.Add(self.m_scrolledWindow, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer_root)
        self.Layout()

        gui_settings = read_gui_settings(r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\preferences\preferences.txt')

        self.SetBackgroundColour(gui_settings['panel_backgroundcolour'])

        # Set sbSizers Input Files labels foreground color and font type
        sbSizers_list = [sbSizer1_2_1,
                         sbSizer1_4_1,
                         sbSizer1_6_1,
                         sbSizer1_10_1,
                         sbSizer1_12_1]

        for _ in sbSizers_list:
            set_sbSizer_foregroundcolour(_,
                                         gui_settings['sbSizers_labels_color'],
                                         gui_settings['sbSizers_labels_font_size'],
                                         gui_settings['sbSizers_labels_font_family'],
                                         gui_settings['sbSizers_labels_font_style'],
                                         gui_settings['sbSizers_labels_font_type'])

        # Set static labels preferences
        staticText_list = [self.m_static_inputs_file_folder,
                           self.m_static_modeling_file,
                           self.m_static_model_outputs,
                           self.m_static_model_markers,
                           self.m_static_model_loc_coords,
                           self.m_static_outputs_folder,
                           self.m_static_plot_variable,
                           self.m_static_plot_filter_choice,
                           self.m_static_plot_filter_freq,
                           self.m_static_outputs_folder,
                           self.m_static_export_outputs,
                           self.m_static_export_outputs_init_frame,
                           self.m_static_export_outputs_end_frame,
                           self.m_static_export_outputs_normalized,
                           self.m_checkBox_normalized_yes,
                           self.m_checkBox_normalized_no,
                           ]

        for _ in staticText_list:
            set_staticText_foregroundcolour(_,
                                            gui_settings['static_labels_color'],
                                            gui_settings['static_labels_font_size'],
                                            gui_settings['static_labels_font_family'],
                                            gui_settings['static_labels_font_style'],
                                            gui_settings['static_labels_font_type'],
                                            )

        self.m_button_show_model.SetFont(wx.Font(gui_settings['button_font_size'],
                                                 gui_settings['sbSizers_labels_font_family'],
                                                 gui_settings['sbSizers_labels_font_style'],
                                                 gui_settings['sbSizers_labels_font_type'],
                                                 False,
                                                 wx.EmptyString))

        self.m_button_export_outputs.SetFont(wx.Font(gui_settings['button_font_size'],
                                                     gui_settings['sbSizers_labels_font_family'],
                                                     gui_settings['sbSizers_labels_font_style'],
                                                     gui_settings['sbSizers_labels_font_type'],
                                                     False,
                                                     wx.EmptyString))


        # # # Hide Data Filter Frequency
        self.m_static_plot_filter_freq.Hide()
        self.m_textCtrl_plot_filter_freq.Hide()
        self.m_static_export_outputs_init_frame.Hide()
        self.m_static_export_outputs_end_frame.Hide()
        self.m_static_export_outputs_normalized.Hide()
        self.m_checkBox_normalized_yes.Hide()
        self.m_checkBox_normalized_no.Hide()
        self.m_spinCtrl_export_outputs_init_frame.Hide()
        self.m_spinCtrl_export_outputs_end_frame.Hide()
        self.m_static_outputs_folder.Hide()
        self.m_dirPicker_outputs_folder.Hide()
        self.m_button_export_outputs.Hide()

        # self.SetSizer(bSizer_root)
        # self.Layout()

        # Connect Events
        self.m_dirPicker_input_files_folder.Bind(wx.EVT_DIRPICKER_CHANGED,
                                                 self.m_dirPicker_input_files_folderOnDirChanged)
        self.m_filePicker_modeling_file.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_modeling_fileOnFileChanged)
        self.m_filePicker_model_outputs.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_model_outputsOnFileChanged)
        self.m_filePicker_model_markers.Bind(wx.EVT_FILEPICKER_CHANGED, self.m_filePicker_model_markersOnFileChanged)
        self.m_filePicker_model_loc_coords.Bind(wx.EVT_FILEPICKER_CHANGED,
                                                self.m_filePicker_model_loc_coordsOnFileChanged)
        self.m_comboBox_plot_data.Bind(wx.EVT_COMBOBOX, self.m_comboBox_plot_dataOnCombobox)
        self.m_comboBox_plot_filter_choice.Bind(wx.EVT_COMBOBOX, self.m_comboBox_plot_dataOnCombobox)
        self.m_button_show_model.Bind(wx.EVT_BUTTON, self.m_button_show_modelOnButtonClick)
        self.m_comboBox_export_outputs.Bind(wx.EVT_COMBOBOX, self.m_comboBox_plot_parametersOnCombobox)
        self.m_button_export_outputs.Bind(wx.EVT_BUTTON, self.m_button_export_outputsOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_dirPicker_input_files_folderOnDirChanged(self, event):
            input_files_folder_fpath = self.m_dirPicker_input_files_folder.GetPath()

        # try:
            self.m_filePicker_modeling_file.SetPath(
                [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                 x.endswith('.mod')][0])

            self.m_filePicker_model_outputs.SetPath(
                [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                 x.endswith('.out')][0])

            self.m_filePicker_model_markers.SetPath(
                [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                 x.endswith('.mkr')][0])

            self.m_filePicker_model_loc_coords.SetPath(
                [os.path.join(input_files_folder_fpath, x) for x in os.listdir(input_files_folder_fpath) if
                 x.endswith('.jt')][0])

            self.m_dirPicker_outputs_folder.SetPath(input_files_folder_fpath)

            model_file_fpath = self.m_filePicker_model_outputs.GetPath()

            nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables, model_plot_variables_labels = read_model_outputs(
                model_file_fpath)

            self.m_spinCtrl_export_outputs_end_frame.SetValue(nFrames)

        # except Exception as e:
        #     self.m_textCtrl_Messages.AppendText(str(e) + '\n')
        #     pass

        # try:
            self.m_comboBox_plot_data.Clear()

            model_file_fpath = self.m_filePicker_model_outputs.GetPath()

            nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables, model_plot_variables_labels = read_model_outputs(
                model_file_fpath)
            self.m_comboBox_plot_data.Clear()
            self.m_comboBox_plot_data.Append(model_plot_variables_labels)
            self.m_comboBox_plot_data.SetSelection(1)

        # except Exception as e:
        #     self.m_textCtrl_Messages.AppendText(str(e) + '\n')
        #     pass

    def m_filePicker_modeling_fileOnFileChanged(self, event):
        try:
            fpath = self.m_filePicker_modeling_file.GetPath()
            self.m_dirPicker_outputs_folder.SetPath(os.path.join(os.path.split(fpath)[0]))

        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

    def m_filePicker_model_outputsOnFileChanged(self, event):
        # two tabs
        try:
            self.m_comboBox_plot_data.Clear()

            model_file_fpath = self.m_filePicker_model_outputs.GetPath()

            nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables, model_plot_variables_labels = read_model_outputs(
                model_file_fpath)
            self.m_comboBox_plot_data.Clear()
            self.m_comboBox_plot_data.Append(model_plot_variables_labels)
            self.m_comboBox_plot_data.SetSelection(1)

            self.m_spinCtrl_export_outputs_end_frame.SetValue(nFrames)

        # two tabs
        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

    def m_filePicker_model_markersOnFileChanged(self, event):
        event.Skip()

    def m_filePicker_model_loc_coordsOnFileChanged(self, event):
        event.Skip()

    def m_comboBox_plot_dataOnCombobox(self, event):
        if self.m_comboBox_plot_filter_choice.GetStringSelection() == 'No':
            self.m_static_plot_filter_freq.Hide()
            self.m_textCtrl_plot_filter_freq.Hide()
            self.Layout()
        elif self.m_comboBox_plot_filter_choice.GetStringSelection() == 'Yes':
            self.m_static_plot_filter_freq.Show()
            self.m_textCtrl_plot_filter_freq.Show()
            self.Layout()

    def m_button_show_modelOnButtonClick(self, event):
        # two tabs here
        try:
            input_files_ctrls_list = [
                                      # self.m_dirPicker_input_files_folder,
                                      self.m_filePicker_modeling_file,
                                      self.m_filePicker_model_outputs,
                                      # self.m_filePicker_model_markers,
                                      self.m_filePicker_model_loc_coords,
                                      # self.m_dirPicker_outputs_folder,
                                      ]

            for ctrl in input_files_ctrls_list:
                ctrl.GetValidator().Validate(ctrl)

            model_file_fpath = self.m_filePicker_model_outputs.GetPath()

            nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables, model_plot_variables_labels = read_model_outputs(
                model_file_fpath)

            model_loc_coords_fpath = self.m_filePicker_model_loc_coords.GetPath()

            lines_info = compute_lines_info(model_loc_coords_fpath, model_coordinates_data)

            # Label of the variable of the model to plot in axis 2
            ax2_variable_label = self.m_comboBox_plot_data.GetStringSelection()

            # Filter raw data of the selected variable of the model
            if self.m_comboBox_plot_filter_choice.GetValue() == 'Yes':
                ax2_ydata = butter_filter(model_plot_variables[ax2_variable_label][:-1],
                                  int(sampling_frequency),
                                  float(self.m_textCtrl_plot_filter_freq.GetValue()),
                                  4)
            else:
                ax2_ydata = model_plot_variables[ax2_variable_label][:-1]

            # Number of frames of plot_variable_data
            ax2_xdata = np.arange(0, ax2_ydata.shape[0], 1)

            # Max and min of 'x' and 'y' cartesian coordinates of the model
            ax1_xlim, ax1_ylim = compute_axis_limits(model_coordinates_data, nRigidBodies, 'both')
            ax2_xlim, ax2_ylim = compute_axis_limits(model_plot_variables[ax2_variable_label], nRigidBodies, 'y')

            self.GrandParent.m_plot_panel.draw_plots(nRigidBodies = nRigidBodies,
                                                     model_coordinates = model_coordinates_data,
                                                     lines_info=lines_info,
                                                     axis1_xlim=ax1_xlim,
                                                     axis1_ylim=ax1_ylim,
                                                     axis2_xdata = ax2_xdata,
                                                     axis2_ydata = ax2_ydata,
                                                     axis2_xlim=ax2_xlim,
                                                     axis2_ylim=ax2_ylim
                                                     )

        # two tabs here
        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

    def m_comboBox_plot_parametersOnCombobox(self, event):
        try:
            if self.m_comboBox_export_outputs.GetValue() == 'Yes':
                self.m_static_export_outputs_init_frame.Show()
                self.m_static_export_outputs_end_frame.Show()
                self.m_static_export_outputs_normalized.Show()
                self.m_checkBox_normalized_yes.Show()
                self.m_spinCtrl_export_outputs_init_frame.Show()
                self.m_spinCtrl_export_outputs_end_frame.Show()
                self.m_static_outputs_folder.Show()
                self.m_dirPicker_outputs_folder.Show()
                self.m_button_export_outputs.Show()
                self.Layout()
            elif self.m_comboBox_export_outputs.GetValue() == 'No':
                self.m_static_export_outputs_init_frame.Hide()
                self.m_static_export_outputs_end_frame.Hide()
                self.m_static_export_outputs_normalized.Hide()
                self.m_checkBox_normalized_yes.Hide()
                self.m_spinCtrl_export_outputs_init_frame.Hide()
                self.m_spinCtrl_export_outputs_end_frame.Hide()
                self.m_static_outputs_folder.Hide()
                self.m_dirPicker_outputs_folder.Hide()
                self.m_button_export_outputs.Hide()
                self.Layout()
        except Exception as e:
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

    def m_button_export_outputsOnButtonClick(self, event):
        try:
            if self.m_comboBox_export_outputs.GetValue() == 'Yes':

                model_file_fpath = self.m_filePicker_model_outputs.GetPath()

                nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables, model_plot_variables_labels = read_model_outputs(
                    model_file_fpath)

                # init_frame = self.m_spinCtrl_export_outputs_init_frame.GetValue()
                #
                # end_frame = self.m_spinCtrl_export_outputs_end_frame.GetValue()

                check_smaller_equal(self.m_spinCtrl_export_outputs_init_frame, self.m_spinCtrl_export_outputs_end_frame)
                # check_equal(self.m_spinCtrl_export_outputs_init_frame, self.m_spinCtrl_export_outputs_end_frame)

                # data = model_plot_variables[self.m_comboBox_plot_data.GetStringSelection()][init_frame:end_frame]

                # start_time = init_frame / sampling_frequency
                #
                # end_time = end_frame / sampling_frequency
                #
                # time = np.arange(start_time, end_time, 1 / sampling_frequency)

                #
                # if self.m_checkBox_normalized_yes.GetValue() == True:
                #     interp_data = interpolate_1D_data(data, 101)
                #     time = np.arange(0, 101, 1)
                #     np.savetxt(os.path.join(self.m_dirPicker_outputs_folder.GetPath(),self.m_comboBox_plot_data.GetStringSelection() + '_interp.csv'),
                #                np.vstack((time, interp_data)).T,
                #                delimiter=",")
                #     wx.MessageBox(
                #         self.m_comboBox_plot_data.GetStringSelection() + '_interp.csv file exported successfully.',
                #         'Info',
                #         wx.OK)
                #     self.m_textCtrl_Messages.AppendText(
                #         self.m_comboBox_plot_data.GetStringSelection() + '_interp.csv file exported successfully to '
                #         + self.m_dirPicker_outputs_folder.GetPath() + ' folder.\n')
                # else:
                #
                #     np.savetxt(os.path.join(self.m_dirPicker_outputs_folder.GetPath(),self.m_comboBox_plot_data.GetStringSelection() + '.csv'),
                #                np.vstack((time, data)).T,
                #                delimiter=",")
                #     wx.MessageBox(self.m_comboBox_plot_data.GetStringSelection() + '.csv file exported successfully.',
                #                   'Info',
                #                   wx.OK)
                #     self.m_textCtrl_Messages.AppendText(self.m_comboBox_plot_data.GetStringSelection() + '_interp.csv file exported successfully to '
                #                                         + self.m_dirPicker_outputs_folder.GetPath() + ' folder. \n')

        except Exception as e:
            wx.MessageBox(self.m_comboBox_plot_data.GetStringSelection() + '_interp.csv file not exported successfully.',
                          'Error',
                          wx.ICON_HAND)
            self.m_textCtrl_Messages.AppendText(str(e) + '\n')
            pass

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)