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

from math import inf

import numpy as np
from scipy.optimize import minimize

from det_crossed_joints import det_crossed_joints


# from det_crossed_joints import det_joints_bodies, det_crossed_joints

def cost_function(x, nh, nm):
    """

    Function defines the cost function used in the static optimization.

    Parameters:
    x   :   numpy.array
            solution of the static optimization problem
    nh  :   int
            number of kinematic constraint equations
    nm  :   int
            number of muscles of the biomechanical model

    Returns:
    f0  :   float
            value of the

    """

    a = x[nh:]

    fo = 0
    for m in range(nm):
        fo += a[m]**2

    return fo

def cost_function_jacobian(x, nh, nm):
    """
    Define cost function to evaluate in the optimization problem.
    OpenSim
    """

    gradient = np.zeros(nh+nm)

    for m in range(nh, nh+nm):
        gradient[m] = x[m]*2

    return gradient

def Jacobian(xo,
             generalized_forces_vector,
             dPhidq,
             mass_matrix,
             q,
             qpp,
             t,
             activation_rep,
             nCoordinates,
             totalNumberConstraints,
             gravitationalForces,
             g_M_pe,
             g_M_ce):

     return np.concatenate((dPhidq.T, g_M_ce.T), axis = 1)



# def cost_function2(x, nh, nm, fl_component, fv_component, muscle_info):
#     """
#     Define cost function to evaluate in the optimization problem.
#     """
#
#     a_values = x[nh:]
#
#     fo = 0
#     for m in range(nm):
#         muscle_name = list(muscle_info.keys())[m]
#         a = a_values[m]
#         fl = fl_component[m]
#         fv = fv_component[m]
#         F0 = muscle_info[muscle_name]['fo']
#         fo = fo + ((a*F0)/(fl*fv))**3
#
#     return fo
#
# def cost_function3(x, nh, nm, fl_component, fv_component):
#     """
#     Define cost function to evaluate in the optimization problem.
#     """
#
#     a_values = x[nh:]
#
#     fo = 0
#     for m in range(nm):
#         a = a_values[m]
#         fl = fl_component[m]
#         fv = fv_component[m]
#         fo = fo + (a/(fl*fv))**3
#
#     return fo
#
# def cost_function4(x, nh, nm, fl_component, fv_component):
#     """
#     Define cost function to evaluate in the optimization problem.
#     """
#
#     a_values = x[nh:]
#
#     fo = 0
#     for m in range(nm):
#         a = a_values[m]
#         fl = fl_component[m]
#         fv = fv_component[m]
#         fo = fo + (a*fl*fv)**3
#
#     return fo

def define_bounds(nh, nm, muscle_info, dataConst):
    """
    Define the bounds for each variable.
    
    Parameters:
    nh                  : float
                          total number of constraints  
    nm                  : float
                          number of muscles of the model
                          
    Returns:
    bnds                : tuple
                          bounds for every variable
    """
    
    # Bounds for each variable
    b_lagrange_rem = [-inf, +inf]

    # Bounds for joins crossed by muscles
    # b_lagrange_joint = [-10.0**(-3), +10.0**(-3)]
    b_lagrange_joint = [-10.0, +10.0]

    # Bounds for muscle activation
    b_a = [0.0, 1.0]
    
    # Size of x (lambda and a)
    size_x = nh + nm
    
    # Initialize bounds list
    bnds = list(np.zeros(size_x))

    # Define bounds for the lagrange multipliers
    for i in range(0, nh):
        bnds[i] = b_lagrange_rem

    for i in range(nh, size_x):
        bnds[i] = b_a
    
    # Determine the bodies connected to the muscles
    # joints_bodies = det_joints_bodies(muscle_info)
    
    # Determine the joints crossed by muscles
    crossed_joints_list = det_crossed_joints(muscle_info)

    # Define bounds for the joints crossed by muscles
    for joint in crossed_joints_list:
        a = joint
        # Iterate through all lines of Jacobian matrix
        for row in range(len(dataConst[:, 1])):
            constraint_type = dataConst[row, 0]
            if constraint_type == 2 or constraint_type == 4:
                if sorted(joint) == sorted([dataConst[row, 2], dataConst[row, 3]]):
                    lagrange_line = dataConst[row, 1]
                    bnds[int(lagrange_line)] = b_lagrange_joint

    # Transform bound list into tuple
    for b in range(0,len(bnds)):
        bnds[b] = tuple(bnds[b])
    
    bnds = tuple(bnds)
    
    return bnds

# def constraint_RP(x, forceSplineFuncs, generalized_forces_vector, dPhidq,
#                massMatrix, q, qpp, t, lagrangeMultipliers_rep, activation_rep, nCoordinates,
#                totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
#
#     # Colocar fora da optimização
#     generalized_forces_vector = np.zeros(nCoordinates)
#
#     generalized_forces_vector = updateGVector(generalized_forces_vector, gravitationalForces)
#
#     for force, body in forceSplineFuncs.items():
#         body = int(list(body.keys())[0])
#         coordinates_type = forceSplineFuncs[force][body]['coords_type'].lower()
#         tck_force_x = forceSplineFuncs[force][body]['tck_force_x']
#         tck_force_z = forceSplineFuncs[force][body]['tck_force_z']
#         tck_coord_x = forceSplineFuncs[force][body]['tck_coords_x']
#         tck_coord_z = forceSplineFuncs[force][body]['tck_coords_z']
#         tck_on_off = forceSplineFuncs[force][body]['tck_on_off']
#
#         # Spline on_off
#         on_off = splev(t, tck_on_off, der=0, ext=2)
#
#         if on_off > 0.2:
#             on_off = 1
#         else:
#             on_off = 0
#
#         # Splined Force components
#         new_force_x = splev(t, tck_force_x, der=0, ext=2) * on_off
#         new_force_z = splev(t, tck_force_z, der=0, ext=2) * on_off
#
#         # Splined Coordinates components
#         new_coord_x = splev(t, tck_coord_x, der=0, ext=2)
#         new_coord_z = splev(t, tck_coord_z, der=0, ext=2)
#
#         # New force vector
#         new_force = np.hstack((new_force_x, new_force_z))
#
#         # New coordinates vector
#         new_coords = np.hstack((new_coord_x, new_coord_z))
#
#         if coordinates_type == 'locals':
#             generalized_force = {body: applyForce(new_force, new_coords)}
#             generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)
#         elif coordinates_type  == 'globals':
#             # Change from global to local coordinates with respect to body local reference frame
#             pointP = new_coords
#             origin = q[4*(body-1):4*(body-1)+2]
#             vector = q[4*(body-1)+2:4*(body-1)+4]
#             new_coords = glob_2_loc(pointP, origin, vector)
#             generalized_force = {body: applyForce(new_force, new_coords)}
#             generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)
#
#     g_PE = np.zeros(nCoordinates)
#     for g_pe in g_M_pe:
#         g_PE += g_pe
#
#     dPhidq_chi = np.append(dPhidq.T, - g_M_ce.T, axis=1)
#
#     f_eq = massMatrix.dot(qpp) + dPhidq_chi.dot(x) - generalized_forces_vector - g_PE
#
#     return f_eq

def constraint_IFR(x,
               generalized_forces_vector,
               dPhidq,
               massMatrix,
               q,
               qpp,
               t,
               lagrangeMultipliers_rep,
               activation_rep,
               nCoordinates,
               totalNumberConstraints,
               gravitationalForces,
               g_M_pe,
               g_M_ce):

    # # Colocar fora da optimização
    # generalized_forces_vector = np.zeros(nCoordinates)
    #
    # generalized_forces_vector = updateGVector(generalized_forces_vector, gravitationalForces)
    #
    # for force, body in forceSplineFuncs.items():
    #     body = int(list(body.keys())[0])
    #     coordinates_type = forceSplineFuncs[force][body]['coords_type'].lower()
    #     tck_force_x = forceSplineFuncs[force][body]['tck_force_x']
    #     tck_force_z = forceSplineFuncs[force][body]['tck_force_z']
    #     tck_coord_x = forceSplineFuncs[force][body]['tck_coords_x']
    #     tck_coord_z = forceSplineFuncs[force][body]['tck_coords_z']
    #     tck_on_off = forceSplineFuncs[force][body]['tck_on_off']
    #
    #     # Spline on_off
    #     on_off = splev(t, tck_on_off, der=0, ext=2)
    #
    #     if on_off > 0.2:
    #         on_off = 1
    #     else:
    #         on_off = 0
    #
    #     # Splined Force components
    #     new_force_x = splev(t, tck_force_x, der=0, ext=2) * on_off
    #     new_force_z = splev(t, tck_force_z, der=0, ext=2) * on_off
    #
    #     # Splined Coordinates components
    #     new_coord_x = splev(t, tck_coord_x, der=0, ext=2)
    #     new_coord_z = splev(t, tck_coord_z, der=0, ext=2)
    #
    #     # New force vector
    #     new_force = np.hstack((new_force_x, new_force_z))
    #
    #     # New coordinates vector
    #     new_coords = np.hstack((new_coord_x, new_coord_z))
    #
    #     if coordinates_type == 'locals':
    #         generalized_force = {body: applyForce(new_force, new_coords)}
    #         generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)
    #     elif coordinates_type  == 'globals':
    #         # Change from global to local coordinates with respect to body local reference frame
    #         pointP = new_coords
    #         origin = q[4*(body-1):4*(body-1)+2]
    #         vector = q[4*(body-1)+2:4*(body-1)+4]
    #         new_coords = glob_2_loc(pointP, origin, vector)
    #         generalized_force = {body: applyForce(new_force, new_coords)}
    #         generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)

    g_PE = np.zeros(nCoordinates)
    for g_pe in g_M_pe:
        g_PE += g_pe

    dPhidq_chi = np.append(dPhidq.T, - g_M_ce.T, axis=1)

    f_eq = massMatrix.dot(qpp) + dPhidq_chi.dot(x) - generalized_forces_vector - g_PE

    return f_eq


def constraint(x,
               generalized_forces_vector,
               dPhidq,
               massMatrix,
               q,
               qpp,
               t,
               activation_rep,
               nCoordinates,
               totalNumberConstraints,
               gravitationalForces,
               g_M_pe,
               g_M_ce):

    g_PE = np.zeros(nCoordinates)
    for g_pe in g_M_pe:
        g_PE += g_pe

    dPhidq_chi = np.append(dPhidq.T, - g_M_ce.T, axis=1)

    f_eq = massMatrix.dot(qpp) + dPhidq_chi.dot(x) - generalized_forces_vector - g_PE

    return f_eq



# def constraint_RP(x, forceSplineFuncs, generalized_forces_vector, dPhidq,
#                massMatrix, q, qpp, t, lagrangeMultipliers_rep, activation_rep, nCoordinates,
#                totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
#
#     # Colocar fora da optimização
#     generalized_forces_vector = np.zeros(nCoordinates)
#
#     generalized_forces_vector = updateGVector(generalized_forces_vector, gravitationalForces)
#
#     for force, body in forceSplineFuncs.items():
#         body = int(list(body.keys())[0])
#         coordinates_type = forceSplineFuncs[force][body]['coords_type'].lower()
#         tck_force_x = forceSplineFuncs[force][body]['tck_force_x']
#         tck_force_z = forceSplineFuncs[force][body]['tck_force_z']
#         tck_coord_x = forceSplineFuncs[force][body]['tck_coords_x']
#         tck_coord_z = forceSplineFuncs[force][body]['tck_coords_z']
#         tck_on_off = forceSplineFuncs[force][body]['tck_on_off']
#
#         # Spline on_off
#         on_off = splev(t, tck_on_off, der=0, ext=2)
#
#         if on_off > 0.2:
#             on_off = 1
#         else:
#             on_off = 0
#
#         # Splined Force components
#         new_force_x = splev(t, tck_force_x, der=0, ext=2) * on_off
#         new_force_z = splev(t, tck_force_z, der=0, ext=2) * on_off
#
#         # Splined Coordinates components
#         new_coord_x = splev(t, tck_coord_x, der=0, ext=2)
#         new_coord_z = splev(t, tck_coord_z, der=0, ext=2)
#
#         # New force vector
#         new_force = np.hstack((new_force_x, new_force_z))
#
#         # New coordinates vector
#         new_coords = np.hstack((new_coord_x, new_coord_z))
#
#         if coordinates_type == 'locals':
#             generalized_force = {body: applyForce(new_force, new_coords)}
#             generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)
#         elif coordinates_type  == 'globals':
#             # Change from global to local coordinates with respect to body local reference frame
#             pointP = new_coords
#             origin = q[4*(body-1):4*(body-1)+2]
#             vector = q[4*(body-1)+2:4*(body-1)+4]
#             new_coords = glob_2_loc(pointP, origin, vector)
#             generalized_force = {body: applyForce(new_force, new_coords)}
#             generalized_forces_vector = updateGVector(generalized_forces_vector, generalized_force)
#
#     g_PE = np.zeros(nCoordinates)
#     for g_pe in g_M_pe:
#         g_PE += g_pe
#
#     dPhidq_chi = np.append(dPhidq.T, - g_M_ce.T, axis=1)
#
#     f_eq = massMatrix.dot(qpp) + dPhidq_chi.dot(x) - generalized_forces_vector - g_PE
#
#     return f_eq

def optimizer(bnds, xo, nh, nm, generalized_forces_vector, dPhidq,
              massMatrix, q, qpp, t, activation_rep, nCoordinates,
              totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
    """
    Optimizer function
    """

    con = {'type':    'eq',
           'jac': Jacobian,
           'fun': constraint,
           'args':(generalized_forces_vector, dPhidq,
               massMatrix, q, qpp, t, activation_rep, nCoordinates,
               totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce)}

    # sol = minimize(cost_function, xo, args = (nh, nm), bounds = bnds, method='SLSQP', constraints = con, options={'maxiter': 5000})
    sol = minimize(cost_function, xo, args = (nh, nm), bounds = bnds, method='SLSQP', jac = cost_function_jacobian, constraints = con, options={'maxiter': 5000, 'disp': True})

    return sol.x, sol


#
# def optimizer2(bnds, xo, nh, nm, fl_component, fv_component, muscle_info, forceSplineFuncs,
#                generalized_forces_vector, modelKinematics, massMatrix, q, t, lagrangeMultipliers_rep,
#                activation_rep, nCoordinates, totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
#     """
#     Optimizer function.
#     """
#
#     con = {'type':'eq','fun':constraint,'args':(forceSplineFuncs, generalized_forces_vector, modelKinematics,
#                massMatrix, q, t, lagrangeMultipliers_rep, activation_rep, nCoordinates,
#                totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce,)}
#
#     sol = minimize(cost_function2, xo, args=(nh, nm, fl_component, fv_component, muscle_info),
#                    method='SLSQP', bounds=bnds, constraints=con)
#
#     return sol.x, sol
#
# def optimizer3(bnds, xo, nh, nm, fl_component, fv_component, forceSplineFuncs,
#                generalized_forces_vector, modelKinematics, massMatrix, q, t, lagrangeMultipliers_rep,
#                activation_rep, nCoordinates, totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
#     """
#     Optimizer function.
#     """
#
#     con = {'type':'eq','fun':constraint,'args':(forceSplineFuncs, generalized_forces_vector, modelKinematics,
#                massMatrix, q, t, lagrangeMultipliers_rep, activation_rep, nCoordinates,
#                totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce,)}
#
#     sol = minimize(cost_function3, xo, args=(nh, nm, fl_component, fv_component),
#                    method='SLSQP', bounds=bnds, constraints=con)
#
#     return sol.x, sol
#
# def optimizer4(bnds, xo, nh, nm, fl_component, fv_component, forceSplineFuncs,
#                generalized_forces_vector, modelKinematics, massMatrix, q, t, lagrangeMultipliers_rep,
#                activation_rep, nCoordinates, totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce):
#     """
#     Optimizer function.
#     """
#
#     con = {'type':'eq','fun':constraint,'args':(forceSplineFuncs, generalized_forces_vector, modelKinematics,
#                massMatrix, q, t, lagrangeMultipliers_rep, activation_rep, nCoordinates,
#                totalNumberConstraints, gravitationalForces, g_M_pe, g_M_ce,)}
#
#     sol = minimize(cost_function4, xo, args=(nh, nm, fl_component, fv_component),
#                    method='SLSQP', bounds=bnds, constraints=con)
#
#     return sol.x, sol
    