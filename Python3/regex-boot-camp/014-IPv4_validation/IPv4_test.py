import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from IPv4 import is_valid

Test = EdabitTester()

Test.assert_equals(
    is_valid("12.255.56.1"), True, "This is a valid IPv4")
Test.assert_equals(
    is_valid("1.2.3.4"), True, "This is a valid IPv4")
Test.assert_equals(
    is_valid("1.2.3"), False, "IPv4 contain exactly four octets.")
Test.assert_equals(
    is_valid("1.2.3.4.5"), False, "IPv4 contain exactly four octets.")
Test.assert_equals(
    is_valid("123.45.67.89"), True, "This is a valid IPv4")
Test.assert_equals(
    is_valid("123.456.78.90"), False,
    "Each octet must be a decimal value between 0 and 255.")
Test.assert_equals(
    is_valid("123.045.067.089"), False,
    "Each octet must be a decimal value between 0 and 255.")
Test.assert_equals(
    is_valid(""), False, "An empty string is invalid.")
Test.assert_equals(
    is_valid("abc.def.ghi.jkl"), False, "This is not in dot decimal format.")
Test.assert_equals(
    is_valid("123.456.789.0"), False,
    "Each octet must be a decimal value between 0 and 255.")
Test.assert_equals(
    is_valid("12.34.56"), False, "IPv4 contain exactly four octets.")
Test.assert_equals(
    is_valid("12.34.56 .1"), False, "Check for spaces.")
Test.assert_equals(
    is_valid("12.34.56.-1"), False, "Check for invalid characters.")
Test.assert_equals(
    is_valid("123.045.067.089"), False,
    "Each octet must be a decimal value between 0 and 255.")
Test.assert_equals(
    is_valid("192.168.1.1"), True, "This is a valid IPv4")
Test.assert_equals(
    is_valid("192.168.1.1  "), False, "IPs with trailing spaces are invalid.")
Test.assert_equals(
    is_valid("  192.168.1.1"), False, "IPs with leading spaces are invalid.")
Test.assert_equals(
    is_valid("0.232.47.227"), True, "This is a valid IPv4")
Test.assert_equals(
    is_valid("1e0.1e0.1e0.1e0"), False,
    "Each octet must be a decimal value between 0 and 255.")

Test.summary()
