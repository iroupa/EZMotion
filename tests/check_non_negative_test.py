import unittest
from unittest.mock import MagicMock
import wx
from check_non_negative import check_non_negative

class TestCheckNonNegative(unittest.TestCase):
    def setUp(self):
        self.widget_input_positive = MagicMock(return_value='10')
        self.widget_input_negative = MagicMock(return_value='-10')
        self.msg = 'Input cannot be negative'

    def test_positive_input(self):
        res = check_non_negative(self.widget_input_positive, self.msg)
        self.assertTrue(res)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            check_non_negative(self.widget_input_negative, self.msg)
            wx.MessageBox.assert_called_once_with(self.msg, 'Error', wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    unittest.main()
