__author__ = 'ijstokes'

# 1. Import the module we want to test
import functions

# 2. Import unittest
import unittest

# 3. Create a class that subclasses TestCase to encapsulate a set of tests
class TestFunctions(unittest.TestCase):

    # 4. Create methods whose names are prefixed with "test_"
    def test_adder(self):
        # 5. Exercise the function under test
        result = functions.adder(2,3)
        # 6. Assert some expected condition or result
        self.assertEqual(result, 5)

    def test_lambda(self):
        result = functions.adder_lambda(10, 20)
        self.assertEqual(result, 30)

    def test_class(self):
        " a test case for the Class-based function "
        pass

    def test_partial(self):
        result = functions.add10(7)
        self.assertEqual(result, 17)

# 7. (optional) for convenience, make the testing module "runnable", to run
#    all the tests in this module.
if __name__ == '__main__':
    unittest.main()