import unittest

from letter_checker import letter_check

class main_test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(letter_check(["trances", "nectar"]), True)
    
    def test_2(self):
        self.assertEqual(letter_check(["THE EYES", "they see"]), True)
    
    def test_3(self):
        self.assertEqual(letter_check(["assert", "staring"]), False)
    
    def test_4(self):
        self.assertEqual(letter_check(["arches", "later"]), False)
    
    def test_5(self):
        self.assertEqual(letter_check(["dale", "caller"]), False)
    
    def test_6(self):
        self.assertEqual(letter_check(["parses", "parsecs"]), False)
    
    def test_7(self):
        self.assertEqual(letter_check(["replays", "adam"]), False)
    
    def test_8(self):
        self.assertEqual(letter_check(["mastering", "streaming"]), True)
    
    def test_9(self):
        self.assertEqual(letter_check(["drapes", "compadres"]), False)
    
    def test_10(self):
        self.assertEqual(letter_check(["deltas", "slated"]), True)

if __name__ == '__main__':
    unittest.main()