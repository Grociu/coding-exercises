def same_letter_pattern(txt1, txt2):
    if len(txt1) != len(txt2):
        return False
    
    pairs_of_elements = list(zip(txt1, txt2))
    code = {}
    for pair in pairs_of_elements:
        
        if pair[0] not in code:
            code[pair[0]] = pair[1]
        
        elif pair[0] in code:
            if code[pair[0]] != pair[1]:
                return False
    return True
