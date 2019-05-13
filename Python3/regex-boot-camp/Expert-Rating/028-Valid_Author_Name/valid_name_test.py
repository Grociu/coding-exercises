import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from valid_name import valid_name

Test = EdabitTester()

Test.assert_equals(valid_name("H. Wells"), True)
Test.assert_equals(valid_name("H. G. Wells"), True)
Test.assert_equals(valid_name("Herbert G. Wells"), True)
Test.assert_equals(valid_name("Herbert George Wells"), True)
Test.assert_equals(valid_name("Herbert"), False, 'Name must be 2 or 3 words.')
Test.assert_equals(
    valid_name("Herbert W. G. Wells"), False, 'Name must be 2 or 3 words')
Test.assert_equals(valid_name("h. Wells"), False, 'Incorrect Capitalization.')
Test.assert_equals(
    valid_name("herbert G. Wells"), False, 'Incorrect Capitalization.')
Test.assert_equals(
    valid_name("H Wells"), False, 'Initials must end with a dot.')
Test.assert_equals(
    valid_name("Herb. Wells"), False, 'Words cannot end with a dot.')
Test.assert_equals(
    valid_name("H. George Wells"),
    False, 'First name is initial but middle name is word.')
Test.assert_equals(
    valid_name("Herbert George W."), False, 'Last name cannot be an initial.')

Test.summary()
