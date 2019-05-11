import re


def tic_tac_toe_check(a):
    if a == [["---"],  ["---"], ["---"]]:
        return "Nobody moved"
    
    for line in a:
        if type(line) != type([]) or len(a) != 3:
            return "No/Incomplete game"
        
        if  line == [None] or \
            type(line[0]) != type("") or \
            len(line[0]) != 3 or \
            not re.match('[XO-]{3}', "".join(line)):
                return "Corrupted game"
    
    def row_victory(game):
        for line in game:
            if line in [['OOO'], ['XXX']]:
                return True 
        return False
    
    def column_victory(game):
        for i in range(3):
            if  game[0][0][i] in ['X', 'O'] and \
                game[0][0][i] == game[1][0][i] and \
                game[1][0][i] == game[2][0][i]:  
                return True   
        return False
    
    def diagonal_victory(game):
        for i in [0, 2]:
            if  game[0][0][i] in ['X', 'O'] and \
                game[0][0][i] == game[1][0][1] and \
                game[1][0][1] == game[2][0][2-i]:  
                return True   
        return False
    
    return row_victory(a) or column_victory(a) or diagonal_victory(a)
