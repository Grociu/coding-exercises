# import unitest module
import unittest
# from tested file import tested function
from pinv import is_valid_PIN

# create a class for the test with unique name of unittest.TestCase object
class main_test(unittest.TestCase):
    # define functions in class taking self as argument with
    # assertEqual function on tested function and value, and target value
    # name of function can hint to what exactly is being tested
      
    def test_1_4digits(self):
        self.assertEqual(
            is_valid_PIN("1234"), True)

    def test_2_5digits(self):
        self.assertEqual(
            is_valid_PIN("12345"), False)

    def test_3_letter(self):
        self.assertEqual(
            is_valid_PIN("a234"), False)
    
    def test_4_empty_string(self):
        self.assertEqual(
            is_valid_PIN(""), False)
      
    def test_5_percentage(self):
        self.assertEqual(
            is_valid_PIN("%234"), False)

    def test_6_quotes(self):
        self.assertEqual(
            is_valid_PIN("`234"), False)

    def test_7_sharp(self):
        self.assertEqual(
            is_valid_PIN("#234"), False)
    
    def test_8_dollar(self):
        self.assertEqual(
            is_valid_PIN("$234"), False)

    def test_9_asterisk(self):
        self.assertEqual(
            is_valid_PIN("*234"), False)

    def test_10(self):
        self.assertEqual(
            is_valid_PIN("5678"), True)

    def test_11(self):
        self.assertEqual(
            is_valid_PIN("^234"), False)
    
    def test_12(self):
        self.assertEqual(
            is_valid_PIN("(234"), False)

    def test_13_parenthesis(self):
        self.assertEqual(
            is_valid_PIN(")234"), False)

    def test_14_6digits(self):
        self.assertEqual(
            is_valid_PIN("123456"), True)

    def test_15_minus(self):
        self.assertEqual(
            is_valid_PIN("-234"), False)

    def test_16_underscore(self):
        self.assertEqual(
            is_valid_PIN("_234"), False)
    
    def test_17_plus(self):
        self.assertEqual(
            is_valid_PIN("+234"), False)
    
    def test_18_equal(self):
        self.assertEqual(
            is_valid_PIN("=234"), False)
    
    def test_19_question_mark(self):
        self.assertEqual(
            is_valid_PIN("?234"), False)
    
# include this so it works lol. Initializes the test.
if __name__ == '__main__':
    unittest.main()
