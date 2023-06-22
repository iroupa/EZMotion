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


def read_angular_driver_info(modeling_file_data):
    """

    Function compiles the information about the angular driving constraint equations of
    the multibody system.


    Parameters:
        modeling_file_data  :   numpy array
                                all information regarding the modeling of each component of the multibody system

    Returns:
        ang_drivers_info    :   dictionary
                                info (n_bodies, bodies and type of constraint) of each
                                driver of the multibody system.

    """

    ang_drivers_info = {}

    kinematic_constraint_idx = 0

    for row in modeling_file_data:
        if row[0] == 1:
            kinematic_constraint_idx += 1
        elif row[0] == 2:
            kinematic_constraint_idx += 1
            n_bodies = 2
            body_1 = int(row[1])
            body_2 = int(row[2])
            product_type = 'dot_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'body_2': body_2,
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 3:
            kinematic_constraint_idx += 1
            n_bodies = 1
            body_1 = int(row[1])
            # body_2 = 'unit_vec_dir'
            product_type = 'dot_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'unit_vec_dir': np.array([row[2], row[3]]),
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 4:
            kinematic_constraint_idx += 1
            n_bodies = 2
            body_1 = int(row[1])
            body_2 = int(row[2])
            product_type = 'cross_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'body_2': body_2,
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 5:
            kinematic_constraint_idx += 1
            n_bodies = 1
            body_1 = int(row[1])
            # body_2 = 'unit_vec_dir'
            product_type = 'cross_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'unit_vec_dir': np.array([row[2], row[3]]),
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 6:
            kinematic_constraint_idx += 2

        elif row[0] == 7:
            kinematic_constraint_idx += 1

        elif row[0] == 8:
            kinematic_constraint_idx += 2

        elif row[0] == 9:
            kinematic_constraint_idx += 2

        elif row[0] == 10:
            kinematic_constraint_idx += 2

        elif row[0] == 11:
            kinematic_constraint_idx += 2

        elif row[0] == 12:
            kinematic_constraint_idx += 1
            n_bodies = 1
            body_1 = int(row[1])
            # body_2 = 'unit_vec_dir'
            product_type = 'dot_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'unit_vec_dir': np.array([row[2], row[3]]),
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 13:
            kinematic_constraint_idx += 1
            n_bodies = 2
            body_1 = int(row[1])
            body_2 = int(row[2])
            product_type = 'dot_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'body_2': body_2,
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 14:
            kinematic_constraint_idx += 1
            n_bodies = 1
            body_1 = int(row[1])
            # body_2 = 'unit_vec_dir'
            product_type = 'cross_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'unit_vec_dir': np.array([row[2], row[3]]),
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 15:
            kinematic_constraint_idx += 1
            n_bodies = 2
            body_1 = int(row[1])
            body_2 = int(row[2])
            product_type = 'cross_idx'
            n_angular_driver = int(row[13])

            if n_angular_driver not in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver] = {'n_bodies': n_bodies,
                                                      'body_1': body_1,
                                                      'body_2': body_2,
                                                      product_type: kinematic_constraint_idx - 1
                                                      }
            elif n_angular_driver in ang_drivers_info.keys():
                ang_drivers_info[n_angular_driver].update({product_type: kinematic_constraint_idx - 1})

        elif row[0] == 16:
            kinematic_constraint_idx += 1

    return ang_drivers_info


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
