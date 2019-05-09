import re


def erase(txt):
    result = txt
    pattern = "[^#]?#"
    search_result = re.search(pattern, result)
    while search_result:
        result = result.replace(search_result.group(), "", 1)
        search_result = re.search(pattern, result)
    return result