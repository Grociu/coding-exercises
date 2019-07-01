import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from house import we_have_house

Test = EdabitTester()

Test.assert_equals(we_have_house(8, 30, 32, 8), "Yellow: 873, Gray: 242")
Test.assert_equals(we_have_house(10, 31, 30, 11), "No permission.")
Test.assert_equals(we_have_house(8, 30, 30, 8), "Yellow: 849, Gray: 234")
Test.assert_equals(we_have_house(9, 20, 18, 8), "Yellow: 581, Gray: 146")
Test.assert_equals(we_have_house(9, 14, 20, 9), "House too small.")
Test.assert_equals(we_have_house(8, 16, 12, 8), "Yellow: 353, Gray: 106")
Test.assert_equals(we_have_house(10, 25, 25, 0), "Yellow: 689, Gray: 194")
Test.assert_equals(we_have_house(8, 45, 42, 8), "House too big.")
Test.assert_equals(we_have_house(10, 40, 40, 10), "Yellow: 1569, Gray: 314")
Test.assert_equals(we_have_house(10, 15, 10, 7), "House too small.")
Test.assert_equals(we_have_house(9, 38, 36, 9), "Yellow: 1267, Gray: 290")
Test.assert_equals(we_have_house(8, 15, 12, 6), "Yellow: 303, Gray: 102")
Test.assert_equals(we_have_house(8, 30, 45, 6), "House too big.")
Test.assert_equals(we_have_house(9, 20, 14, 8), "Yellow: 525, Gray: 130")

Test.summary()
