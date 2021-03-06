# -*- coding: UTF-8 -*-
""":mod:`test_cumulative` tests the function that computes the momentum
of a vector in :py:func:`cumulative.momentum`. This module uses `unittest` to 
assert the correct output of the tested module.

This module can be exectuted with ``python test_cumulative.py``
"""
import unittest
import cumulative
import datetime

class TestVolatility(unittest.TestCase):
    def test_cumulative(self):
        self.assertEqual(cumulative.momentum(b), 1.7295882763433332)

b = [204.0899,203.86,203.13,199.25,199.23,198.87,198.95,200.62]

if __name__ == '__main__':
    unittest.main()
