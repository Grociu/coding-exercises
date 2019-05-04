# import unitest module
import unittest
# from tested file import tested function
from ctdn import convert_to_decimal

# create a class for the test with unique name of unittest.TestCase object
class main_test(unittest.TestCase):
    # define functions in class taking self as argument with
    # assertEqual function on tested function and value, and target value
    # name of function can hint to what exactly is being tested
    def test_1(self):
        self.assertEqual(convert_to_decimal(
        ["1%", "2%", "3%"]), [0.01, 0.02, 0.03])

    def test_2(self):
        self.assertEqual(convert_to_decimal(
            ["45%", "32%", "97%", "33%"]), [0.45, 0.32, 0.97, 0.33])

    def test_3(self):
        self.assertEqual(convert_to_decimal(
            ["33%", "98.1%", "56.44%", "100%"]), [0.33, 0.981, 0.5644, 1])

# include this so it works lol. Initializes the test.
if __name__ == '__main__':
    unittest.main()
