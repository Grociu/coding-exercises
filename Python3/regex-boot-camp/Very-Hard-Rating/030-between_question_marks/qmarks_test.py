import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from qmarks import question_marks

Test = EdabitTester()

Test.assert_equals(question_marks(""), False)
Test.assert_equals(question_marks("???"), False)
Test.assert_equals(question_marks("0???9"), False)
Test.assert_equals(question_marks("1???9???10"), True)
Test.assert_equals(question_marks("1???9???1"), True)
Test.assert_equals(question_marks("1???9xx0???10"), True)
Test.assert_equals(question_marks("0???10"), True)
Test.assert_equals(question_marks("-1???11"), True)
Test.assert_equals(question_marks("111???-101"), True)
Test.assert_equals(question_marks("arrb6???4xxbl5???eee5"), True)

Test.summary()
