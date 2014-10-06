" Module demonstrating different ways to create function-like things in Python"

__author__ = 'ijstokes'

# 1. function
def adder(a, b):
    " simple demonstration of function to perform addition"
    return a + b

# 2. lambda (anonymous, single expression function object)
adder_lambda = lambda a, b: a + b

# 3. class (with callable instances)
class Adder:
    """ Creates objects that can be called, and when called require two
        arguments that will be added together.
    """
    def __call__(self, a, b):
        return a + b