def is_isogram(string):
    parse = string.lower().replace("-", "").replace(" ", "")
    return len(set(parse)) == len(parse)
