def letter_check(lst):
    char_set_A = set(lst[0].lower())
    char_set_B = set(lst[-1].lower())
    return char_set_B.issubset(char_set_A)