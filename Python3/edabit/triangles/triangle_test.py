import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from triangle import does_triangle_fit

Test = EdabitTester()

Test.assert_equals(does_triangle_fit([1, 1, 1], [1, 1, 1]), True)
Test.assert_equals(does_triangle_fit([1, 1, 1], [2, 2, 2]), True)
Test.assert_equals(does_triangle_fit([1, 6, 8], [1, 6, 8]), False)
Test.assert_equals(does_triangle_fit([12, 63, 42], [1, 6, 8]), False)
Test.assert_equals(does_triangle_fit([3, 6, 8], [23, 63, 42]), True)
Test.assert_equals(does_triangle_fit([3, 6, 8], [1, 10, 8]), False)
# Additional tests to this exercise.
# Brick bigger than the hole.
Test.assert_equals(does_triangle_fit([10, 10, 10], [4, 4, 4]), False)
# Spiky brick cannot fit a hole despite smaller area.
Test.assert_equals(does_triangle_fit([1, 8, 8], [6, 6, 6]), False)
Test.assert_equals(does_triangle_fit([1, 8, 8], [4, 4, 4]), False)

Test.summary()
