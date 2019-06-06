import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from parenthesis import split

Test = EdabitTester()

Test.assert_equals(split("()()()"), ["()", "()", "()"])
Test.assert_equals(split(""), [])
Test.assert_equals(split("()()(())"), ["()", "()", "(())"])
Test.assert_equals(split("(())(())"), ["(())", "(())"])
Test.assert_equals(split("((()))"), ["((()))"])
Test.assert_equals(
    split("()(((((((((())))))))))"), ["()", "(((((((((())))))))))"]
    )
Test.assert_equals(
    split("((())()(()))(()(())())(()())"),
          ["((())()(()))", "(()(())())", "(()())"]
    )
Test.assert_equals(
    split("((()))(())()()(()())"), ["((()))", "(())", "()", "()", "(()())"]
    )
Test.assert_equals(split("((())())(()(()()))"), ["((())())", "(()(()()))"])
Test.assert_equals(
  split("(()(()()))()(((()))()(()))(()((()))(())())"), 
        ["(()(()()))", "()", "(((()))()(()))", "(()((()))(())())"]
    )

Test.summary()
