import re


def is_valid(txt):
    pattern = '^([1-2]?[0-9]{1,2}\.){3}[1-2]?[0-9]{1,2}$'
    return bool(re.match(pattern, txt))
