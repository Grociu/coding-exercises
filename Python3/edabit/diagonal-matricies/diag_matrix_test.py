import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from diag_matrix import diagonalize

Test = EdabitTester()

Test.assert_equals(diagonalize(3, 'ul'), [
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 4]
], "It should work for the upper left corner.")

Test.assert_equals(diagonalize(4, 'ur'), [
    [3, 2, 1, 0],
    [4, 3, 2, 1],
    [5, 4, 3, 2],
    [6, 5, 4, 3]
], "It should work for the upper right corner.")

Test.assert_equals(diagonalize(3, 'll'), [
    [2, 3, 4],
    [1, 2, 3],
    [0, 1, 2]
], "It should work for the lower left corner.")

Test.assert_equals(diagonalize(5, 'lr'), [
    [8, 7, 6, 5, 4],
    [7, 6, 5, 4, 3],
    [6, 5, 4, 3, 2],
    [5, 4, 3, 2, 1],
    [4, 3, 2, 1, 0]
], "It should work for the lower right corner.")

Test.summary()
