import unittest
import numpy as np
from assemble_mass_matrix import assemble_mass_matrix


class TestAssembleMassMatrix(unittest.TestCase):

    def setUp(self):
        # Define sample input parameters
        self.nBodies = 1
        self.dataConst = np.array([[1, 0, 1, 0, 1.0, 1.0, 2.0, 3.0, 4.0, 0, 0, 0, 0, 0],
                                   [3, 4, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                                   [5, 3, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                                   [8, 1, 1, 0, 0, 0, -1, 0.0, 0, 0, 0, 0, 0, 0]])

        self.inertial_parameters = {
            1: {'Mass': 1, 'Moment_Inertia': 2.0, 'CoM_LocCoordX': 3.0, 'CoM_LocCoordY': 4.0}}

    def test_assemble_mass_matrix(self):
        expected_output = np.array([
            [1.0, 0, 3, 4],
            [0, 1.0, -4, 3],
            [3, -4, 2.0, 0],
            [4, 3, 0, 2.0]])

        # Call the function to get the actual output
        actual_output = assemble_mass_matrix(self.nBodies, self.dataConst, self.inertial_parameters)

        # Assert that the actual output matches the expected output
        self.assertTrue(np.allclose(actual_output, expected_output))

if __name__ == '__main__':
    unittest.main()
