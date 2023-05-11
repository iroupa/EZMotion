import unittest
import os

# Define a test loader
loader = unittest.TestLoader()

# Discover all the tests in the current directory
start_dir = r'C:\Documentos\Ivo\PhD\Thesis\All_Chapters\Chapter_8_EZ_Motion_2D\funcs_test_files'
suite = loader.discover(start_dir, pattern='*_test.py')

# Define a test runner and run the tests
runner = unittest.TextTestRunner()
result = runner.run(suite)
