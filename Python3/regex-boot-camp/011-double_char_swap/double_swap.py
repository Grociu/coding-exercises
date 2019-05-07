import re

def double_swap(txt, c1, c2):
    
    # parse special characters
    parsed_c1 = c1
    parsed_c2 = c2
    if not c1.isalnum():
        parsed_c1 = '\\' + c1
    if not c2.isalnum():
        parsed_c2 = '\\' + c2    
    
    # replace c1 with c2
    # list because of ease of changing the indexed value (invalid for strings)
    new_text = list(re.sub(parsed_c1, c2, txt))
    
    # find instances in txt to replace and change them in new_text
    for match in  re.finditer(parsed_c2, txt):
        new_text[match.start()] = c1
    
    return "".join(new_text)