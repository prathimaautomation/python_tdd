# Test Driven Development TDD

```python
- Let's dive into coding
- we have already completed step 1 and 2
- Let's create a file called calc_test.py
- we will use 'unittest' and 'pytest'
- 'pip install'
- 'python -m unittest'
- 'python -m unittest discover -v'

## calc_test.py
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
## simple_calc.py
class SimpleCalc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2
```

```python
Output when we run in Terminal using python -m pytest:
========================================== test session starts ===========================================
platform win32 -- Python 3.8.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Medha\PycharmProjects\python_tdd
collected 4 items
calc_test.py ....                                                                                   [100%]
=========================================== 4 passed in 0.11s ============================================
```