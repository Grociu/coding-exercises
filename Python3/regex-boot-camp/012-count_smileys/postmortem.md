First actual regex exercise with a happy twist. I initially missed the tilde
also being considered a valid "nose". The solution is ok.

Top solution on Edabit:

import re

def count_smileys(lst):
    return len(re.findall(r'[:;][-~]?[)D]', ''.join(lst)))

This is elegant, first it makes a string from the list. Then searches the string for all occurences, then returns lenght of the list., Overall 1 line function quite readable. 