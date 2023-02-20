# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:38:45 2023

@author: user
"""

import unittest
import exceptions as ex

class TestDivisionMethod(unittest.TestCase):

    def test_normalDivision(self):
        self.assertEqual(ex.division(5), 20.0)

    def test_typeError(self):
        self.assertEqual(ex.division("sss"), "TypeError")

    def test_divisionByZero(self):
        self.assertEqual(ex.division(0), "ZeroDivisionError")


if __name__ == '__main__':
    unittest.main()