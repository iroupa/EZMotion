# -*- coding: utf-8 -*-

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
import numpy as np
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
        self.canvas     = FigureCanvas(self, -1, self.figure)
        self.toolbar    = NavigationToolbar(self.canvas)
        self.toolbar.Realize()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)
        self.show_model_CoM = True
        self.show_model_refs = True
        self.SetMinSize(wx.Size(250, 250))

    def draw_plots(self,
                   nRigidBodies = '',
                   model_coordinates='',
                   lines_info='',
                   axis1_xlim = '',
                   axis1_ylim = '',
                   axis2_ydata = '',
                   axis2_xdata = '',
                   axis2_xlim='',
                   axis2_ylim='',
                   ):

        # Clear both axes when a new variable is selected
        self.ax1.cla()
        self.ax2.cla()

        # Turn grid of variable plot visible
        self.ax2.grid(True)

        # Set model plot 'x' and 'y' limits
        self.ax1.set_xlim(axis1_xlim)
        self.ax1.set_ylim(axis1_ylim)

        # Set plotted variable 'x' and 'y' limits
        self.ax2.set_xlim(axis2_xlim)
        self.ax2.set_ylim(axis2_ylim)

        # Get number of frames of processed data
        axis2_xdata = np.arange(0, axis2_ydata.shape[0], 1)

        # Create the lines that represent the segments of the multibody system in the left plot
        model_lines = sum(
            [self.ax1.plot([], [], '-', color='black', linewidth=1.5) for n in range(int(nRigidBodies))], [])

        # Initialize the plot of the CoM of each segment of the model
        model_CoMs = sum(
            [self.ax1.plot([], [], marker="o", color='orange', ms=15) for n in range(int(nRigidBodies))], [])

        # Initialize the vertical line that follows the plot of the selected variable
        v_line = self.ax2.axvline(0, color="cornflowerblue")

        # Initialize the plot of the selected variable
        scatter_point, = self.ax2.plot([], [], marker="o", color="crimson", ms=10)

        x_axes_lines = sum([self.ax1.plot([], [], '-', color='red', linewidth=2.5) for n in range(int(nRigidBodies))], [])

        z_axes_lines = sum([self.ax1.plot([], [], '-', color='blue', linewidth=2.5) for n in range(int(nRigidBodies))], [])

        # Combine all plots lines in one object
        lines = [model_lines, model_CoMs, v_line, scatter_point, x_axes_lines, z_axes_lines]

        # Plot the selected variable of the model in self.axis 2
        self.ax2.plot(axis2_ydata)

        # Show value of selected variable of the model in every frame of the right plot
        t1 = self.ax2.text(0, 0, '')

        def init():
            # Model segments
            lines[0]  = sum(
                [self.ax1.plot([], [], '-', color='black', linewidth=1.5) for n in range(int(nRigidBodies))], [])
            # Model segments CoMs
            lines[1] = sum(
                [self.ax1.plot([], [], '-', marker="o", color='orange', linewidth=1.5) for n in range(int(nRigidBodies))], [])
            # v_line for xy_data
            lines[2]  = self.ax2.axvline(0, color="cornflowerblue")
            # xy_data marker
            lines[3]  = self.ax2.plot([], [], marker="o", color="crimson", ms=15)
            # Model segments 'x' axis
            lines[4] = sum(
                [self.ax1.plot([], [], '-', color='red', linewidth=1.5) for n in range(int(nRigidBodies))], [])
            # Model segments 'z' axis
            lines[5] = sum(
                [self.ax1.plot([], [], '-', color='blue', linewidth=1.5) for n in range(int(nRigidBodies))], [])

            return lines

        def animate(i):
            # Update the position of the segments of the model
            for _ in range(0, int(nRigidBodies)):
                xs = [lines_info[_ + 1][i]['joint_1'][0], lines_info[_ + 1][i]['joint_2'][0]]
                ys = [lines_info[_ + 1][i]['joint_1'][1], lines_info[_ + 1][i]['joint_2'][1]]
                lines[0][_].set_data(xs, ys)

            # Update and show / hide the CoM of each segment of the model
            if self.show_model_CoM == True:
                for _ in range(0, int(nRigidBodies)):
                    x = model_coordinates[i, 4 * (_ - 1)]
                    y = model_coordinates[i, 4 * (_ - 1) + 1]
                    lines[1][_].set_data(x, y)
                    lines[1][_].set_visible(True)
            elif self.show_model_CoM == False:
                for _ in range(0, int(nRigidBodies)):
                    lines[1][_].set_visible(False)

            # Update position of the vertical line that follows the value of the plotted variable of the model
            lines[2].set_xdata([i])

            # Update position of the point representing the value of the plotted variable of the model
            lines[3][0].set_data(axis2_xdata[i], axis2_ydata[i])

            if self.show_model_refs == True:
                for _ in range(0, int(nRigidBodies)):
                    dx = model_coordinates[i, 4 * (_) + 2] * 0.1
                    dy = model_coordinates[i, 4 * (_) + 3] * 0.1
                    xs = [model_coordinates[i, _ * 4], model_coordinates[i, _ * 4] + dx]
                    ys = [model_coordinates[i, _ * 4 + 1], model_coordinates[i, _ * 4 + 1] + dy]

                    xs_perp = [model_coordinates[i, _ * 4], model_coordinates[i, _ * 4] - dy]
                    ys_perp = [model_coordinates[i, _ * 4 + 1], model_coordinates[i, _ * 4 + 1] + dx]
                    lines[4][_].set_data(xs, ys)
                    lines[5][_].set_data(xs_perp, ys_perp)
                    lines[4][_].set_visible(True)
                    lines[5][_].set_visible(True)
            elif self.show_model_refs == False:
                for _ in range(0, int(nRigidBodies)):
                    lines[4][_].set_visible(False)
                    lines[5][_].set_visible(False)

            # Update position of the value of the plotted variable of the model
            t1.set_position((float(axis2_xdata[i]), float(axis2_ydata[i]) * 1.05))
            t1.set_text(str(np.round(axis2_ydata[i], 3)))
            return lines

        def on_press(event):
            if event.key.isspace():
                if anim.runs:
                    anim.runs = False
                else:
                    anim.runs = True

        self.figure.canvas.mpl_connect('key_press_event', on_press)
        anim = Player(self.figure, func=animate, frames=int(axis2_xdata.shape[0] - 1), maxi = int(axis2_xdata.shape[0] - 1), init_func=init)

        self.figure.canvas.draw()

if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)