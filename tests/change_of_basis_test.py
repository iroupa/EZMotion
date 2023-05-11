import unittest
import numpy as np
from change_of_basis import glob_2_loc

class TestGlob2Loc(unittest.TestCase):

    def test_glob_2_loc_with_valid_input(self) -> None:
        pointP: np.ndarray = np.array([1, 2])
        origin: np.ndarray = np.array([0, 0])
        vector: np.ndarray = np.array([1, 0])
        expected_result: np.ndarray = np.array([1, 2])
        result: np.ndarray = glob_2_loc(pointP, origin, vector)
        np.testing.assert_array_almost_equal(result, expected_result, decimal=5)

if __name__ == '__main__':
    unittest.main()