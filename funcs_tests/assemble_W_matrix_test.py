import numpy as np
import unittest
from assemble_W_matrix import assemble_W_matrix
import os

class TestAssembleWMatrix(unittest.TestCase):

    def test_assemble_W_matrix(self):

        # Define test inputs
        dataConst = np.array([[6, 0, 1, 2, 0, 0, 0]])
        dPhidq = np.array([[1, 0, 0], [0, 1, 0]])
        trajectory_drivers_weight = 0.1

        # Call the function to be tested
        W = assemble_W_matrix(dataConst, dPhidq, trajectory_drivers_weight)

        # Define expected output
        expected_output = np.array([[1., 0.], [0., 1.]])

        # Compare the actual and expected output
        np.testing.assert_allclose(W, expected_output, atol=1e-10)

if __name__ == '__main__':
    unittest.main()
