# import unitest module
import unittest
# from tested file import tested function
from pvss import is_prefix, is_suffix

# create a class for the test with unique name of unittest.TestCase object
class main_test(unittest.TestCase):
    # define functions in class taking self as argument with
    # assertEqual function on tested function and value, and target value
    # name of function can hint to what exactly is being tested
    def test_1(self):
        self.assertEqual(
            is_prefix("automation", "auto-"), True)

    def test_2(self):
        self.assertEqual(
            is_suffix("arachnophobia", "-phobia"), True)

    def test_3(self):
        self.assertEqual(
            is_prefix("retrospect", "sub-"),  False)
    
    def test_4(self):
        self.assertEqual(
            is_suffix("vocation", "-logy"),  False)
    
    def test_5(self):
        self.assertEqual(
            is_prefix('superfluous', 'super-'), True)

    def test_6(self):
        self.assertEqual(
            is_prefix('oration', 'mega-'), False)

    def test_7(self):
        self.assertEqual(
            is_suffix('rhinoplasty', '-plasty'),  True)

    def test_8(self):
        self.assertEqual(
            is_suffix('movement', '-scope'), False)
    
    def test_9_suffix_is_inside(self):
        self.assertEqual(
            is_suffix('movement', '-ve'), False)
    
    def test_10_prefix_is_inside(self):
        self.assertEqual(
            is_prefix('oration', 'ra-'), False)
    

# include this so it works lol. Initializes the test.
if __name__ == '__main__':
    unittest.main()
