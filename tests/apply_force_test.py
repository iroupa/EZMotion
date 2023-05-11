import unittest
import numpy as np
from typing import List
from applyForce import applyForce

class TestApplyForce(unittest.TestCase):

    def test_check_output_shape(self):
        force = np.array([3.0, 4.0])
        locCoords = [1.0, 1.0]
        result = applyForce(force, locCoords)
        assert result.shape == (4,)

    def test_apply_force(self):
        force = np.array([3.0, 4.0])
        locCoords = [1.0, 1.0]
        expected_result = np.array([3.0, 4.0, 7.0, 1.0])
        result = applyForce(force, locCoords)
        np.testing.assert_allclose(result, expected_result)

if __name__ == '__main__':
    unittest.main()


