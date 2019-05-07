import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from correct_sign import correct_signs

Test = EdabitTester()

Test.assert_equals(correct_signs("3 < 7 < 11"), True)
Test.assert_equals(correct_signs("13 > 44 > 33 > 1"), False)
Test.assert_equals(correct_signs("1 < 2 < 6 < 9 > 3"), True)
Test.assert_equals(correct_signs("4 > 3 > 2 > 1"), True)
Test.assert_equals(correct_signs("5 < 7 > 1"), True)
Test.assert_equals(correct_signs("5 > 7 > 1"), False)
Test.assert_equals(correct_signs("9 < 9"), False)

Test.summary()