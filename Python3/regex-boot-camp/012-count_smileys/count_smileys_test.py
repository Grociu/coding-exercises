import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from count_smileys import count_smileys

Test = EdabitTester()

Test.assert_equals(count_smileys([":)", ";(", ";}", ":-D"]), 2)
Test.assert_equals(count_smileys([";D", ":-(", ":-)", ";~)"]), 3)
Test.assert_equals(count_smileys([";]", ":[", ";*", ":$", ";-D"]), 1)
Test.assert_equals(count_smileys([";(", ":>", ":}", ":]"]), 0)
Test.assert_equals(count_smileys([":)", ":)", ":)", ":)", ":)", ":)", ":)",
                                 ":)", ":)", ":)", ":)", ":)", ":)"]), 13)
Test.assert_equals(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
Test.assert_equals(count_smileys([':-)', ';~D', ':-D', ':_D']), 3)
Test.assert_equals(count_smileys([':---)', '))', ';~~D', ';D']), 1)
Test.assert_equals(count_smileys([';~)', ':)', ':-)', ':--)']), 3)
Test.assert_equals(count_smileys([':o)', ':--D', ';-~)']), 0)
Test.assert_equals(count_smileys([]), 0, "An empty list should return 0")

Test.summary()
