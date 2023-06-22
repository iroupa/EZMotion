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

from run_forward_analysis import run_forward_analysis
import os

# Subject anthropometric measurements
subject_bodymass = 1  # kg

# Path information
input_folder = r'C:\Documentos\Ivo\GitHub\EZMotion\data_files'
model = r'single_pendulum_FD'
# model = r'double_pendulum_FD'

# Files absolute path
# Modeling file
modeling_file_fpath = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model))
                       if x.endswith('.mod')][0]

# Modeling State : Generalized Coordinates
model_state_pos_fpath = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model))
                     if x.endswith('.q')][0]

# Modeling State : Generalized Velocities
model_state_vel_fpath = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model))
                     if x.endswith('.qp')][0]

# Modeling Forces
model_force_files_folder_path = os.path.join(input_folder, model)

# Analysis options
# kinematic / inverse dynamic / musculoskeletal
analysis_type = 'forward'

# Frequency during analysis
fs = 100

# Time interval between consecutive frames during analysis
dt = 1/fs

# Analysis initial time
t0 = 0.0

# Analysis final time
tf = 10

# Create dummy widget
widget = ''

run_forward_analysis(analysis_type,
                     modeling_file_fpath,
                     model_state_pos_fpath,
                     model_state_vel_fpath,
                     model_force_files_folder_path,
                     os.path.join(input_folder, model),
                     fs,
                     t0,
                     tf,
                     'script',
                     widget)


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
