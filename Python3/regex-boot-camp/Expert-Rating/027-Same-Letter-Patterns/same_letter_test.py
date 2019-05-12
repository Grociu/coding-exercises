import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from same_letter import same_letter_pattern

Test = EdabitTester()

Test.assert_equals(same_letter_pattern('ABAB', 'CDCD'), True)
Test.assert_equals(same_letter_pattern('AAABBB', 'CCCDDD'), True)
Test.assert_equals(same_letter_pattern('ABCBA', 'BCDCB'), True)
Test.assert_equals(same_letter_pattern('AAAA', 'BBBB'), True)
Test.assert_equals(same_letter_pattern('BAAB', 'ABBA'), True)
Test.assert_equals(same_letter_pattern('BAAB', 'QZZQ'), True)
Test.assert_equals(same_letter_pattern('TTZZVV', 'PPSSBB'), True)
Test.assert_equals(same_letter_pattern('ZYX', 'ABC'), True)
Test.assert_equals(same_letter_pattern('AABAA', 'SSCSS'), True)
Test.assert_equals(same_letter_pattern('AABAABAA', 'SSCSSCSS'), True)
Test.assert_equals(same_letter_pattern('UBUBUBUB', 'WEWEWEWE'), True)
Test.assert_equals(same_letter_pattern('FFGG', 'FFG'), False)
Test.assert_equals(same_letter_pattern('FFGG', 'CDCD'), False)
Test.assert_equals(same_letter_pattern('FFFG', 'GGHI'), False)
Test.assert_equals(same_letter_pattern('FFFF', 'ABCD'), False)
Test.assert_equals(same_letter_pattern('ABCA', 'ABCD'), False)
Test.assert_equals(same_letter_pattern('ABCAAA', 'DDABCD'), False)

Test.summary()
