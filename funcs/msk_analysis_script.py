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

from run_inverse_analysis import run_inverse_analysis
import os

# Subject anthropometric measurements
subject_bodymass    = 54 # kg

# Path information
input_folder        = r'C:\Documentos\Ivo\GitHub\EZMotion\data_files'
model               = r'trial_0003_1passagem_FCC'

# Files absolute path
modeling_file_fpath         = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.mod')][0]
model_data_fpath            = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.data')][0]
model_drivers_labels_fpath  = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.lbl')][0]
model_state_fpath           = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.q')][0]
model_force_files_fpath     = [os.path.join(input_folder, model, x) for x in os.listdir(os.path.join(input_folder, model)) if x.endswith('.f')]#[0]
muscle_db_fpath             = os.path.join(input_folder, model, r'muscle_attachments_original_local_coords_pelvis_corrected_simple.msk')

analysis_type = 'dynamic'

# Frequency during kinematic analysis
fs = 100

# Time interval between consecutive frames during kinematic analysis
dt = 1/fs

# Kinematic Analysis initial time
t0 = 0.74

# Kinematic Analysis final time
tf = 1.82

# Create widget
widget = ''

run_inverse_analysis(analysis_type,
                     subject_bodymass,
                     modeling_file_fpath,
                     model_data_fpath,
                     model_state_fpath,
                     model_drivers_labels_fpath,
                     model_force_files_fpath,
                     muscle_db_fpath,
                     input_folder,
                     fs,
                     t0,
                     tf,
                     widget,
                     'script'
                     )