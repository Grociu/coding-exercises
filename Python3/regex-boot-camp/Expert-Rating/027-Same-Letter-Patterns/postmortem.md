This is quite awful. I should have known that you can just check txt1[i] and make the directory like this Edabit solution:

def same_letter_pattern(txt1, txt2):
    d = {}
    for i in range(len(txt1)):
        if txt1[i] not in d:
             d[txt1[i]] = txt2[i]
    return ''.join(d[k] for k in txt1)==txt2

At least the directory approach seems to be the way to go.

Does not use regex though.