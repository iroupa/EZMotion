import unittest
import numpy as np
from read_inertial_parameters import read_inertial_parameters
import os

class TestReadInertialParameters(unittest.TestCase):

    def test_read_inertial_parameters_single_body(self):
        dataConst = np.array([[1, 0, 1, 0, 1.0, 1.0, 2.0, 3.0, 4.0, 0, 0, 0, 0, 0],
                         [3, 4, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                         [5, 3, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                         [8, 1, 1, 0, 0, 0, -1, 0.0, 0, 0, 0, 0, 0, 0]]
                        )

        # Define input file path
        fpath = 'test_inertial_parameters.csv'
        np.savetxt(fpath, dataConst, delimiter=',')

        # Define expected result
        expected_result = {1: {'Mass': 1.0, 'Moment_Inertia': 2.0, 'CoM_LocCoordX': 3.0, 'CoM_LocCoordY': 4.0},
                           }

        # Calculate the actual result
        actual_result = read_inertial_parameters(fpath)

        # Compare the expected result with the actual result
        self.assertDictEqual(actual_result, expected_result)

        # Remove '.csv' test file
        os.remove(fpath)

    def test_read_inertial_parameters_2_bodies(self):
        dataConst = np.array([[1, 0, 1, 0, 1.0, 1.0, 2.0, 3.0, 4.0, 0, 0, 0, 0, 0],
                         [3, 4, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                         [5, 3, 1, 0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0, 0, 0, 1],
                         [8, 1, 1, 0, 0, 0, -1, 0.0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 2, 0, 1.0, 0.1, 0.2, 0.3, 0.4, 0, 0, 0, 0, 0]])


        # Define input file path
        fpath = 'test_inertial_parameters2.csv'
        np.savetxt(fpath, dataConst, delimiter=',')

        # Define expected result
        expected_result = {1: {'Mass': 1.0, 'Moment_Inertia': 2.0, 'CoM_LocCoordX': 3.0, 'CoM_LocCoordY': 4.0},
                           2: {'Mass': 0.1, 'Moment_Inertia': 0.2, 'CoM_LocCoordX': 0.3, 'CoM_LocCoordY': 0.4}
                           }

        # Calculate the actual result
        actual_result = read_inertial_parameters(fpath)

        # Compare the expected result with the actual result
        self.assertDictEqual(actual_result, expected_result)

        # Remove '.csv' test file
        os.remove(fpath)


if __name__ == '__main__':
    unittest.main()
