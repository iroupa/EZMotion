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

from scipy.interpolate import splev


def updateDataConst(time, dataConst, func, nConstrainByType, dofType):
    """
    
    Update dataConst every iteration

    Parameters:
        time                :   float64
                                Time instant at which each driver and respective derivatives will be evaluated
        dataConst           :   numpy.ndarray
                                Numpy array to be updated
        func                :   dictionary
                                Dictionary with each driver name and respective knots, coefficients and spline order
                                for spline data and first and second spline derivatives
        nConstrainByType    :   int
                                number of constraint by type
        dofType			    :   int
                                type of degree of freedom (0 - angular | 1 - trajectory)

    Returns:
        dataConst           :   numpy.ndarray
                                Updated dataConst after each iteration

    """

    # Check for angular driver (dofType == 0)
    if int(dofType) == 0:
        dof = int(dataConst[nConstrainByType, 13])

        if dof != 0:
            # Calculate new position value, based on spline interpolation,
            # and update respective dataConst row and col
            dataConst[nConstrainByType, 6] = splev(time, func[dof]['splPos'], der=0)

            # Calculate new velocity value, based on spline interpolation,
            # and update respective dataConst row and col
            dataConst[nConstrainByType, 7] = splev(time, func[dof]['splVel'], der=0)

            # Calculate new acceleration value, based on spline interpolation,
            # and update respective dataConst row and col
            dataConst[nConstrainByType, 8] = splev(time, func[dof]['splAcc'], der=0)
        return dataConst

    # Check for trajectory driver (dofType == 1)
    elif int(dofType) == 1:

        # 'X' component
        dof = int(dataConst[nConstrainByType, 2])

        # Calculate new position value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 6] = splev(time, func[dof]['splPos'], der=0)

        # Calculate new velocity value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 8] = splev(time, func[dof]['splVel'], der=0)

        # Calculate new acceleration value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 10] = splev(time, func[dof]['splAcc'], der=0)

        # 'Y' component
        dof = int(dataConst[nConstrainByType, 3])

        # Calculate new position value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 7] = splev(time, func[dof]['splPos'], der=0)

        # Calculate new velocity value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 9] = splev(time, func[dof]['splVel'], der=0)

        # Calculate new acceleration value, based on spline interpolation, and update respective dataConst row and col
        dataConst[nConstrainByType, 11] = splev(time, func[dof]['splAcc'], der=0)

        return dataConst
    else:
        raise


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
