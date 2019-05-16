import re
import itertools


def unravel(txt):
    # Isolate the expressions in []
    splits = re.findall('\[.*?\]', txt)
    for i in range(len(splits)):
        txt = txt.replace(splits[i], '@')
        splits[i] = [word for word in re.split('\|', splits[i][1:-1])]
    # Creates a list of tuples that contain strings that we're changing into.
    splits = list(itertools.product(*splits))
    # Constructs the result, replaces occurences of @ with values from tuples.
    result = [txt for i in range(len(splits))]
    for i in range(len(splits)):
        for j in range(len(splits[i])):
            result[i] = result[i].replace('@', splits[i][j], 1)
    return sorted(result)
