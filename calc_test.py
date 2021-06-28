# let's import unittest and pytest as these are the dependencies and run

import unittest
import pytest

from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

# assertions to write our test cases
# we will use our basic calculator example to write the tests first then the code

    def test_add(self):
        # Naming convention is essential to have test in the name of our method
        self.assertEqual(self.calc.add(3,2), 5) #if True test would pass
        #return num1 + num2

    def test_substract(self):
        self.assertEqual(self.calc.subtract(8, 5), 3) # 8 - 5 = 3

    def test_multi(self):
        self.assertEqual(self.calc.multiply(2, 3), 6) # 2 * 3 = 6

    def test_div(self):
        self.assertEqual(self.calc.divide(6, 3), 2) # 6 / 3 = 2



