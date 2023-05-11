#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from assemble_C_matrix import assemble_C_matrix
import numpy as np
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splder, splev


__author__ = 'Ivo_Roupa'
__version__ = '.001'
__date__ = '2022'

def compute_moments_of_force_MC(dataConst, q, lmm, drivers_info, weight):

    trajectory_drivers_info = {}

    counter = 1
    for row in dataConst:
        # Trajectory Driver Constraint ( n = 6)
        if row[0] == 6:
            # n_trajectory_driver = str(int(row[3])) + "_" + str(int(row[4]))
            n_body = int(row[2])
            loc_coord_x = row[5]
            loc_coord_y = row[6]
            lmm_idx     = row[1]
            if n_body not in trajectory_drivers_info.keys():
                trajectory_drivers_info[n_body] =  {counter:{'n_body'     : n_body,
                                                             'loc_coord_x' : float(loc_coord_x),
                                                             'loc_coord_y' : float(loc_coord_y),
                                                             'lmm_idx'     : int(lmm_idx)}
                                                    }
            elif n_body in trajectory_drivers_info.keys():
                trajectory_drivers_info[n_body].update( {counter:{'n_body'     : n_body,
                                                                  'loc_coord_x' : float(loc_coord_x),
                                                                   'loc_coord_y' : float(loc_coord_y),
                                                                   'lmm_idx'     : int(lmm_idx)}
                                                         })
            counter += 1

    net_moments_of_force = {}

    for n_body in trajectory_drivers_info.keys():
        for trajectory_driver in trajectory_drivers_info[n_body].keys():
            trajectory_driver_net_moment_of_force = np.zeros(q.shape[0])
            for frame in range(0, q.shape[0]):

                # Obtain generalized coordinates of body of interest
                body_q_coords                               = q[frame, 4 * (n_body - 1):4 * (n_body - 1) + 4]

                # Obtain local coordinates of joint and driver point of application
                traj_driver_application_point_loc_coords    = [trajectory_drivers_info[n_body][trajectory_driver]['loc_coord_x'],
                                                               trajectory_drivers_info[n_body][trajectory_driver]['loc_coord_y']]

                joint_of_interest_loc_coords                = drivers_info[n_body]['loc_coords']

                dof_idx = drivers_info[n_body]['dof_idx']

                lmm_idx = trajectory_drivers_info[n_body][trajectory_driver]['lmm_idx']

                # Compute global coordinates of joint and driver point of application
                traj_driver_application_point_glob_coords   = assemble_C_matrix(traj_driver_application_point_loc_coords).dot(body_q_coords)
                joint_of_interest_glob_coords               = assemble_C_matrix(joint_of_interest_loc_coords).dot(body_q_coords)

                # Compute moment of force for any frame
                r = traj_driver_application_point_glob_coords - joint_of_interest_glob_coords
                F = lmm[frame, lmm_idx:lmm_idx+2]

                # Compute net_moment_of_force with rspect to joint
                trajectory_driver_net_moment_of_force[frame] = r[0]*F[1] - r[1]*F[0]

        # Assign net moment of force to angular driver dictionary
        if dof_idx not in net_moments_of_force.keys():
            net_moments_of_force[dof_idx] = trajectory_driver_net_moment_of_force/weight
        elif dof_idx in net_moments_of_force.keys():
            net_moments_of_force[dof_idx] = net_moments_of_force[dof_idx] + trajectory_driver_net_moment_of_force/weight

    header = sorted(net_moments_of_force.keys())

    net_moments_of_force_arr = np.zeros((q.shape[0] + 1, len(header)))

    net_moments_of_force_arr[0,:] = np.array(header)
    col_counter = 0
    for driver_idx in header:
        net_moments_of_force_arr[1:, col_counter] = net_moments_of_force[driver_idx]
        col_counter += 1

    return trajectory_drivers_info, net_moments_of_force_arr

if __name__ == "__main__":
    from file2dataConst import file2dataConst
    import os
    import matplotlib.pyplot as plt

    input_folder = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_5_Dynamics\Inverse_Dynamics\Experimental Data\Gait\MC_Data'
    model = r'trial_0003_10passagem'

    model_file_fpath  = os.path.join(input_folder, model,'Modeling_File.mod')
    lmm_file_fpath    = os.path.join(input_folder, model,'trial_0003_10passagem_lmm_rep.out')
    q_file_fpath      = os.path.join(input_folder, model,'trial_0003_10passagem_q_rep.out')

    drivers_info = {1:{'loc_coords':[0, -0.5], 'dof_idx':1},
                   2:{'loc_coords':[0, -0.5], 'dof_idx':2},
                   3:{'loc_coords':[0, -0.5], 'dof_idx':3},
                   4:{'loc_coords':[0, -0.5], 'dof_idx':4},
                   5:{'loc_coords':[0, -0.5], 'dof_idx':5},
                   6:{'loc_coords':[0, 0.167], 'dof_idx':6},
                   7:{'loc_coords':[0, 0.162], 'dof_idx':7},
                   8:{'loc_coords':[0, 0.174], 'dof_idx':8},
                   9:{'loc_coords':[0, 0.159], 'dof_idx':9},
                   10:{'loc_coords':[0, 0.153], 'dof_idx':10},
                   11:{'loc_coords':[0, 0.058], 'dof_idx':11},
                   12:{'loc_coords':[0, 0.062], 'dof_idx':12}
                   }

    # Initialize dataConst from '.csv' file
    dataConst = file2dataConst(model_file_fpath)
    lmm_file_data = np.loadtxt(lmm_file_fpath, dtype='float', delimiter=',')
    q_file_data = np.loadtxt(q_file_fpath, dtype='float', delimiter=',')

    trajectory_drivers_info, net_moments_of_force = compute_moments_of_force_MC(dataConst, q_file_data, lmm_file_data, drivers_info, 54)

    fig = plt.figure()

    plt.subplot(3, 1, 1)
    plt.plot(-net_moments_of_force[55:156,7])
    # plt.xlim([0,101])
    # plt.ylim([-1,1])

    plt.subplot(3, 1, 2)
    plt.plot(-net_moments_of_force[55:156,9])
    plt.xlim([0,101])
    # plt.ylim([-1,1])

    plt.subplot(3, 1, 3)
    plt.plot(-net_moments_of_force[55:156,11])
    plt.xlim([0,101])
    # plt.ylim([-0.5,2])

    plt.show()

    a = 1