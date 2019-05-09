import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from backspace import erase

Test = EdabitTester()

Test.assert_equals(erase("he##l#hel#llo"), "hello")
Test.assert_equals(erase("major# spar##ks"), "majo spks" )
Test.assert_equals(erase("si###t boy"), "t boy")
Test.assert_equals(erase("motion #sick"), "motionsick")
Test.assert_equals(erase("m#oti#o#n sick##ne#ss##"), "otn sin")
Test.assert_equals(erase("courz#i#age"), "courage")
Test.assert_equals(erase("aris##### c#r#ti#c"), " tc")
Test.assert_equals(erase("beauty##"), "beau")
Test.assert_equals(erase("beauty#"), "beaut")
Test.assert_equals(erase("b#"), "")
Test.assert_equals(erase("####"), "")

Test.summary()
