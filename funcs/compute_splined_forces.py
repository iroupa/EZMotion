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

from compute_spline_knots_coeffs import compute_spline_knots_coeffs_degree

def compute_splined_forces(time, y, splineDegree=3):
    """
    
    Function computes the spline knots and coefficients of each force applied in the multibody system.

    Parameters:
    time			:   numpy array
                        original data time vector
    y       	    :   dictionary
                        nested dictionary with each segment number and respective force and local coords
    splineDegree    :   int
                        spline degree

    Returns:
    force_dict    	:   dictionary
                      body_number, force magnitude (Fx, Fy, Fz),
                      mag: (t,c,k) - force B-spline coefficients
                      coords: (t,c,k) - local coords B-spline coefficients
    """

    force_dict = {}

    # Iterate through each force applied in the multibody system
    for force, body in y.items():
        # Create key for each segment number  (bodyUpdate keys i
        force_dict[force] = {}
        # Create temporary dictionary to receive tck coefficients for each force component and local coords of each body
        tck_dict = {}
        for body, components in body.items():
            time = y[force][body]['time']
            force_x = y[force][body]['force'][:, 0]
            force_z = y[force][body]['force'][:, 1]
            coord_x = y[force][body]['coords'][:, 0]
            coord_z = y[force][body]['coords'][:, 1]
            coords_type = y[force][body]['coords_type']
            on_off = y[force][body]['on_off']

            # Calculate spline coeeficients for force and coords data
            tck_force_x = compute_spline_knots_coeffs_degree(time, force_x, splineDegree=splineDegree)
            tck_force_z = compute_spline_knots_coeffs_degree(time, force_z, splineDegree=splineDegree)
            tck_coords_x = compute_spline_knots_coeffs_degree(time, coord_x, splineDegree=splineDegree)
            tck_coords_z = compute_spline_knots_coeffs_degree(time, coord_z, splineDegree=splineDegree)
            tck_coords_on_off = compute_spline_knots_coeffs_degree(time, on_off , splineDegree=splineDegree)
            component_info = {'coords_type': coords_type.lower(),
                              'on_off': on_off,
                              'time': time,
                              'tck_force_x': tck_force_x,
                              'tck_force_z': tck_force_z,
                              'tck_coords_x': tck_coords_x,
                              'tck_coords_z': tck_coords_z,
                              'tck_on_off': tck_coords_on_off}
            # Assign info of each force to the respective body
            tck_dict[body] = component_info

        # Update forces dictionary
        force_dict[force].update(tck_dict)

    return force_dict

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)