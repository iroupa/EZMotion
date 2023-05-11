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

from assemble_g_M import assemble_g_M
from compute_fmP import compute_fmP
from compute_ge_bodies import compute_ge_bodies
from compute_ge_fm import compute_ge_fm
from compute_lm import compute_lm
from compute_lmt_and_vm import compute_lmt_and_vm
from compute_pennation_angle import compute_pennation_angle
from contractile_force import compute_contractile_element
from force_length import compute_force_length_component
from force_velocity import compute_force_velocity_component
from passive_force import compute_passive_element


def muscle_analysis(muscle_info, q, qp, nCoordinates, rb_info):
    """
    
    Function computes and assembles the vector of passive and contractile 
    muscle generalized forces, and the lists with the force length and force velocity
    components and the muscle passive and contractile force of each muscle of the
    biomechanical model.
    
    Parameters:
    muscle_info     :   dictionary
                        muscle parameters database (fo, alfa, lo, lt, points) of the biomechanical model 
    q               :   numpy.array
                        vector of generalized coordinates of the multibody system
    qp              :   numpy.array
                        vector of generalized velocities of the multibody system
    nCoordinates    :   int
                        number of generalized coordinates of the multibody system
    rb_info         :   dictionary
                        label and number of each segmento of the multibody system
                        
    Returns:
    g_M_pe          :   numpy.ndarray
                        vector of passive muscle generalized forces
    g_M_ce          :   numpy.ndarray
                        vector of contractile muscle generalized forces
    fl_component    :   list
                        force length component of each muscle of the biomechanical model
    fv_component    :   list
                        force velocity component of each muscle of the biomechanical model
    f_pe            :   list
                        passive force of each muscle of the biomechanical model
    f_ce            :   list
                        contractile force of each muscle of the biomechanical model
    """



    # Compute musculotendon length and muscle contraction velocity
    l_mt, v_m, muscle_info = compute_lmt_and_vm(muscle_info, q, qp, rb_info)
    
    # Compute pennation angle
    pennation_angle = compute_pennation_angle(muscle_info, l_mt)

    # Compute muscle length
    l_m = compute_lm(muscle_info, pennation_angle, l_mt)
    
    # Compute the muscle force according to the force_length and force_velocity curves 
    fl_component = compute_force_length_component(muscle_info, l_m, 'Hill')
    fv_component = compute_force_velocity_component(muscle_info, v_m, 'Hill')
    
    # Compute contractile and passive force 
    f_pe = compute_passive_element(muscle_info, l_m, 'on')
    f_ce = compute_contractile_element(muscle_info, fl_component, fv_component, 'on')
    
    # Compute fmP (vectorial) - forces applied in each point of the muscles
    fmP_pe = compute_fmP(muscle_info, f_pe)
    fmP_ce = compute_fmP(muscle_info, f_ce)

    # Compute ge_fm force vector for every force applied in every point every muscle
    ge_fm_pe = compute_ge_fm(muscle_info, fmP_pe)
    ge_fm_ce = compute_ge_fm(muscle_info, fmP_ce)

    # Compute ge_fm force vector for every body of every muscle
    ge_bodies_pe = compute_ge_bodies(ge_fm_pe)
    ge_bodies_ce = compute_ge_bodies(ge_fm_ce)

    # Compute vector of the generalized coordinates of the whole system for every muscle (each line is a different muscle)
    g_M_pe = assemble_g_M(nCoordinates, ge_bodies_pe)
    g_M_ce = assemble_g_M(nCoordinates, ge_bodies_ce)

    return g_M_pe, g_M_ce, fl_component, fv_component, f_pe, f_ce

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)