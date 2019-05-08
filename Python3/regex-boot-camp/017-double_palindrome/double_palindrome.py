import re


def palindrome_set(lst):
    result = []
    for element in lst:
        count = 0
        letters = "".join(re.findall("\D*", element))
        numbers = "".join(re.findall("\d*", element))
        if letters == letters[::-1] and letters:
            count += 1
        if numbers == numbers[::-1] and numbers:
            count += 1
        result.append(count)
    return result
