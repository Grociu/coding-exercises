import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from jsc import comments_correct

Test = EdabitTester()

Test.assert_equals(comments_correct("//////"), True)
Test.assert_equals(comments_correct("/**//**////**/"), True)
Test.assert_equals(comments_correct("/**//**//**//**/"), True)
Test.assert_equals(comments_correct("///**///"), True)
Test.assert_equals(comments_correct("/**//////**//**////**/////"), True)
Test.assert_equals(comments_correct("//"), True)
Test.assert_equals(comments_correct("/**/"), True)
Test.assert_equals(comments_correct("///*/**/"), False)
Test.assert_equals(comments_correct("//*/**/"), False)
Test.assert_equals(comments_correct("/////"), False)
Test.assert_equals(comments_correct("///"), False)
Test.assert_equals(comments_correct("/**///**/"), False)
Test.assert_equals(comments_correct("/**/////**/"), False)

Test.summary()
