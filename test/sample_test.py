# -*- coding:utf-8 -*-
import unittest
from sample import Calc

class TestSample(unittest.TestCase) :
    def test_sample (self) :
        calc = Calc()
        self.assertEquals(15, calc.add(10, 5))

def suite() :
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestSample))
    return suite
