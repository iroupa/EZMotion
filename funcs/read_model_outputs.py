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

import csv
import numpy as np


def read_model_outputs(fpath):
    """
    
    Function reads and filter the model outputs data from file using
    the residual analysis method proposed by Winter.

    Parameters:
        fpath       :   (str)
                        Absolute path of the model outputs file

    Returns:
        nRigidBodies                :   int
                                        number of rigid bodies od the multibody system
        nFrames                     :   int
                                        number of frames of the analysis
        sampling_frequency          :   float
                                        sampling frequency of the analysis
        model_coordinates_data      :   numpy.ndarray
                                        generalized coordinates of the multibody system during all analysis
        model_plot_variables        :   dictionary
                                        output data of analysis (coordinates, velocities, accelerations, angles, ...)
        model_plot_variables_label  :   list
                                        labels of analysis variables

    """
    
    file_sections_info = {}

    nRigidBodies = 0
    nFrames = 0
    sampling_frequency = 0
    model_coordinates_data = None
    model_plot_variables = {}
    model_plot_variables_labels = []

    with open(fpath, 'r', newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if 'Number_of_Rigid_Bodies' in str(row):
                nRigidBodies = [i.split(':', 1)[1] for i in row]
                for r in ["'", '[', ']']:
                    nRigidBodies = str(nRigidBodies).replace(r, '')
                nRigidBodies = int(nRigidBodies)
                # print('self.m_nRigidBodies',self.m_nRigidBodies)
            elif 'Number_of_Frames' in str(row):
                nFrames = [i.split(':', 1)[1] for i in row]
                for r in ["'", '[', ']']:
                    nFrames = str(nFrames).replace(r, '')
                nFrames = int(nFrames)
                # print('nFrames',nFrames)
            elif 'Sampling_Frequency' in str(row):
                sampling_frequency = [i.split(':', 1)[1] for i in row]
                for r in ["'", '[', ']']:
                    sampling_frequency = str(sampling_frequency).replace(r, '')
                sampling_frequency = int(sampling_frequency)
                # print('self.m_sampling_frequency',self.m_sampling_frequency)
            elif '***** Coordinates [m] *****' in str(row):
                file_sections_info['Coordinates'] = idx
                # print('m')
            elif '***** Velocities [m.s^-1] *****' in str(row):
                file_sections_info['Velocities'] = idx
                # print('vels')
            elif '***** Accelerations [m.s^-2] *****' in str(row):
                file_sections_info['Accelerations'] = idx
                # print('accs')
            elif '***** Angles [deg] *****' in str(row):
                file_sections_info['Angles'] = idx
                # print('deg')
            elif '***** Angles Velocities [deg.s^-1] *****' in str(row):
                file_sections_info['Angles Velocities'] = idx
                # print('deg.s^-1')
            elif '***** Angles Accelerations [deg.s^-2] *****' in str(row):
                file_sections_info['Angles Accelerations'] = idx
                # print('deg.s^-2')
            elif '***** Moments of Force [N.m] *****' in str(row):
                file_sections_info['Moments of Force'] = idx
                # print('N.m')
            elif '***** Joints Powers [W] *****' in str(row):
                file_sections_info['Joints Power'] = idx
                # print('W')
            elif '***** Muscles normalized length [%] *****' in str(row):
                file_sections_info['Muscle Normalized Lengths'] = idx
                # print('%')
            elif '***** Muscles activations [%] *****' in str(row):
                file_sections_info['Muscle Activations'] = idx
                # print('%')

    with open(fpath, 'r', newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        model_outputs_data = list(csv_reader)

    # Labels of the sections of the model outputs file containing different types of model data
    file_sections_labels = ['Coordinates',
                            'Velocities',
                            'Accelerations',
                            'Angles',
                            'Angles Velocities',
                            'Angles Accelerations',
                            'Moments of Force',
                            'Joints Power',
                            'Muscle Normalized Lengths',
                            'Muscles Activations',
                            ]

    # Units of each sections of the model outputs file containing different types of model data
    file_sections_units = [[' [m]', ' [ deg]'],
                           [' [m.s^-1]', ' [ deg.s^-1]'],
                           [' [m.s^-2]', ' [ deg.s^-2]'],
                           [' [deg]', ' [ deg]'],
                           [' [deg.s^-1]', ' [ deg.s^-1]'],
                           [' [deg.s^-2]', ' [ deg.s^-2]'],
                           [' [N.m]', ' [N.m]'],
                           [' [W]', ' [W]'],
                           [' [%]', ' [%]'],
                           [' [%]', ' [%]']
                           ]

    for idx in range(0, len(file_sections_labels)):
        if file_sections_labels[idx] in file_sections_info:
            # Get labels of model "Coordinates" section
            header = model_outputs_data[file_sections_info[file_sections_labels[idx]] + 1]

            # Get model output data for each type of variable
            model_data = np.asarray(model_outputs_data[file_sections_info[file_sections_labels[idx]] + 2:
                                                       file_sections_info[file_sections_labels[idx]] + int(nFrames)],
                                    dtype='float')

            # Get generalized coordinates of the model
            if "Coordinates" in file_sections_labels[idx]:
                model_coordinates_data = model_data[:, 2:]

            # Get label of each variable of each type of model data (Coordinates, velocities, accelerations, angles, ...)
            for _ in range(2, len(header)):
                if '#' in header[_]:
                    header_element = str(header[_].replace('#', '')).strip() + file_sections_units[idx][0]
                elif 'Mixed' in header[_]:
                    header_element = str(header[_].replace('#', '')).strip() + file_sections_units[idx][1]
                else:
                    header_element = str(header[_]).strip() + file_sections_units[idx][0]

                # Assign label and data of each variable of each type of model data
                # (Coordinates, velocities, accelerations, angles, ...)
                model_plot_variables[header_element] = model_data[:, _]
                model_plot_variables_labels.append(header_element)

    return nRigidBodies, nFrames, sampling_frequency, model_coordinates_data, model_plot_variables,\
           model_plot_variables_labels


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
