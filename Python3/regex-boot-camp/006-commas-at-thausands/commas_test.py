import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from commas import format_num 

Test = EdabitTester()

Test.assert_equals(format_num(1000), "1,000")
Test.assert_equals(format_num(1000000), "1,000,000")
Test.assert_equals(format_num(20), "20")
Test.assert_equals(format_num(0), "0")
Test.assert_equals(format_num(12948), "12,948")
Test.assert_equals(format_num(100000), "100,000")
Test.assert_equals(format_num(100), "100")

Test.summary()