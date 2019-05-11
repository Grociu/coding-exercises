import sys
sys.path.append('D:/Python/coding-exercises/Python3/utility')
from edabit_tester import EdabitTester
from ttt import tic_tac_toe_check

Test = EdabitTester()

Test.assert_equals(tic_tac_toe_check([["-X-"],["OXO"],["--O"]]),False)
Test.assert_equals(tic_tac_toe_check([["O-X"],["XOO"],["XOX"]]),False)
Test.assert_equals(tic_tac_toe_check([["-XO"],["XOX"],["O-O"]]),True)
Test.assert_equals(tic_tac_toe_check([["--X"],["-O-"],["-O-"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["---"],["X--"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOO"],["X--"],["XOO"]]),True)
Test.assert_equals(tic_tac_toe_check([["XO-"],["OX-"],["X-O"]]),False)
Test.assert_equals(tic_tac_toe_check([["-OX"],["---"],["--X"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["-OO"],["X--"]]),False)
Test.assert_equals(tic_tac_toe_check([["OO-"],["XXX"],["OXO"]]),True)
Test.assert_equals(tic_tac_toe_check([["OOO"],["-OX"],["X-X"]]),True)
Test.assert_equals(tic_tac_toe_check([["XO-"],["-XO"],["-XO"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOX"],["-XO"],["-OO"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["--O"],["X--"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["-X-"],["OO-"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOO"],["OXO"],["XXX"]]),True)
Test.assert_equals(tic_tac_toe_check([["--O"],["XOX"],["OOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["O--"],["--X"],["O--"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["--O"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["--X"],["XO-"],["-XO"]]),False)
Test.assert_equals(tic_tac_toe_check([["--O"],["--X"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["--X"],["O--"]]),False)
Test.assert_equals(tic_tac_toe_check([["-O-"],["---"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["X--"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["-O-"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["X-O"],["---"],["X-O"]]),False)
Test.assert_equals(tic_tac_toe_check([["-X-"],["X--"],["OXO"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["---"],["--O"]]),False)
Test.assert_equals(tic_tac_toe_check([["XX-"],["-O-"],["-XO"]]),False)
Test.assert_equals(tic_tac_toe_check([["-XX"],["-O-"],["OO-"]]),False)
Test.assert_equals(tic_tac_toe_check([["OOX"],["XX-"],["XOO"]]),True)
Test.assert_equals(tic_tac_toe_check([["--X"],["---"],["XO-"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOO"],["XOO"],["XOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["X-X"],["XXO"],["O-O"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOX"],["OXX"],["OOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["XOX"],["XOX"],["OOO"]]),True)
Test.assert_equals(tic_tac_toe_check([["---"],["O--"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["---"],["O-X"]]),False)
Test.assert_equals(tic_tac_toe_check([["OOO"],["OXX"],["XOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["--O"],["XXO"],["OOX"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["---"],["O--"]]),False)
Test.assert_equals(tic_tac_toe_check([["OOO"],["XOX"],["OXX"]]),True)
Test.assert_equals(tic_tac_toe_check([["XX-"],["-O-"],["OX-"]]),False)
Test.assert_equals(tic_tac_toe_check([["OXX"],["XXX"],["OOO"]]),True)
Test.assert_equals(tic_tac_toe_check([["OXX"],["XOO"],["OXO"]]),True)
Test.assert_equals(tic_tac_toe_check([["--X"],["OO-"],["XOX"]]),False)
Test.assert_equals(tic_tac_toe_check([["XXO"],["OOX"],["OOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["OOO"],["-XO"],["-XX"]]),True)
Test.assert_equals(tic_tac_toe_check([["---"],["-O-"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["XO-"],["XO-"],["OXX"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["O--"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["-X-"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"],["O--"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["-OO"],["X-X"],["O-X"]]),False)
Test.assert_equals(tic_tac_toe_check([["X-O"],["---"],["--X"]]),False)
Test.assert_equals(tic_tac_toe_check([["O--"],["XO-"],["XO-"]]),False)
Test.assert_equals(tic_tac_toe_check([["OX-"],["O--"],["X--"]]),False)
Test.assert_equals(tic_tac_toe_check([["OXO"],["---"],["X-O"]]),False)
Test.assert_equals(tic_tac_toe_check([["-XO"],["X--"],["--O"]]),False)
Test.assert_equals(tic_tac_toe_check([["XOX"],["OOX"],["XOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["XOO"],["OXO"],["XOX"]]),True)
Test.assert_equals(tic_tac_toe_check([["-XO"],["-X-"],["---"]]),False)
Test.assert_equals(tic_tac_toe_check([["--O"],["--X"],["-X-"]]),False)
Test.assert_equals(tic_tac_toe_check([["--O"],["OX-"],["X-O"]]),False)
Test.assert_equals(tic_tac_toe_check([["X--"],["OOX"],["--O"]]),False)
Test.assert_equals(tic_tac_toe_check([["---"]]),"No/Incomplete game")
Test.assert_equals(tic_tac_toe_check([1, ["XOX"], ["XOO"]]), "No/Incomplete game")
Test.assert_equals(tic_tac_toe_check([["X"],["XX"],["X-"]]), "Corrupted game")
Test.assert_equals(tic_tac_toe_check([["AAA"],["BBA"],["ABB"]]), "Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XOX"],["XOO"],[None]]), "Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XXX"],["XOX"],[""]]), "Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XXX"],["XOX"],[1,2,3]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XXX"],["X_X"],["XOX"]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XOO"],["OXO"],[{}]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["OXO"],["OXO"],["OXOX"]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XOXO"],["OXO"],["XOX"]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["XOX"],["OXXO"],["XOX"]]),"Corrupted game")
Test.assert_equals(tic_tac_toe_check([["---"],["---"],["---"]]),"Nobody moved")

Test.summary()