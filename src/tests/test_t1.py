"""
TESTS FOR THE APP

This file contains the unit tests for the app.

To run the tests, run the following command in the terminal:
python -m unittest src/tests/test_t1.py (this will run all the tests in this file)
"""

# * To run the tests, run the following command in the terminal:
# * python -m unittest src/tests/test_t1.py (this will run all the tests in this file)

import unittest

class TestApp(unittest.TestCase):
    """
    TESTS FOR THE APP

    This class contains the unit tests for the app.
    """
    def test_is_prime(self):
        self.assertEqual(1, 1)

    def test_is_prime2(self):
        self.assertEqual(1, 1)

    def test_is_prime3(self):
        self.assertEqual(0, 1)
