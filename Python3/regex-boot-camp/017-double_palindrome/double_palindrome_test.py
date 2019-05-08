import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from double_palindrome import palindrome_set

Test = EdabitTester()

Test.assert_equals(
    palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]), [2, 2, 1, 0])
Test.assert_equals(
    palindrome_set(["18a99b89cc881ba", "p7o8p987", "p7o", "p7o8"]),
    [1, 2, 1, 0])
Test.assert_equals(
    palindrome_set(["ab9a", "abba", "aa78bb8bbaa7", "a88a"]), [2, 1, 2, 2])
Test.assert_equals(palindrome_set(["789", "555", "ccc", "abba"]), [0, 1, 1, 1])
Test.assert_equals(palindrome_set(["7a", "5f", "6c"]), [2, 2, 2])
Test.assert_equals(palindrome_set(["7ab", "5fc", "6cd"]), [1, 1, 1])
Test.assert_equals(palindrome_set(["87ab", "15fc", "26cd"]), [0, 0, 0])
Test.assert_equals(palindrome_set(["1234ab", "144a441"]), [0, 2])
Test.assert_equals(palindrome_set([""]), [0])

Test.summary()
