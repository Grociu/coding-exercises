# import unitest module
import unittest
# from tested file import tested function
from valid_zipcode import is_valid

# create a class for the test with unique name of unittest.TestCase object
class zipcode_test(unittest.TestCase):
    # define functions in class taking self as argument with
    # assertEqual function on tested function and value, and target value
    # name of function can hint to what exactly is being tested
    def test_1(self):
        self.assertEqual(is_valid("49001"), True)

    def test_2(self):
        self.assertEqual(is_valid("853a7"), False)

    def test_3(self):
        self.assertEqual(is_valid("732 32"), False)

    def test_4(self):
        self.assertEqual(is_valid("1  34 99"), False)
    
    def test_5(self):
        self.assertEqual(is_valid("19923"), True)

    def test_6(self):
        self.assertEqual(is_valid("aabcd"), False)
    
    def test_7(self):
        self.assertEqual(is_valid("a8887"), False)
    
    def test_8(self):
        self.assertEqual(is_valid("a923b"), False)
    
    def test_9(self):
        self.assertEqual(is_valid("88231"), True)

# include this so it works lol. Initializes the test.
if __name__ == '__main__':
    unittest.main()
