import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from rgb import valid_color

Test = EdabitTester()

# True Tests
Test.assert_equals(valid_color('rgb(0,0,0)'), True, 'rgb lowest valid numbers')
Test.assert_equals(
    valid_color('rgb(255,255,255)'), True, 'rgb highest valid numbers')
Test.assert_equals(
    valid_color('rgba(0,0,0,0)'), True, 'rgba lowest valid numbers')
Test.assert_equals(
    valid_color('rgba(255,255,255,1)'), True, 'rgba highest valid numbers')
Test.assert_equals(
    valid_color('rgba(0,0,0,0.123456789)'),
    True, 'alpha can have many decimals')
Test.assert_equals(valid_color(
    'rgba(0,0,0,.8)'), True, 'in alpha the number before the dot is optional')
Test.assert_equals(valid_color(
    'rgba(	0 , 127	, 255 , 0.1	)'),
    True, 'whitespace is allowed around numbers (even tabs)')
Test.assert_equals(
    valid_color('rgb(0%,50%,100%)'), True, 'numbers can be percentages')

# False Tests
Test.assert_equals(valid_color('rgb(0,,0)'), False, 'INVALID: missing number')
Test.assert_equals(
    valid_color('rgb (0,0,0)'),
    False, 'INVALID: whitespace before parenthesis')
Test.assert_equals(
    valid_color('rgb(0,0,0,0)'), False, 'INVALID: rgb with 4 numbers')
Test.assert_equals(
    valid_color('rgba(0,0,0)'), False, 'INVALID: rgba with 3 numbers')
Test.assert_equals(
    valid_color('rgb(-1,0,0)'), False, 'INVALID: numbers below 0')
Test.assert_equals(
    valid_color('rgb(255,256,255)'), False, 'INVALID: numbers above 255')
Test.assert_equals(
    valid_color('rgb(100%,100%,101%)'), False, 'INVALID: numbers above 100%')
Test.assert_equals(
    valid_color('rgba(0,0,0,-1)'), False, 'INVALID: alpha below 0')
Test.assert_equals(
    valid_color('rgba(0,0,0,1.1)'), False, 'INVALID: alpha above 1')

Test.summary()
