import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from strip import strip_url_params

Test = EdabitTester()

Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2&a=2"), "https://edabit.com?a=2&b=2")
Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]), "https://edabit.com?a=2")
Test.assert_equals(strip_url_params("https://edabit.com", ["b"]), "https://edabit.com")
Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2"), "https://edabit.com?a=1&b=2")
Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2", ["c"]), "https://edabit.com?a=1&b=2")
Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2&c=3&d=4", ["a", "d"]), "https://edabit.com?b=2&c=3", "The 2nd argument can contain multiple URL params.")
Test.assert_equals(strip_url_params("https://edabit.com?a=1&b=2&c=3&d=4&c=5", ["a", "d"]), "https://edabit.com?b=2&c=5")
Test.summary()
