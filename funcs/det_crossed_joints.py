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

def det_crossed_joints(muscle_info):
    """

    Function identifies the joints of the biomechanical model crossed by muscles.

    Parameters
    muscle_info         :   dictionary
                            muscle parameters database (fo, alfa, lo, lt, points) of the biomechanical model

    Return
                        :   list os lists
                            number of the bodies that define the joints crossed by muscles
    """
    crossed_joint = []

    # Update through all joints of the model (joints_info)
    for muscle_idx in range(0, len(muscle_info.keys())):
        muscle_bodies = []
        muscle_via_points = [x for x in muscle_info[muscle_idx].keys() if x.startswith('vp') ]
        origin_body = muscle_info[muscle_idx]['origin']['body']
        insertion_body = muscle_info[muscle_idx]['insertion']['body']
        muscle_bodies.append(origin_body)
        muscle_bodies.append(insertion_body)
        for via_point in muscle_via_points:
            muscle_bodies.append(muscle_info[muscle_idx][via_point]['body'])
        muscle_bodies = sorted(list(set(muscle_bodies)))
        if len(muscle_bodies) == 2:
            crossed_joint.append(muscle_bodies)
        elif len(muscle_bodies) > 2:
            for _ in range(0, len(muscle_bodies) - 1):
                crossed_joint.append([muscle_bodies[_], muscle_bodies[_ + 1]])

    return [*map(list, {*map(tuple, crossed_joint)})]

if __name__ == "__main__":
    import doctest
        
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)