import re


def findShortestWords(txt):
    words = re.findall("[a-zA-Z']+", txt)
    shortest = min(map(len, words))
    words = [word.lower() for word in words if len(word) == shortest]
    words.sort()
    return words
