def split(txt):
    result, current, count =  [], "", 0
    for char in txt:
        if char == "(": count += 1   
        if char == ")": count -= 1
        current += char
        if count == 0:
            result.append(current)
            current = ""
    return result