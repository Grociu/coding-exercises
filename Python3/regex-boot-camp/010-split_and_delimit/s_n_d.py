import re

def split_and_delimit(txt, num, delimiter):
    # as f-strings don't recognise { } as valid chars, and backslashes give 
    # errors, they need to be added separately
    pattern = ".{"+f"1,{num}"+"}"
    return delimiter.join(re.findall(pattern, txt))
