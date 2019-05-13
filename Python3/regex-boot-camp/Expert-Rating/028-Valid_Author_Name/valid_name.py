import re


def valid_name(name):
    words = name.split()
    if not 2<=len(words)<=3: return False
    pattern = '([A-Z]{1}[a-z]+$)|([A-Z]{1}\.)'
    for word in words:
        if not re.match(pattern, word): return False
    # If initial is at the start, second element can't be a word.
    if  len(words) == 3 and \
        words[0] == re.match(pattern, words[0]).group(2) and \
        words[1] == re.match(pattern, words[1]).group(1):
        return False
    # Last element can't be an initial.
    if words[-1] == re.match(pattern, words[-1]).group(2):
        return False
    return True