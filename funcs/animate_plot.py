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

import os
import matplotlib.pyplot as plt
import numpy as np
from getCMatrix import getCMatrix


def animate(i, model_title, data, markers, legend, right_segments, left_segments, point2lines, pointsofInterest, xlim, ylim, fig, ax, show_refs, writeplots, path):
    """
       Animate model

       Parameters:
       i                    :   int
                                dataFrame with all data
       model                :   str
                                model title
       data                 :   numpy array
                                model coordinates
       markers              :   numpy array
                                model markers laboratory coordinates
       legend               :   str
                                plot legend
       right_segments       :   list
                                list with number of all model right side bodies
       left_segments        :   list
                                list with number of all model left side bodies
       point2lines          :   dictionary
                                Dictionary with pair of local coordinates wrt to each model body. A line will be drawn between these two local coordinates
       pointsofInterest     :   dictionary
                                Dictionary with local coordinates wrt to each model body. A point will be drawn in these local coordinates
       xlim                 :   list
                                Figure 'x' limits
       ylim                 :   list
                                Figure 'y' limits
       fig                  :   matplotlib figure
                                -
       ax                   :   matplotlib axis figure
                                -
       writeplots           :   boolean
                                Flag to export or not export all plot figures
       path                 :   str
                                absolute path to export plot pictures

       Return:

       """

    lines = {}
    points = {}

    q = data[i]

    markerscoords = None

    if markers.size != 0:
        markerscoords = True
        m = markers[i]

    if len(point2lines.keys())>0:
        for bodyNumber, LocCoords in point2lines.items():
            for poiLocCoords in LocCoords:
                if poiLocCoords == [0,0]:
                    bodyCMatrix = np.array([[1, 0, 0, 0],
                                            [0, 1, 0, 0]])
                else:
                    bodyCMatrix = getCMatrix(poiLocCoords)
                bodyQVec = q[4 * (bodyNumber - 1):4 * (bodyNumber - 1) + 4]
                if bodyNumber in lines:
                    lines[bodyNumber] = list(lines[bodyNumber]) + list(np.dot(bodyCMatrix, bodyQVec) )
                else:
                    lines[bodyNumber] = list(np.dot(bodyCMatrix, bodyQVec))

    if len(pointsofInterest.keys()) > 0:
        for bodyNumber, LocCoords in pointsofInterest.items():
            for poiLocCoords in LocCoords:
                bodyCMatrix = getCMatrix(poiLocCoords)
                bodyQVec = q[4 * (bodyNumber - 1):4 * (bodyNumber - 1) + 4]
                if bodyNumber in points:
                    points[bodyNumber] = list(points[bodyNumber]) + list(np.dot(bodyCMatrix, bodyQVec))
                else:
                    points[bodyNumber] = list(np.dot(bodyCMatrix, bodyQVec))

    if markerscoords:
        plotData  = {'lines':lines, 'points': points, 'markers': m}
    else:
        plotData  = {'lines':lines, 'points': points}

    for k, v in plotData.items():
        ax.clear()
        # major_ticks = np.arange(xlim[0], xlim[1], 200)
        # ax.set_xticks(major_ticks)
        # ax.grid(which='major', alpha=0.2)
        # ax.scatter(0, 0, marker='s', color='black')
        ax.scatter([q[0]], [q[1]], marker='o', color='blue')

        # Body coordinates
        ax.scatter([q[0::4]], [q[1::4]], marker='o', color='purple', facecolor='purple', s=15)
        #ax.annotate(str(i / 100), xy=(2.2, 2.4), size=15)
        ax.set_ylabel('Position (m)')
        ax.set_xlabel('Position (m)')
        # plt.xlabel('Time (s)')
        if markerscoords:
            ax.scatter([plotData['markers'][0::2]], [plotData['markers'][1::2]], marker='x', color='black')
        for point in plotData['points'].values():
           ax.scatter(point[0::2], point[1::2])
        for body, line in plotData['lines'].items():
            if show_refs == True:
                x = q[4 * (body - 1)]
                y = q[4 * (body - 1) + 1]
                dx = q[4 * (body - 1) + 2] * 50/1000
                dy = q[4 * (body - 1) + 3] * 50/1000
                dx_unit = "{0:.2f}".format(q[4 * (body - 1) + 2])
                dy_unit = "{0:.2f}".format(q[4 * (body - 1) + 3])
                width = 2.5/500
                plt.arrow(x,y,dx,dy, width=width, color='red', zorder=100)
                plt.arrow(x,y,-dy,dx, width=width, color='blue', zorder=100)
            # label = '(' + str(int(x))+ ' , ' + str(int(y)) + ' : '  + str(dx_unit) + ' , '  + str(dy_unit) + ')'
            # ax.annotate(label, xy=(x, y), size=10)
            if body in right_segments:
                ax.plot(line[0::2], line[1::2], color='green')
                # plt.arrow(x,y,dx,dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')
            elif body in left_segments:
                ax.plot(line[0::2], line[1::2], color='red')
                # plt.arrow(x, y, dx, dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')
            else:
                ax.plot(line[0::2], line[1::2], color='black', linewidth=1.5)
                # plt.arrow(x,y,dx,dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')

        fp_y_pos = -13

        # Draw Force Platess
        # ax.plot([-595, -93], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 1
        # ax.plot([16,   519], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 2
        # ax.plot([625, 1135], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 3
        # ax.annotate('FP 1', xy=(-424, -150), size=14)
        # ax.annotate('FP 2', xy=(187.5, -150), size=14)
        # ax.annotate('FP 3', xy=(800, -150), size=14)
        # ax.annotate(i, xy=(1800, 2600), size=14)

        # ax.set_xlabel(' Anterior Posterior Direction (m)')
        # ax.set_ylabel(' Height (m)')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # ax.grid(True, linestyle='--')
        ax.grid(False, linestyle='--')
        # Remove plot axis
        # ax.set_axis_off()

        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_xlim()
        ax.set_aspect(abs(x1-x0)/abs(y1-y0))
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')

    ax.set_title(model_title)
    # ax.legend(legend)
    if writeplots:
        plots_path = path + "\\Plots"
        print(plots_path)
        if os.path.isdir(plots_path):
            plt.savefig(plots_path + "\\" + "img_" + "{0:03d}".format(i) + ".TIFF", dpi=600)
        else:
            os.makedirs(plots_path)
            plt.savefig(plots_path + "\\" + "img_" + "{0:03d}".format(i) + ".TIFF", dpi=600)

def animate_test(i, model_title, data, markers, legend, right_segments, left_segments, point2lines, pointsofInterest, muscles2lines, grf, xlim, ylim, fig, ax, show_refs, writeplots, path):
    """
       Animate model

       Parameters:
       i                    :   int
                                dataFrame with all data
       model                :   str
                                model title
       data                 :   numpy array
                                model coordinates
       markers              :   numpy array
                                model markers laboratory coordinates
       legend               :   str
                                plot legend
       right_segments       :   list
                                list with number of all model right side bodies
       left_segments        :   list
                                list with number of all model left side bodies
       point2lines          :   dictionary
                                Dictionary with pair of local coordinates wrt to each model body. A line will be drawn between these two local coordinates
       pointsofInterest     :   dictionary
                                Dictionary with local coordinates wrt to each model body. A point will be drawn in these local coordinates
       xlim                 :   list
                                Figure 'x' limits
       ylim                 :   list
                                Figure 'y' limits
       fig                  :   matplotlib figure
                                -
       ax                   :   matplotlib axis figure
                                -
       writeplots           :   boolean
                                Flag to export or not export all plot figures
       path                 :   str
                                absolute path to export plot pictures

       Return:

       """

    lines = {}
    points = {}
    muscles = {}

    q = data[i]

    markerscoords = None

    if markers.size != 0:
        markerscoords = True
        m = markers[i]

    if len(point2lines.keys())>0:
        for bodyNumber, LocCoords in point2lines.items():
            for poiLocCoords in LocCoords:
                if poiLocCoords == [0,0]:
                    bodyCMatrix = np.array([[1, 0, 0, 0],
                                            [0, 1, 0, 0]])
                else:
                    bodyCMatrix = getCMatrix(poiLocCoords)
                bodyQVec = q[4 * (bodyNumber - 1):4 * (bodyNumber - 1) + 4]
                point_glob_coords = bodyCMatrix.dot(bodyQVec).tolist()
                if bodyNumber not in lines:
                    lines[bodyNumber] = point_glob_coords
                else:
                    lines[bodyNumber] = lines[bodyNumber] + point_glob_coords

    if len(pointsofInterest.keys()) > 0:
        for bodyNumber, LocCoords in pointsofInterest.items():
            for poiLocCoords in LocCoords:
                bodyCMatrix = getCMatrix(poiLocCoords)
                bodyQVec = q[4 * (bodyNumber - 1):4 * (bodyNumber - 1) + 4]
                if bodyNumber in points:
                    points[bodyNumber] = list(points[bodyNumber]) + list(np.dot(bodyCMatrix, bodyQVec))
                else:
                    points[bodyNumber] = list(np.dot(bodyCMatrix, bodyQVec))

    if len(muscles2lines.keys()) > 0:
        for muscle in muscles2lines.keys():
            for element in muscles2lines[muscle]['elements'].keys():
                muscle_origin_nbody = int(muscles2lines[muscle]['elements'][element][1]['body'])
                muscle_origin_loc_coords = muscles2lines[muscle]['elements'][element][1]['coords']
                muscle_origin_glob_coords = getCMatrix(muscle_origin_loc_coords).dot(q[4 * (muscle_origin_nbody - 1) : 4 * (muscle_origin_nbody - 1) + 4])
                muscle_insertion_nbody = int(muscles2lines[muscle]['elements'][element][2]['body'])
                muscle_insertion_loc_coords = muscles2lines[muscle]['elements'][element][2]['coords']
                muscle_insertion_glob_coords = getCMatrix(muscle_insertion_loc_coords).dot(q[4 * (muscle_insertion_nbody - 1) : 4 * (muscle_insertion_nbody - 1) + 4])
                if muscle not in muscles.keys():
                    muscles[muscle] = {element: np.concatenate((muscle_origin_glob_coords, muscle_insertion_glob_coords))}
                elif muscle in muscles.keys():
                    muscles[muscle].update({element: np.concatenate((muscle_origin_glob_coords, muscle_insertion_glob_coords))})

    if markerscoords:
        plotData  = {'lines':lines, 'points': points, 'markers': m, 'grf':grf, 'muscles':muscles}
    else:
        plotData  = {'lines':lines, 'points': points, 'grf':grf, 'muscles':muscles}

    for k, v in plotData.items():
        ax.clear()
        # major_ticks = np.arange(xlim[0], xlim[1], 200)
        # ax.set_xticks(major_ticks)
        # ax.grid(which='major', alpha=0.2)
        # ax.scatter(0, 0, marker='s', color='black')
        # ax.scatter([q[0]], [q[1]], marker='o', color='blue')

        # Plot model CoMs
        # ax.scatter([q[0::4]], [q[1::4]], marker='o', color='purple', facecolor='purple', s=15)
        #ax.annotate(str(i / 100), xy=(2.2, 2.4), size=15)
        ax.set_ylabel('Position (m)')
        ax.set_xlabel('Position (m)')
        # plt.xlabel('Time (s)')

        # Plot model experimental markers
        if markerscoords:
            ax.scatter([plotData['markers'][0::2]], [plotData['markers'][1::2]], marker='x', color='black')
        # Plot model points of interest
        for point in plotData['points'].values():
            ax.scatter(point[0::2], point[1::2])
        # Plot segments
        for body, line in plotData['lines'].items():
            if show_refs == True:
                x = q[4 * (body - 1)]
                y = q[4 * (body - 1) + 1]
                dx = q[4 * (body - 1) + 2] * 50/1000
                dy = q[4 * (body - 1) + 3] * 50/1000
                dx_unit = "{0:.2f}".format(q[4 * (body - 1) + 2])
                dy_unit = "{0:.2f}".format(q[4 * (body - 1) + 3])
                width = 2.5/500
                plt.arrow(x,y,dx,dy, width=width, color='red', zorder=100)
                plt.arrow(x,y,-dy,dx, width=width, color='blue', zorder=100)
            # label = '(' + str(int(x))+ ' , ' + str(int(y)) + ' : '  + str(dx_unit) + ' , '  + str(dy_unit) + ')'
            # ax.annotate(label, xy=(x, y), size=10)
            if body in right_segments:
                ax.plot(line[0::2], line[1::2], color='green')
                # plt.arrow(x,y,dx,dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')
            elif body in left_segments:
                ax.plot(line[0::2], line[1::2], color='red')
                # plt.arrow(x, y, dx, dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')
            else:
                ax.plot(line[0::2], line[1::2], color='black', linewidth=1.5)
                # plt.arrow(x,y,dx,dy, width=width, color='blue')
                # plt.arrow(x,y,-dy,dx, width=width, color='red')
        # Plot grf for each force plate
        for force_plate_idx in plotData['grf'].keys():
            ax.plot([grf[force_plate_idx]['CoP_X'][i],
                     grf[force_plate_idx]['CoP_X'][i] + grf[force_plate_idx]['Fx'][i]],
                    [0, grf[force_plate_idx]['Fz'][i]], color='red')
        # Plot muscles
        for muscle in plotData['muscles'].keys():
            for element in plotData['muscles'][muscle]:
                xs =  plotData['muscles'][muscle][element][[0,2]]
                ys =  plotData['muscles'][muscle][element][[1,3]]
                ax.plot(xs, ys, color='black')

        # fp_y_pos = -13

        # Draw Force Platess
        # ax.plot([-595, -93], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 1
        # ax.plot([16,   519], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 2
        # ax.plot([625, 1135], [fp_y_pos, fp_y_pos], color='black', linewidth=5)  # Force plate 3
        # ax.annotate('FP 1', xy=(-424, -150), size=14)
        # ax.annotate('FP 2', xy=(187.5, -150), size=14)
        # ax.annotate('FP 3', xy=(800, -150), size=14)
        # ax.annotate(i, xy=(1800, 2600), size=14)

        # ax.set_xlabel(' Anterior Posterior Direction (m)')
        # ax.set_ylabel(' Height (m)')
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # ax.grid(True, linestyle='--')
        # ax.grid(False, linestyle='--')
        # Remove plot axis
        ax.set_axis_off()

        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_xlim()
        ax.set_aspect(abs(x1-x0)/abs(y1-y0))
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')

    ax.set_title(model_title)
    # ax.legend(legend)
    if writeplots:
        plots_path = path + "\\Plots"
        print(plots_path)
        if os.path.isdir(plots_path):
            plt.savefig(plots_path + "\\" + "img_" + "{0:03d}".format(i) + ".TIFF", dpi=600)
        else:
            os.makedirs(plots_path)
            plt.savefig(plots_path + "\\" + "img_" + "{0:03d}".format(i) + ".TIFF", dpi=600)


if __name__ == "__main__":
    pass
