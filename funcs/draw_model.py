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

__author__ 		= 'Ivo_Roupa'
__copyright__ 	= "Copyright (C) 2023 Ivo Roupa"
__email__ 		= "iroupa@gmail.com"
__license__ 	= "Apache 2.0"

import pathlib

import matplotlib.pyplot as plt
import numpy as np
from classes.Player import Player

from assemble_C_matrix import assemble_C_matrix
from filter_signal import butter_filter
from read_model_loc_coords import read_model_loc_coords


def draw_model(model_loc_coords_fpath,
               model_coordinates_data,
               variable_label,
               filter_data,
               cutoff_frequency,
               sampling_frequency,
               model_variables,
               nRigidBodies
               ):
    """

    Function plots the segments of the multibody system and a selected variable of the model during the period of analysis.

    Parameters:
    model_loc_coords_fpath  :   str
                                absolute path of the file containing the local coordinates of each segment of the multibody system
    model_coordinates_data  :   numpy.ndarray
                                data of all variables of the multibody system available to plot
    variable_label          :   str
                                label of the variable selected to plot
    filter_data             :   boolean
                                True to filter the raw data of the variable selected to plot / False not to filter the raw data of the variable selected to plot
    cutoff_frequency        :   float
                                cuttoff frequency to filter the raw data of the variable selected to plot
    sampling_frequency      :   float
                                sampling frequency of the model variables
    model_variables         :   list
                                label of all variables of the multibody system available to plot
    nRigidBodies            :   int
                                number of rigid bodies of the multibody system

    Returns:

    """

    # Get the local coordinates of each segment of the multibody system
    linesData = read_model_loc_coords(model_loc_coords_fpath)

    # Create dictionary with the global coordinates of the extremities of each segment of the multibody system
    lines_info = {}

    if len(linesData.keys()) > 0:
        for body_number, loc_coords in linesData.items():
            joint_coords = {}
            for loc_coords_idx in range(0, len(loc_coords)):
                bodyCMatrix = assemble_C_matrix(loc_coords[loc_coords_idx])
                for _ in range(model_coordinates_data.shape[0]):
                    bodyQVec = model_coordinates_data[_, 4 * (body_number - 1):4 * (body_number - 1) + 4]
                    joint = bodyCMatrix.dot(bodyQVec)
                    if _ in joint_coords:
                        joint_coords[_].update({'joint_' + str(loc_coords_idx + 1): bodyCMatrix.dot(bodyQVec)})
                    else:
                        joint_coords[_] = {'joint_' + str(loc_coords_idx + 1): bodyCMatrix.dot(bodyQVec)}
            lines_info[body_number] = joint_coords

    # Create figure and respective axes to plot the model and the selected variable of interest
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

    # Turn grid of variable plot visible
    ax2.grid(True)

    # Get max and min of 'x' and 'y' cartesian coordinates of the model
    x_min = np.amin(model_coordinates_data[:,0::4])
    x_max = np.amax(model_coordinates_data[:,0::4])
    y_min = np.amin(model_coordinates_data[:,1::4])
    y_max = np.amax(model_coordinates_data[:,1::4])

    # x_min = 0
    # x_max = 1.5
    # y_min = 0
    # y_max = 2

    # Set model plot 'x' and 'y' limits
    ax1.set_xlim([x_min, x_max])
    ax1.set_ylim([y_min, y_max])

    # Set plotted variable 'x' and 'y' limits
    ax2.set_xlim([0, model_variables[variable_label].shape[0]-2])

    # Filter raw data of the selected variable of the model
    if filter_data == 'Yes':
        y = butter_filter(model_variables[variable_label][:-1],
                          int(sampling_frequency),
                          float(cutoff_frequency),
                          4)
    else:
        y = model_variables[variable_label][:-1]

    # Get number of frames of processed data
    x = np.arange(0, y.shape[0], 1)

    # Create the lines that represent the segments of the multibody system in the left plot
    stick_lines = sum(
        [ax1.plot([], [], [], '-', color='black', linewidth=1.5) for n in range(int(nRigidBodies))], [])

    v_line = ax2.axvline(0, color="cornflowerblue")

    # Create the line that shows the selected variable of the model in the right plot
    ax2.plot(y)
    point, = ax2.plot([], [], marker="o", color="crimson", ms=15)

    # Expand plot to screen size
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    # Show value of selected variabvle of the model in every frame of the right plot
    t1 = ax2.text(0, 0, '')

    def update(i):

        # Update position of the point representing the value of the plotted variable of the model
        point.set_data(x[i], y[i])

        # Update position of the value of the plotted variable of the model
        t1.set_position((float(x[i]), float(y[i]) * 1.05))
        t1.set_text(str(np.round(y[i], 3)))

        # Update position of the vertical line that follows the value of the plotted variable of the model
        v_line.set_xdata([i])

        # Update the position of the segments of the model
        for _ in range(0, int(nRigidBodies)):
            xs = [lines_info[_ + 1][i]['joint_1'][0], lines_info[_ + 1][i]['joint_2'][0]]
            ys = [lines_info[_ + 1][i]['joint_1'][1], lines_info[_ + 1][i]['joint_2'][1]]
            stick_lines[_].set_data(xs, ys)


    img_output_folder_fpath =  pathlib.Path(model_loc_coords_fpath).parent

    ani = Player(fig, update, maxi=len(y) - 2, img_output_folder_fpath=img_output_folder_fpath)

    plt.show()

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)