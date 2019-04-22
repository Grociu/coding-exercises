"""
This program will check if a given string contains all the letters
of the English alphabeth.
https://en.wikipedia.org/wiki/Pangram
"""
# define alphabeth
alphabeth = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(sentence):
    """ This function checks if a given sentence is a pangram"""
    # make sentence lowercase
    sentence = sentence.lower()
    # iterate for letters in alphabeth, if letter not found, return false
    for letter in alphabeth:
        if letter not in sentence:
            return False
    return True