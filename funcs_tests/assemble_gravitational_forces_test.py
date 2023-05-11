import unittest
from assemble_gravitational_forces import assemble_gravitational_forces
import numpy as np

class TestAssembleGravitationalForces(unittest.TestCase):

    def test_assemble_gravitational_forces(self):
        # Define test input values
        dataConst = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 2, 0, 0, 0, 0, 0, 0], [1, 3, 3, 0, 0, 0, 0, 0, 0]]
        inertial_parameters = {1: {'Mass': 1.0, 'Moment_Inertia': 1.0, 'CoM_LocCoordX': 0.0, 'CoM_LocCoordY': 0.0},
                               2: {'Mass': 2.0, 'Moment_Inertia': 2.0, 'CoM_LocCoordX': 0.0, 'CoM_LocCoordY': 0.0},
                               3: {'Mass': 3.0, 'Moment_Inertia': 3.0, 'CoM_LocCoordX': 0.0, 'CoM_LocCoordY': 0.0}}

        expected_output = {1: [0, -9.81, 0, 0], 2: [0, -19.62, 0, 0], 3: [0, -29.43, 0, 0]}

        # Call function to get actual output
        actual_output = assemble_gravitational_forces(dataConst, inertial_parameters)

        # Compare the expected and actual output
        for key in expected_output:
            np.testing.assert_allclose(actual_output[key], expected_output[key])

if __name__ == '__main__':
    unittest.main()
