import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from s_n_d import split_and_delimit

Test = EdabitTester()

Test.assert_equals(
    split_and_delimit("bellow", 2, '&'), "be&ll&ow")
Test.assert_equals(
    split_and_delimit("magnify", 3, ':'), "mag:nif:y")
Test.assert_equals(
    split_and_delimit("poisonous", 2, '~'), "po~is~on~ou~s")
Test.assert_equals(
    split_and_delimit("shape-shifting", 5, '^'), "shape^-shif^ting")
Test.assert_equals(
    split_and_delimit("nebulous", 1, '#'), "n#e#b#u#l#o#u#s")

Test.summary()