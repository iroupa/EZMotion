import unittest
from read_model_loc_coords import read_model_loc_coords
import numpy as np
import os

class TestReadModelLocCoords(unittest.TestCase):

    def test_read_model_loc_coords_multiple_lines(self):
        # Test when file contains multiple lines
        data = np.array([[1, 0.1, 0.2, 0.3, 0.4],
                         [2, 0.5, 0.6, 0.7, 0.8],
                         [3, 0.9, 1, 1.1, 1.2]
                         ])

        fpath1 = 'test_model_coords_1.csv.csv'
        np.savetxt(fpath1, data, delimiter=',')

        # Call the function to get the actual output
        actual_output = read_model_loc_coords(fpath1)

        # Expected output
        expected_output1 = {
            1: [[0.1, 0.2], [0.3, 0.4]],
            2: [[0.5, 0.6], [0.7, 0.8]],
            3: [[0.9, 1.0], [1.1, 1.2]]
        }

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output1)

        # Remove '.csv' test file
        os.remove(fpath1)

    def test_read_model_loc_coords_single_line(self):
        # Test when file contains a single line
        data = np.array([[1, 0.1, 0.2, 0.3, 0.4],
                         ])

        fpath2 = 'test_model_coords_2.csv.csv'
        np.savetxt(fpath2, data, delimiter=',')

        # Call the function to get the actual output
        actual_output = read_model_loc_coords(fpath2)

        # Expected output
        expected_output = {1: [[0.1, 0.2], [0.3, 0.4]]}

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output)

        # Remove '.csv' test file
        os.remove(fpath2)

if __name__ == '__main__':
    unittest.main()
