import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from phone_text import text_to_num

Test = EdabitTester()

Test.assert_equals("123-647-3937", text_to_num("123-647-EYES"))
Test.assert_equals("(325)444-8378", text_to_num("(325)444-TEST"))
Test.assert_equals("653-879-8447", text_to_num("653-TRY-THIS"))
Test.assert_equals("435-224-7613", text_to_num("435-224-7613"))
Test.assert_equals("(333)668-3245", text_to_num("(33D)ONT-FAIL"))
Test.assert_equals("(025)445-6741", text_to_num("(025)445-6741"))

Test.summary()
