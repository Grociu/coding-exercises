import re

def count_smileys(lst):
    smiley = '[:;][-~]?[)D]'
    count = 0
    for element in lst:
        if re.match(smiley, element):
            count += 1
    return count
