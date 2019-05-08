import re


def comments_correct(txt):
    pattern = '((//)+|(/\*\*/)+)+'
    if re.match(pattern, txt):
        return re.match(pattern, txt).group() == txt
    else:
        return False
