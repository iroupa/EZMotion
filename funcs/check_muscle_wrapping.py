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

def check_muscle_wrapping(P, S, r, direction):
    """
	Function checks if muscle wrapping between two points occurs.
	
    Parameters:
        P:          list
                    cartesian coordinates of the last muscle point before the obstacle
        S:          list
                    cartesian coordinates of the first muscle point after the obstacle
        r:          float
                    obstacle radius
        direction:   string
                    obstacle radius

    Returns:
        Q:          list
                    cartesian coordinates of the proximal contact point of the muscle before the obstacle
        T:          list
                    cartesian coordinates of the distal contact point of the muscle before the obstacle
		wrapping:   boolean
					True if wrapping occurs or False if wrapping does not occur
    """

    Px, Py = P[0], P[1]
    Sx, Sy = S[0], S[1]

    if direction.lower() == 'cw':
        r = r
    elif direction.lower() == 'ccw':
        r = -r

    Qx =  (Px*r**2 + r*Py*(Px**2 + Py**2 - r**2)**0.5)/(Px**2 + Py**2)
    Qy =  (Py*r**2 - r*Px*(Px**2 + Py**2 - r**2)**0.5)/(Px**2 + Py**2)
    Q = [Qx, Qy]

    Tx =  (Sx*r**2 - r*Sy*(Sx**2 + Sy**2 - r**2)**0.5)/(Sx**2 + Sy**2)
    Ty =  (Sy*r**2 + r*Sx*(Sx**2 + Sy**2 - r**2)**0.5)/(Sx**2 + Sy**2)
    T = [Tx, Ty]

    if r*(Qx*Ty - Qy*Tx) > 0:
        wrapping = False
    if r*(Qx * Ty - Qy * Tx) < 0:
        wrapping = True

    return Q, T, wrapping

if __name__ == "__main__":
    import doctest
	
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)