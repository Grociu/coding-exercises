import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from jugs import waterjug

Test = EdabitTester()

Test.assert_equals(waterjug([3, 5, 8], [0, 3, 5]), 2)
Test.assert_equals(waterjug([1, 3, 4],  [0, 2, 2]), 3)
Test.assert_equals(waterjug([8, 17, 20], [0, 10, 10]), 9)
Test.assert_equals(waterjug([4, 17, 22], [2, 5, 15]), "No solution.")
Test.assert_equals(waterjug([3, 5, 8],  [0, 5, 3]), 1)
Test.assert_equals(waterjug([3, 5, 8], [0, 6, 2]), "No solution.")
Test.assert_equals(waterjug([6, 7, 10],  [0, 0, 10]), 0)
Test.assert_equals(waterjug([3, 5, 8],  [4, 0, 4]), "No solution.")
Test.assert_equals(waterjug([3, 5, 8],  [2, 1, 4]), "No solution.")
Test.assert_equals(waterjug([3, 5, 8],  [0, 2, 6]), 3)
Test.assert_equals(waterjug([6, 7, 10],  [5, 5, 0]), "No solution.")
Test.assert_equals(waterjug([30, 45, 50],  [25, 25, 0]), "No solution.")
Test.assert_equals(waterjug([3, 5, 8],  [0, 4, 4]), 7)
Test.assert_equals(waterjug([4, 7, 10],  [0, 5, 5]), 8)

Test.summary()
