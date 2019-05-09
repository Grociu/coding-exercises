import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from grocery import get_prices

Test = EdabitTester()

Test.assert_equals(
    get_prices(['ice cream ($5.99)', 'banana ($0.20)', 'sandwich ($8.50)',
    'soup ($1.99)']), [5.99, 0.2, 8.50, 1.99])
Test.assert_equals(get_prices(['salad ($4.99)']), [4.99])
Test.assert_equals(
    get_prices(['artichokes ($1.99)', 'rotiserrie chicken ($5.99)',
    'gum ($0.75)']), [1.99, 5.99, 0.75])
Test.assert_equals(get_prices(['pizza ($2.99)', 'shampoo ($15.75)',
'trash bags ($15.00)']), [2.99, 15.75, 15])

Test.summary()
