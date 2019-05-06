import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from split_codes import split_code

Test = EdabitTester()

Test.assert_equals(split_code("TEWA8392"), ["TEWA", 8392])
Test.assert_equals(split_code("MMU778"), ["MMU", 778])
Test.assert_equals(split_code("SRPE5532"), ["SRPE", 5532])
Test.assert_equals(split_code("SKU8977"), ["SKU", 8977])
Test.assert_equals(split_code("MCI5589"), ["MCI", 5589])
Test.assert_equals(split_code("WIEB3921"), ["WIEB", 3921])

Test.summary()