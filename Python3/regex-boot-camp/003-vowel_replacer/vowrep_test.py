# import unitest module
import unittest
# from tested file import tested function
from vowrep import replace_vowels

# create a class for the test with unique name of unittest.TestCase object
class main_test(unittest.TestCase):
    # define functions in class taking self as argument with
    # assertEqual function on tested function and value, and target value
    # name of function can hint to what exactly is being tested
      
    def test_1(self):
        self.assertEqual(
            replace_vowels("the aardvark", "#"), "th# ##rdv#rk")

    def test_2(self):
        self.assertEqual(
            replace_vowels("minnie mouse", "?"), "m?nn?? m??s?")

    def test_3(self):
        self.assertEqual(
            replace_vowels("shakespeare", "*"), "sh*k*sp**r*")
    
    def test_4(self):
        self.assertEqual(
            replace_vowels("all is fair in love and war", "<"),
                "<ll <s f<<r <n l<v< <nd w<r")
    
# include this so it works lol. Initializes the test.
if __name__ == '__main__':
    unittest.main()
