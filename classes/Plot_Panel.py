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
import csv
import os
from scipy import signal
import numpy as np
from collections import Counter
import os
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import time
import matplotlib as mpl
import pathlib
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mpl_toolkits.axes_grid1
import matplotlib.widgets
import os
from classes.Player import Player
matplotlib.use('TkAgg')


class Plot_Panel(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, pos=(0.125, 0.92), **kwargs)
        # self.figure     = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))
        self.figure, (self.ax1, self.ax2) = plt.subplots(2, 1)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)
        self.show_model_CoM = True
        self.show_model_refs = True
        self.show_model_markers = True
        self.show_grfs = True

        self.SetMinSize(wx.Size(250, 250))

    def draw_plots(self,
                   nRigidBodies='',
                   model_coordinates='',
                   lines_info='',
                   model_markers='',
                   grf_info='',
                   model_plot_xlim='',
                   model_plot_ylim='',
                   variable_plot_ydata='',
                   variable_plot_xdata='',
                   variable_plot_xlim='',
                   variable_plot_ylim='',
                   variable_plot_ylabel=''
                   ):

        # Clear both axes when a new variable is selected
        self.ax1.cla()
        self.ax2.cla()

        # Set variable plot 'y' label
        self.ax2.set_ylabel(variable_plot_ylabel)

        # Turn grid of variable plot visible
        self.ax2.grid(True)

        # Set model plot 'x' and 'y' limits
        self.ax1.set_xlim(model_plot_xlim)
        self.ax1.set_ylim(model_plot_ylim)

        # Set plotted variable 'x' and 'y' limits
        self.ax2.set_xlim(variable_plot_xlim)
        self.ax2.set_ylim(variable_plot_ylim)

        # Get number of frames of processed data
        variable_plot_xdata = np.arange(0, variable_plot_ydata.shape[0], 1)

        # Get the number of experimental markers
        if isinstance(model_markers, np.ndarray):
            n_markers = int(model_markers.shape[1]/2)
        else:
            n_markers = 0

        # Create the lines that represent the segments of the multibody system in the left plot
        model_segment_lines = sum(
            [self.ax1.plot([], [], '-', color='black', linewidth=1.5) for n in range(int(nRigidBodies))], [])

        # Initialize the plot of the CoM of each segment of the model
        model_CoMs = sum(
            [self.ax1.plot([], [], marker="o", color='orange', ms=15) for n in range(int(nRigidBodies))], [])

        # Initialize the vertical line that follows the plot of the selected variable
        v_line = self.ax2.axvline(0, color="cornflowerblue")

        # Initialize the plot of the selected variable
        scatter_point, = self.ax2.plot([], [], marker="o", color="crimson", ms=10)

        # Initialize the plot of 'x' axis of each segment of the model
        x_axes_lines = sum([self.ax1.plot([], [], '-', color='red', linewidth=2.5) for n in
                            range(int(nRigidBodies))], [])

        # Initialize the plot of 'z' axis of each segment of the model
        z_axes_lines = sum([self.ax1.plot([], [], '-', color='blue', linewidth=2.5) for n in
                            range(int(nRigidBodies))], [])

        # Initialize the plot of the ground reaction forces of the model
        grf_lines = sum(
                [self.ax1.plot([], [], '-', color='purple', linewidth=1.5) for n in range(len(grf_info.keys()))], [])

        # Initialize the plot of the experimental markers of the model
        model_markers_lines = sum(
            [self.ax1.plot([], [], '-', marker="x", color='black', linewidth=1.5) for n in range(n_markers)],
            [])

        # Combine all plots lines in one object
        lines = [model_segment_lines, model_CoMs, v_line, scatter_point, x_axes_lines,
                 z_axes_lines, grf_lines, model_markers_lines]

        # Plot the selected variable of the model in self.axis 2
        self.ax2.plot(variable_plot_ydata)

        # Show value of selected variable of the model in every frame of the right plot
        t1 = self.ax2.text(0, 0, '')

        def init():
            # Initialize model segments
            lines[0] = sum(
                [self.ax1.plot([], [], '-', color='black', linewidth=1.5) for n in range(int(nRigidBodies))], [])

            # Initialize model segments CoMs
            lines[1] = sum(
                [self.ax1.plot([], [], '-', marker="o", color='orange', linewidth=1.5) for n in
                 range(int(nRigidBodies))], [])

            # Initialize vertical line for xy_data
            lines[2] = self.ax2.axvline(0, color="cornflowerblue")

            # Initialize xy_data marker
            lines[3] = self.ax2.plot([], [], marker="o", color="crimson", ms=15)

            # Initialize model segments 'x' axis
            lines[4] = sum(
                [self.ax1.plot([], [], '-', color='red', linewidth=1.5) for n in range(int(nRigidBodies))], [])

            # Initialize model segments 'z' axis
            lines[5] = sum(
                [self.ax1.plot([], [], '-', color='blue', linewidth=1.5) for n in range(int(nRigidBodies))], [])

            # Initialize grf lines
            lines[6] = sum(
                [self.ax1.plot([], [], '-', color='purple', linewidth=1.5) for n in range(len(grf_info.keys()))], [])

            # Initialize model markers
            lines[7] = sum(
                [self.ax1.plot([], [], '-', marker="x", color='black', linewidth=1.5) for n in range(n_markers)],
                [])

            return lines

        def animate(i):
            # Update the position of the segments of the model
            for _ in range(0, int(nRigidBodies)):
                xs = [lines_info[_ + 1][i]['joint_1'][0], lines_info[_ + 1][i]['joint_2'][0]]
                ys = [lines_info[_ + 1][i]['joint_1'][1], lines_info[_ + 1][i]['joint_2'][1]]
                lines[0][_].set_data(xs, ys)

            # Update and show / hide the CoM of each segment of the model
            if self.show_model_CoM:
                for _ in range(0, int(nRigidBodies)):
                    x = model_coordinates[i, 4 * (_ - 1)]
                    y = model_coordinates[i, 4 * (_ - 1) + 1]
                    lines[1][_].set_data(x, y)
                    lines[1][_].set_visible(True)
            elif self.show_model_CoM:
                for _ in range(0, int(nRigidBodies)):
                    lines[1][_].set_visible(False)

            # Update position of the vertical line that follows the value of the plotted variable of the model
            lines[2].set_xdata([i])

            # Update position of the point representing the value of the plotted variable of the model
            lines[3][0].set_data(variable_plot_xdata[i], variable_plot_ydata[i])

            if self.show_model_refs:
                for _ in range(0, int(nRigidBodies)):
                    dx = model_coordinates[i, 4 * _ + 2] * 0.1
                    dy = model_coordinates[i, 4 * _ + 3] * 0.1
                    xs = [model_coordinates[i, _ * 4], model_coordinates[i, _ * 4] + dx]
                    ys = [model_coordinates[i, _ * 4 + 1], model_coordinates[i, _ * 4 + 1] + dy]

                    xs_perp = [model_coordinates[i, _ * 4], model_coordinates[i, _ * 4] - dy]
                    ys_perp = [model_coordinates[i, _ * 4 + 1], model_coordinates[i, _ * 4 + 1] + dx]
                    lines[4][_].set_data(xs, ys)
                    lines[5][_].set_data(xs_perp, ys_perp)
                    lines[4][_].set_visible(True)
                    lines[5][_].set_visible(True)

            elif not self.show_model_refs:
                for _ in range(0, int(nRigidBodies)):
                    lines[4][_].set_visible(False)
                    lines[5][_].set_visible(False)

            # Update values of the grf lines
            if not bool(grf_info):
                if self.show_grfs:
                    for _ in range(0, int(len(grf_info.keys()))):
                        lines[6][_].set_data([grf_info[_]['CoP_X'][i], grf_info[_]['CoP_X'][i] + grf_info[_]['Fx'][i]],
                                             [0, grf_info[_]['Fz'][i]])
                        lines[6][_].set_visible(True)
                elif not self.show_grfs:
                    for _ in range(0, int(len(grf_info.keys()))):
                        lines[6][_].set_visible(False)

            # Update values of experimental markers of the model
            if self.show_model_markers:
                for _ in range(0, n_markers):
                    xs = model_markers[i, (_ * 2)]
                    ys = model_markers[i, (_ * 2) + 1]
                    lines[7][_].set_data(xs, ys)
                    lines[7][_].set_visible(True)
            elif not self.show_model_markers:
                for _ in range(0, n_markers):
                    lines[7][_].set_visible(False)

            # Update position of the value of the plotted variable of the model
            t1.set_position((float(variable_plot_xdata[i]), float(variable_plot_ydata[i]) * 1.05))
            t1.set_text(str(np.round(variable_plot_ydata[i], 3)))

            return lines

        def on_press(event):
            if event.key.isspace():
                if anim.runs:
                    anim.runs = False
                else:
                    anim.runs = True

        self.figure.canvas.mpl_connect('key_press_event', on_press)
        anim = Player(self.figure, func=animate, frames=int(variable_plot_xdata.shape[0] - 1),
                      maxi=int(variable_plot_xdata.shape[0] - 1), init_func=init)

        self.figure.canvas.draw()


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
