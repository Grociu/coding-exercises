import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from complete_the_word import can_complete

Test = EdabitTester()

Test.assert_equals(can_complete('butl', 'beautiful'), True)
Test.assert_equals(
    can_complete('butlz', 'beautiful'), False,
    "'z' does not exist in the word `beautiful`")
Test.assert_equals(
    can_complete('tulb', 'beautiful'), False,
    "although 't', 'u', 'l' and 'b' incorrectly ordered")
Test.assert_equals(
    can_complete('bbutl', 'beautiful'), False,
    "too many 'b's, beautiful has only 1")
Test.assert_equals(can_complete('sg', 'something'), True)
Test.assert_equals(can_complete('sgi', 'something'), False, "out of order")
Test.assert_equals(can_complete('sing', 'something'), True)
Test.assert_equals(can_complete('siing', 'something'), False, "too many i's")

Test.summary()
