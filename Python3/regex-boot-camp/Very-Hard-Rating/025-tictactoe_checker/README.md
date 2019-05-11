
Tic Tac Toe Checker

Mike and his friend love playing tic tac toe. In fact, they love it so much they created a multiplayer web version to play remotly against each other. At the last minute Mike realized he forgot to call an animation when a player won the game. Now he needs to create a function that will check it but can't do it himself because he's short on time. Mike needs your help!

Create a function that takes a two dimensional lists representing a finished game of tic tac toe (e.g. [["XO-"], ["XXX"], ["XO-"]]).

    X represents player 1 move(s).
    O represents player 2 move(s).
    Dash (-) represents no move(s).

Rules

1) Return True if player 1 or player 2 win the game.

tic_tac_toe_check( [["XO-"], ["XXO"], ["O-X"]]) ➞ True

2) Return False if nobody won the game.

tic_tac_toe_check([["XXO"], ["OOX"], ["XOO"]]) ➞ False

3) Return "Nobody moved" if nobody made a move.

tic_tac_toe_check([[---],  [---], [---]]) ➞ "Nobody moved"

4) Return "No/Incomplete game" if no value was received / all received lists are void / type of any given value is not "list".

tic_tac_toe_check([[], [], []]) ➞ "No/Incomplete game"

tic_tac_toe_check([[], []]) ➞ "No/Incomplete game"

tic_tac_toe_check([[1, ["XOX"], ["XOO"]]) ➞ "No/Incomplete game"

tic_tac_toe_check(["XOX", ["XOX"], []]) ➞ "No/Incomplete game"

5) Return "Corrupted game" if any values differ from the expected "X", "O", "-".

tic_tac_toe_check([["X"], ["XX"], ["X-"]]) ➞ "Corrupted game"

tic_tac_toe_check([["AAA"], ["BBA"], ["ABB"]]) ➞ "Corrupted game"

tic_tac_toe_check([["XOX"], ["XOO"], [undefined]]) ➞ "Corrupted game"

tic_tac_toe_check([["XXX"], ["XOX"], [""]]) ➞ "Corrupted game"

tic_tac_toe_check([["XXX"], ["XOX"], [1,2,3]]) ➞ "Corrupted game"

Notes

Each list in the main list represent a line in the game.
