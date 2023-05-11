import unittest
import numpy as np
from read_model_q import read_model_q

class TestReadModelQ(unittest.TestCase):

    def test_read_model_q(self):
        # create a test file
        test_file = 'test_q.txt'
        with open(test_file, 'w') as f:
            f.write('1.0,2.0,3.0\n4.0,5.0,6.0\n')

        # test the function with the test file
        expected_q = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype='f')
        q = read_model_q(test_file)
        self.assertTrue(np.array_equal(q, expected_q))

        # remove the test file
        import os
        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
