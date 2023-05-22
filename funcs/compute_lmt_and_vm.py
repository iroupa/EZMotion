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
from assemble_C_matrix import assemble_C_matrix
from change_of_basis import glob_2_loc
from check_muscle_wrapping import check_muscle_wrapping
from compute_points_length_and_vel import compute_points_length_and_velocity
from compute_wrapping_points import compute_wrapping_points


def compute_lmt_and_vm(muscle_info, q, qp, rb_info):
    """
    Function computes the muscle length and velocity and updates the dictionary
    that contains the parameters of each muscle used in the biomechanical model.

    Parameters:
    muscle_info          : dictionary 
                           information about every muscle of the model
    q                    : list
                           q vector from the kinematic analysis
    qp                   : list
                           qp vector from the kinematic analysis
                           
    Returns:
    l_mt                 : list    
                           musculotendon length of every muscle of the model

    v_m					 : list
                           musculotendon length of every muscle of the model

    muscle_info:		 : dictionary
                           Contains the muscle database

    """
    
    # Initialize l_mt list
    l_mt = []
    
    # Initialize v_m list
    v_m = []
    
    # Go through every muscle 
    for muscle_idx in range(0, len(muscle_info.keys())):

        # Muscle name
        # muscle_name = list(muscle_info.keys())[muscle_idx]

        # Number of muscle elements
        # nb_muscle_element = muscle_info[muscle_idx]['element']

        # Initialize segments length list
        element_length = []
        
        # Initialize segments velocity list
        element_vel = []

        # Compute muscle length for muscles with no via points
        if muscle_info[muscle_idx]['type'].lower() == 's':
            # Get point 'm' (muscle origin)  loc coords from muscle info db
            point_m = muscle_info[muscle_idx]['origin']['coords']

            # Get point 'n' (muscle insertion)  loc coords from muscle info db
            point_n = muscle_info[muscle_idx]['insertion']['coords']

            # Get number of body to which point 'm' belongs
            body_m = muscle_info[muscle_idx]['origin']['body']

            # Get number of body to which point 'n' belongs
            body_n = muscle_info[muscle_idx]['insertion']['body']

            # Compute partial length and velocity
            r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

            # Add partial length and velocity
            element_length.append(r_mn)
            element_vel.append(rp_mn)

        # Compute muscle length for muscles with via points
        elif muscle_info[muscle_idx]['type'].lower() == 'vp':
            # Get total number of via points
            element_n_via_points = muscle_info[muscle_idx]['n_via_points']

            # Compute muscle length and velocity between muscle origin and first via point
            # Get point 'm' (muscle origin)  loc coords from muscle info db
            point_m = muscle_info[muscle_idx]['origin']['coords']

            # Get point 'n' (muscle insertion)  loc coords from muscle info db
            point_n = muscle_info[muscle_idx]['vp1']['coords']

            # Get number of body to which point 'm' belongs
            body_m = muscle_info[muscle_idx]['origin']['body']

            # Get number of body to which point 'n' belongs
            body_n = muscle_info[muscle_idx]['vp1']['body']

            # Compute partial length and velocity
            r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

            # Add partial length and velocity
            element_length.append(r_mn)
            element_vel.append(rp_mn)

            # Compute muscle length and velocity between all via points
            for via_point in range(0, element_n_via_points - 1):
                # Get point 'm' loc coords from muscle info db
                point_m = muscle_info[muscle_idx]['vp' + str(via_point + 1)]['coords']

                # Get point 'n' loc coords from muscle info db
                point_n = muscle_info[muscle_idx]['vp' + str(via_point + 2)]['coords']

                # Get number of body to which point 'm' belongs
                body_m = muscle_info[muscle_idx]['vp' + str(via_point + 1)]['body']

                # Get number of body to which point 'n' belongs
                body_n = muscle_info[muscle_idx]['vp' + str(via_point + 2)]['body']

                # Compute partial length and velocity
                r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                # Add partial length and velocity
                element_length.append(r_mn)
                element_vel.append(rp_mn)

            # Compute muscle length and velocity between last via point and muscle insertion
            # Get point 'm' (muscle origin) loc coords from muscle info db
            point_m = muscle_info[muscle_idx]['vp' + str(element_n_via_points)]['coords']

            # Get point 'n' (muscle insertion)  loc coords from muscle info db
            point_n = muscle_info[muscle_idx]['insertion']['coords']

            # Get number of body to which point 'm' belongs
            body_m = muscle_info[muscle_idx]['vp' + str(element_n_via_points)]['body']

            # Get number of body to which point 'n' belongs
            body_n = muscle_info[muscle_idx]['insertion']['body']

            r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

            element_length.append(r_mn)
            element_vel.append(rp_mn)

        # Compute muscle length for muscles with via points
        elif muscle_info[muscle_idx]['type'].lower() == 'bc':
            # Get wrapping obstacle body
            wrap_obstacle_body = muscle_info[muscle_idx]['wrap_obstacle_body']

            wrap_obstacle_n_body = rb_info[wrap_obstacle_body.lower()]

            # Get wrapping obstacle origin global coords # TODO corrigir coords locais para tornar generico
            obstacle_origin_global_coords = assemble_C_matrix([0, -0.2121]).dot(q[4 * (wrap_obstacle_n_body - 1):
                                                                                  4 * (wrap_obstacle_n_body - 1) + 4])

            # Get wrapping obstacle orientation vector
            obstacle_orientation_vector = q[4 * (wrap_obstacle_n_body - 1) + 2:
                                            4 * (wrap_obstacle_n_body - 1) + 4]

            # Get muscle wrapping point 0 label
            wrap_point_P_label = muscle_info[muscle_idx]['wrap_point_P']

            # Get muscle wrapping point 0 body number
            wrap_point_P_n_body = muscle_info[muscle_idx][wrap_point_P_label]['body']

            # Get muscle wrapping point 0 coords
            wrap_point_P_loc_coords = np.array(muscle_info[muscle_idx][wrap_point_P_label]['coords'])

            # Get muscle wrapping point 0 global coords
            wrap_point_P_glob_coords = assemble_C_matrix(wrap_point_P_loc_coords).dot(q[4 * (wrap_point_P_n_body - 1):
                                                                                        4 * (wrap_point_P_n_body - 1) + 4])

            # Get muscle wrapping point 1 label
            wrap_point_S_label = muscle_info[muscle_idx]['wrap_point_S']

            # Get muscle wrapping point 0 body number
            wrap_point_S_n_body = muscle_info[muscle_idx][wrap_point_S_label]['body']

            # Get muscle wrapping point 0 coords
            wrap_point_S_loc_coords = np.array(muscle_info[muscle_idx][wrap_point_S_label]['coords'])

            # Get muscle wrapping point 0 global coords
            wrap_point_S_glob_coords = assemble_C_matrix(wrap_point_S_loc_coords).dot(q[
                                                                                      4 * (wrap_point_S_n_body - 1):
                                                                                      4 * (wrap_point_S_n_body - 1) + 4])

            # Get muscle wrapping point 0 local coords wrt to obstacle body
            wrap_point_P_obs_local_coords = glob_2_loc(wrap_point_P_glob_coords,
                                                       obstacle_origin_global_coords,
                                                       obstacle_orientation_vector,
                                                       )

            # Get muscle wrapping point 0 local coords wrt to obstacle body
            wrap_point_S_obs_local_coords = glob_2_loc(wrap_point_S_glob_coords,
                                                       obstacle_origin_global_coords,
                                                       obstacle_orientation_vector,
                                                       )

            # Get muscle wrapping direction ('anterior' or 'posterior')
            muscle_wrapping_direction = muscle_info[muscle_idx]['wrap_direction']

            Q, T, wrapping = check_muscle_wrapping(wrap_point_P_obs_local_coords,
                                                   wrap_point_S_obs_local_coords,
                                                   0.03,
                                                   muscle_wrapping_direction)

            if wrapping == False:
                # Compute muscle length and velocity between muscle origin and first via point
                # Get point 'm' (muscle origin)  loc coords from muscle info db
                point_m = muscle_info[muscle_idx]['origin']['coords']

                # Get point 'n' (muscle insertion)  loc coords from muscle info db
                point_n = muscle_info[muscle_idx]['vp1']['coords']

                # Get number of body to which point 'm' belongs
                body_m = muscle_info[muscle_idx]['origin']['body']

                # Get number of body to which point 'n' belongs
                body_n = muscle_info[muscle_idx]['vp1']['body']

                # Compute partial length and velocity
                r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                # Add partial length and velocity
                element_length.append(r_mn)
                element_vel.append(rp_mn)

                # Compute muscle length and velocity between via point 1 and muscle insertion
                # Get point 'm' (muscle origin) loc coords from muscle info db
                point_m = muscle_info[muscle_idx]['vp1']['coords']

                # Get point 'n' (muscle insertion)  loc coords from muscle info db
                point_n = muscle_info[muscle_idx]['insertion']['coords']

                # Get number of body to which point 'm' belongs
                body_m = muscle_info[muscle_idx]['vp1']['body']

                # Get number of body to which point 'n' belongs
                body_n = muscle_info[muscle_idx]['insertion']['body']

                # Compute partial length and velocity
                r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                # Add partial length and velocity
                element_length.append(r_mn)
                element_vel.append(rp_mn)

            elif wrapping == True:
                # Compute muscle length and velocity between muscle origin and first via point
                # Get point 'm' (muscle origin)  loc coords from muscle info db
                point_m = muscle_info[muscle_idx]['origin']['coords']

                # Get point 'n' (muscle insertion)  loc coords from muscle info db
                point_n = muscle_info[muscle_idx]['vp1']['coords']

                # Get number of body to which point 'm' belongs
                body_m = muscle_info[muscle_idx]['origin']['body']

                # Get number of body to which point 'n' belongs
                body_n = muscle_info[muscle_idx]['vp1']['body']

                # Compute partial length and velocity
                r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                # Add partial length and velocity
                element_length.append(r_mn)
                element_vel.append(rp_mn)

                # Compute muscle length and velocity between vp 1 and last wrapping via point
                Q_angle = np.arctan2(Q[1], Q[0])
                T_angle = np.arctan2(T[1], T[0])

                QT_angle_RoM = np.abs(np.abs(Q_angle) - np.abs(T_angle))

                if QT_angle_RoM < 30:
                    nPoints = 15
                elif QT_angle_RoM >= 30 and QT_angle_RoM < 60:
                    nPoints = 30
                elif QT_angle_RoM >= 60 and QT_angle_RoM < 90:
                    nPoints = 45
                elif QT_angle_RoM >= 90 and QT_angle_RoM < 120:
                    nPoints = 60
                elif QT_angle_RoM >= 120 and QT_angle_RoM < 150:
                    nPoints = 75
                elif QT_angle_RoM >= 150 and QT_angle_RoM < 180:
                    nPoints = 90

                # Update muscle info dictionary with wrapping points info
                wrapping_points_loc_coords = compute_wrapping_points(Q_angle, T_angle, muscle_wrapping_direction, nPoints)

                wrapping_via_points_info = {'vp2':{'body': wrap_obstacle_n_body, 'coords': Q}
                }

                for _ in range(0, nPoints):
                    wrapping_via_points_info['vp' + str(_ + 3)] = {'body': wrap_obstacle_n_body, 'coords': wrapping_points_loc_coords[_]}

                wrapping_via_points_info['vp' + str(2 + nPoints + 1)] = {'body': wrap_obstacle_n_body, 'coords': T}

                muscle_info[muscle_idx].update(wrapping_via_points_info)
                muscle_info[muscle_idx]['n_via_points'] = int(len(wrapping_via_points_info.keys())) + 1

                # Obtain updated number of wrapping via points
                element_n_via_points = muscle_info[muscle_idx]['n_via_points']

                # Compute muscle length and velocity between all via points
                for via_point in range(0, element_n_via_points - 1):
                    # Get point 'm' loc coords from muscle info db
                    point_m = muscle_info[muscle_idx]['vp' + str(via_point + 1)]['coords']

                    # Get point 'n' loc coords from muscle info db
                    point_n = muscle_info[muscle_idx]['vp' + str(via_point + 2)]['coords']

                    # Get number of body to which point 'm' belongs
                    body_m = muscle_info[muscle_idx]['vp' + str(via_point + 1)]['body']

                    # Get number of body to which point 'n' belongs
                    body_n = muscle_info[muscle_idx]['vp' + str(via_point + 2)]['body']

                    # Compute partial length and velocity
                    r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                    # Add partial length and velocity
                    element_length.append(r_mn)
                    element_vel.append(rp_mn)

                # Compute muscle length and velocity between muscle point T and muscle insertion
                # Get point 'm' (muscle origin)  loc coords from muscle info db
                point_m = T

                # Get point 'n' (muscle insertion)  loc coords from muscle info db
                point_n = muscle_info[muscle_idx]['insertion']['coords']

                # Get number of body to which point 'm' belongs
                body_m = wrap_obstacle_n_body

                # Get number of body to which point 'n' belongs
                body_n = muscle_info[muscle_idx]['insertion']['body']

                # Compute partial length and velocity
                r_mn, rp_mn = compute_points_length_and_velocity(point_m, body_m, point_n, body_n, q, qp)

                # Add partial length and velocity
                element_length.append(r_mn)
                element_vel.append(rp_mn)

        lmt = 0
        vm = 0
        for i in range(0,len(element_length)):
            lmt += element_length[i]
            vm += element_vel[i]
        
        v_m.append(vm)
        l_mt.append(lmt)
            
    return l_mt, v_m, muscle_info


if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
