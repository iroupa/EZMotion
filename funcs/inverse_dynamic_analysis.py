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
from get_trajectory_drivers_info import get_trajectory_drivers_info
from compute_splined_forces_coords import compute_splined_forces_coords


def inverse_dynamic_analysis(t, q, qpp, model_n_mixed_angular_drivers, modeling_file_fpath, nRigidBodies,
                             modeling_file, modelKinematics, massMatrix, generalized_forces_vector, forceSplineFuncs):
    """

    Function performs the inverse dynamic analysis of a given multibody system.

    Parameters:
        t                               :   float
                                            time instant of the analysis
        q                               :   numpy.array
                                            vector of generalized coordinates of the multibody system
        qpp                             :   numpy.array
                                            vector of generalized accelerations of the multibody system
        model_n_mixed_angular_drivers   :   int
                                            total number of mixed angular drivers of the multibody system
        modeling_file_fpath             :   string
                                            absolute path of the modeling file of the multibody system
        nRigidBodies                    :   int
                                            total number of rigid bodies of the multibody system
        modeling_file                   :   numpy.array
                                            modeling file of the multibody system
        modelKinematics                 :   numpy.array
                                            jacobian of the the multibody system
        massMatrix                      :   numpy.array
                                            mass matrix of the multibody system
        generalized_forces_vector       :   numpy.array
                                            vector of generalized external forces the multibody system
        forceSplineFuncs                :   dictionary
                                            body_number, force magnitude (Fx, Fy, Fz),
                                            mag: (t,c,k) - force B-spline coefficients
                                            coords: (t,c,k) - local coords B-spline coefficients

    Returns:
        lmm                             :   numpy.array
                                            lagrange multipliers obtained by solving the equations of motion
                                            of the multibody system
    """

    if model_n_mixed_angular_drivers > 1:
        # Get index of rows of trajectory drivers used in Mixed Coordinates
        rows_to_remove = get_trajectory_drivers_info(modeling_file_fpath)

        # Get index of columns of angular generalized coordinates used in Mixed Coordinates
        cols_to_remove = [x for x in range(nRigidBodies * 4, nRigidBodies * 4 + model_n_mixed_angular_drivers)]

        # Check if model contains a double support joint
        support_joints = [x for x in modeling_file[:, 0] if x == 8]

        # Set starting index of trajectory drivers constraints
        if len(support_joints) > 0:
            trajectory_drivers_start_idx = 0
        elif len(support_joints) == 0:
            trajectory_drivers_start_idx = 2

        # Remove rows of trajectory drivers used in Mixed Coordinates
        dPhidq_updated = np.delete(modelKinematics['dPhidq'],
                                   rows_to_remove[trajectory_drivers_start_idx:],
                                   axis=0)
        # Remove columns of angular generalized coordinates
        dPhidq_updated = np.delete(modelKinematics['dPhidq'], cols_to_remove, axis=1)
    else:
        dPhidq_updated = modelKinematics['dPhidq']

        # Update generalized_forces_vector
    generalized_forces_vector = compute_splined_forces_coords(t, q, forceSplineFuncs, generalized_forces_vector)

    A = dPhidq_updated.T
    b = generalized_forces_vector[: nRigidBodies * 4] - massMatrix[: nRigidBodies * 4, : nRigidBodies * 4].dot(
        qpp[: nRigidBodies * 4])

    # Compute the lagrange multipliers of the system
    lmm = np.linalg.lstsq(A, b, rcond=None)[0]

    return lmm


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
