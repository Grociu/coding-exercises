import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from collatz import collatz

Test = EdabitTester()

Test.assert_equals(collatz(1), [0, 1])
Test.assert_equals(collatz(3), [7, 16])
Test.assert_equals(collatz(9), [19, 52])
Test.assert_equals(collatz(27), [111, 9232])
Test.assert_equals(collatz(81), [22, 244])

Test.summary()
