import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from bell_number import bell

Test = EdabitTester()

Test.assert_equals(bell(1), 1)
Test.assert_equals(bell(2), 2)
Test.assert_equals(bell(3), 5)
Test.assert_equals(bell(4), 15)
Test.assert_equals(bell(5), 52)
Test.assert_equals(bell(6), 203)

Test.summary()
