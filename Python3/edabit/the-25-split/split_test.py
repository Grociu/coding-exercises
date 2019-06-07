import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from split import split

Test = EdabitTester()

Test.assert_equals(split(25), 8748)
Test.assert_equals(split(1), 1)
Test.assert_equals(split(10), 36)
Test.assert_equals(split(5), 6)
Test.assert_equals(split(15), 243)
Test.assert_equals(split(20), 1458)

Test.summary()
