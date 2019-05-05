import re

def replace_vowels(txt, ch):
    """Replaces vowels in a string with character ch."""
    # First establish a pattern for the sub function.
    # I'm looking for any vowel.
    pattern = '[aeiou]'
    # nou use the sub function to replace any occurences of pattern in the txt
    # with char ch
    return re.sub(pattern, ch, txt)