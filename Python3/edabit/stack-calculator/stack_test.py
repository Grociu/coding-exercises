import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from stack import StackCalc

Test = EdabitTester()

tests = [
  {'arg': '12', 'ans': 12},
  {'arg': '5 6 +', 'ans': 11},
  {'arg': '3 6 -', 'ans': 3},
  {'arg': '3 DUP +', 'ans': 6},
  {'arg': '2 5 - 5 + DUP +', 'ans': 16},
  {'arg': '9 14 DUP + - 3 POP', 'ans': 19},
  {'arg': '1 2 3 4 5 POP POP POP', 'ans': 2},
  {'arg': '13 DUP 4 POP 5 DUP + DUP + -', 'ans': 7},
  {'arg': '6 5 5 7 * - /', 'ans': 5},
  {'arg': '4 2 4 * 3 + 5 + / 5 -', 'ans': 1},
  {'arg': '5 8 + 4 5 1 + POP 13 +', 'ans': 17},
  {'arg': 'x', 'ans': 'Invalid instruction: x'},
  {'arg': '4 6 + x', 'ans': 'Invalid instruction: x'},
  {'arg': 'y x *', 'ans': 'Invalid instruction: y'},
  {'arg': '', 'ans': 0},
  {'arg': '4 POP', 'ans': 0}
]

for dict in tests:
	arg = dict['arg']
	ans = dict['ans']
	machine = StackCalc()
	machine.run(arg)
	Test.assert_equals(machine.getValue(), ans)

Test.summary()
