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

import numpy as np
from scipy.interpolate import splev
from change_of_basis import glob_2_loc
from update_G_vector import update_G_vector
from apply_force import apply_force


def compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector):
    """
    Function compute new coordinates and forces and update the vector of generalized forces.

    Parameters:
        t							:   float
                                        new time instant
        q							:   numpy.array
                                        vector of generalized coordinates of the multibody system
        forceSplineFuncs			:   dictionary
                                        body_number, force magnitude (Fx, Fy, Fz),
                                        mag: (t,c,k) - force B-spline coefficients
                                        coords: (t,c,k) - local coords B-spline coefficients
        generalized_forces_vector	:   numpy.array
                                        vector of generalized forces of the multibody system

    Returns:
        generalized_forces_vector	:   numpy.array
                                        updated vector of generalized forces of the multibody system

    """

    for force, body in forceSplineFuncs.items():
        body = int(list(body.keys())[0])
        coordinates_type = forceSplineFuncs[force][body]['coords_type'].lower()
        tck_force_x = forceSplineFuncs[force][body]['tck_force_x']
        tck_force_z = forceSplineFuncs[force][body]['tck_force_z']
        tck_coord_x = forceSplineFuncs[force][body]['tck_coords_x']
        tck_coord_z = forceSplineFuncs[force][body]['tck_coords_z']
        tck_on_off = forceSplineFuncs[force][body]['tck_on_off']

        # Spline on_off
        on_off = splev(t, tck_on_off, der=0, ext=2)

        if on_off > 0.2:
            on_off = 1
        else:
            on_off = 0

        # Splined Force components
        new_force_x = splev(t, tck_force_x, der=0, ext=2) * on_off
        new_force_z = splev(t, tck_force_z, der=0, ext=2) * on_off

        # Splined Coordinates components
        new_coord_x = splev(t, tck_coord_x, der=0, ext=2)
        new_coord_z = splev(t, tck_coord_z, der=0, ext=2)

        # New force vector
        new_force = np.hstack((new_force_x, new_force_z))

        # New coordinates vector
        new_coords = np.hstack((new_coord_x, new_coord_z))

        if coordinates_type == 'locals':
            generalized_force = {body: apply_force(new_force, new_coords)}
            generalized_forces_vector = update_G_vector(generalized_forces_vector, generalized_force)
        # Change from global to local coordinates with respect to body local reference frame
        elif coordinates_type == 'globals':
            pointP = new_coords
            origin = q[4 * (body - 1):4 * (body - 1) + 2]
            vector = q[4 * (body - 1) + 2:4 * (body - 1) + 4]
            new_coords = glob_2_loc(pointP, origin, vector)
            generalized_force = {body: apply_force(new_force, new_coords)}
            generalized_forces_vector = update_G_vector(generalized_forces_vector, generalized_force)

    return generalized_forces_vector


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
