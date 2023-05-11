import unittest
import numpy as np
from assemble_C_matrix import assemble_C_matrix

class TestAssembleCMatrix(unittest.TestCase):

    def test_assemble_c_matrix_with_valid_input(self):
        localCoordinates = [1.0, 2.0]
        expected_result = np.array([[1, 0, 1.0, -2.0], [0, 1, 2.0, 1.0]])
        result = assemble_C_matrix(localCoordinates)
        np.testing.assert_allclose(result, expected_result)

    def test_assemble_c_matrix_output_shape(self):
        localCoordinates = [1.0, 2.0]
        result = assemble_C_matrix(localCoordinates)
        assert result.shape == (2,4)

if __name__ == '__main__':
    unittest.main()