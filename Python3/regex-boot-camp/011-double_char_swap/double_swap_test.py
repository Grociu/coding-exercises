import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')

from edabit_tester import EdabitTester
from double_swap import double_swap

Test = EdabitTester()

Test.assert_equals(double_swap("aabbccc", "a", "b"), "bbaaccc")
Test.assert_equals(
    double_swap("random w#rds writt&n h&r&", "#", "&"),
        "random w&rds writt#n h#r#")
Test.assert_equals(
    double_swap("128 895 556 788 999", "8", "9"),
        "129 985 556 799 888")
Test.assert_equals(double_swap("mamma mia", "m", "a"), "amaam aim")
Test.assert_equals(double_swap("**##**", "*", "#"), "##**##")
Test.assert_equals(double_swap("123456789", "4", "5"), "123546789")
Test.assert_equals(double_swap("445566&&", "4", "&"), "&&556644")
Test.assert_equals(double_swap("!?@,.", ",", "."), "!?@.,")
Test.assert_equals(double_swap("Q_Q T_T =.= >.<", "Q", "T"), "T_T Q_Q =.= >.<")
Test.assert_equals(double_swap("(Q_Q) (T_T) (=.=) (>.<)", ")", "("), ")Q_Q( )T_T( )=.=( )>.<(")
Test.assert_equals(double_swap("<>", ">", "<"), "><")
Test.assert_equals(double_swap("001101", "1", "0"), "110010")
Test.assert_equals(double_swap("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~", "a", "b"), "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`bacdefghijklmnopqrstuvwxyz{|}~")

Test.summary()