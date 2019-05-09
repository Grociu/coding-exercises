import re


def can_complete(initial, word):
    pattern = ".*".join(list(initial))
    print(pattern)
    return bool(re.match(pattern, word))