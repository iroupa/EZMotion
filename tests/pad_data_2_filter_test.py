import unittest
import numpy as np
from pad_data_2_filter import pad_signal

class TestPadSignal(unittest.TestCase):

    def test_pad_signal(self):
        # Test case 1: signal padding with start and end indices
        signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        slope_frames = 2
        start_idx = 2
        end_idx = 4
        nPads_begin = 1
        nPads_end = 2

        # Call the function to get the actual output
        actual_output = pad_signal(signal, slope_frames, start_idx, end_idx, nPads_begin, nPads_end)
        print(actual_output)

        # # Expected output
        # expected_output = np.array([1.0, 1.75, 2.5, 3.0, 4.0, 5.0, 5.75, 6.5])
        #
        # # Assert that the actual output matches the expected output
        # np.testing.assert_allclose(actual_output, expected_output)

        # # Test case 2: signal padding with start and end indices, with smaller slope frames
        # signal = np.array([1, 2, 3, 4, 5, 6])
        # slope_frames = 1
        # start_idx = 2
        # end_idx = 4
        # nPads_begin = 1
        # nPads_end = 2
        # expected_output = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 5.5, 6.0])
        # np.testing.assert_array_almost_equal(pad_signal(signal, slope_frames, start_idx, end_idx, nPads_begin, nPads_end), expected_output)
        #
        # # Test case 3: signal padding with start and end indices, with larger slope frames
        # signal = np.array([1, 2, 3, 4, 5, 6])
        # slope_frames = 3
        # start_idx = 1
        # end_idx = 5
        # nPads_begin = 1
        # nPads_end = 2
        # expected_output = np.array([0.333, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 6.667])
        # np.testing.assert_array_almost_equal(pad_signal(signal, slope_frames, start_idx, end_idx, nPads_begin, nPads_end), expected_output)

if __name__ == '__main__':
    unittest.main()
