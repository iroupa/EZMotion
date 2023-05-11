import unittest
import numpy as np
from read_inertial_parameters import read_inertial_parameters
import os

class TestReadInertialParameters(unittest.TestCase):
    def test_read_inertial_parameters(self):
        # Create a temporary file with inertial parameter data for testing
        data = np.array([[1, 2.0, 1.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0],
                        [1, 12.0, 2.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0],
                        [1, 0.20, 3.0, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.10, 0.11, 0.12, 0.13, 0.14]
                         ])

        file_path = 'test_inertial_parameters.csv'
        np.savetxt(file_path, data, delimiter=',')

        # Call the function to read the data from the temporary file
        result = read_inertial_parameters(file_path)

        # Check that the result matches the expected output
        expected_output = {1: {'Mass': 6.0, 'Moment_Inertia': 7.0, 'CoM_LocCoordX': 8.0, 'CoM_LocCoordY': 9.0},
                           2: {'Mass': 16.0, 'Moment_Inertia': 17.0, 'CoM_LocCoordX': 18.0, 'CoM_LocCoordY': 19.0},
                           3: {'Mass': 0.60, 'Moment_Inertia': 0.7, 'CoM_LocCoordX': 0.80, 'CoM_LocCoordY': 0.90}}

        self.assertEqual(result, expected_output)

        # Remove the temporary file
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
