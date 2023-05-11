import unittest
import wx
from check_smaller_equal import check_smaller_equal

class TestCheckSmallerEqual(unittest.TestCase):
    def setUp(self):
        app = wx.App()

        self.widget1 = wx.TextCtrl(parent=None, id=-1)
        self.widget2 = wx.TextCtrl(parent=None, id=-1)

    def test_widget1_smaller(self):
        self.widget1.SetValue('1')
        self.widget2.SetValue('2')
        self.assertTrue(check_smaller_equal(self.widget1, self.widget2))
        self.assertEqual(self.widget1.GetBackgroundColour(), (255, 255, 255))
        self.assertEqual(self.widget2.GetBackgroundColour(), (255, 255, 255))

    def test_widget1_larger(self):
        self.widget1.SetValue('2')
        self.widget2.SetValue('1')
        self.assertFalse(check_smaller_equal(self.widget1, self.widget2))
        self.assertEqual(self.widget1.GetBackgroundColour(), "pink")
        self.assertEqual(self.widget2.GetBackgroundColour(), "pink")

    def tearDown(self):
        self.widget1.Destroy()
        self.widget2.Destroy()

if __name__ == '__main__':
    unittest.main()
