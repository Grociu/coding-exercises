import re


def replace_nth(txt, nth, old_char, new_char):
    """This replaces every nth instance of old_char with new_char."""
    if nth == 0:
        return txt
    # Create a list of all matches of old_char.
    MatchObj = re.finditer(old_char, txt)
    result = list(txt)
    # Every nth match gets switched in the list of result.
    for match in list(MatchObj)[nth-1::nth]:
        result[match.start()] = new_char
    # Joins the result to a final string.
    return "".join(result)
