import unittest
import numpy as np
from update_G_vector import update_G_vector

class TestUpdateGVector(unittest.TestCase):

    def test_update_G_vector(self):
        # define initial gVector and forceVector
        gVector = np.zeros(12)
        forceVector = {1: np.array([1, 2, 3, 4]), 3: np.array([5, 6, 7, 8])}

        # calculate the expected result
        expected_gVector = np.array([1, 2, 3, 4, 0, 0, 0, 0, 5, 6, 7, 8])
        gVector = update_G_vector(gVector, forceVector)

        # compare the expected result with the actual result
        self.assertTrue(np.array_equal(gVector, expected_gVector))

    def test_update_G_vector_empty(self):
        # define initial gVector and empty forceVector
        gVector = np.zeros(12)
        forceVector = {}

        # calculate the expected result
        expected_gVector = np.zeros(12)
        gVector = update_G_vector(gVector, forceVector)

        # compare the expected result with the actual result
        self.assertTrue(np.array_equal(gVector, expected_gVector))

    def test_update_G_vector_partial(self):
        # define initial gVector and partial forceVector
        gVector = np.zeros(12)
        forceVector = {2: np.array([1, 2, 3, 4])}

        # calculate the expected result
        expected_gVector = np.array([0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 0, 0])
        gVector = update_G_vector(gVector, forceVector)

        # compare the expected result with the actual result
        self.assertTrue(np.array_equal(gVector, expected_gVector))


if __name__ == '__main__':
    unittest.main()
