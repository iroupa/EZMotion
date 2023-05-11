import unittest
import numpy as np
from scipy import interpolate
from interpolate_signal import interpolate_1D_data

class TestInterpolation(unittest.TestCase):

    def setUp(self):
        self.x = np.arange(0, 10, 1)
        self.y = np.sin(self.x)
        self.nPoints = 20

    def test_interpolation(self):
        ynew = interpolate_1D_data(self.y, self.nPoints)
        self.assertEqual(ynew.shape[0], self.nPoints)

if __name__ == '__main__':
    unittest.main()
