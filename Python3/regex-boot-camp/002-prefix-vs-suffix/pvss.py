import re 

def is_prefix(word, prefix):
    """Finds if the word starts with a given prefix."""
    # Pattern is, start of string, find a word, and only letters.
    pattern = '^\w+'
    # First we filter the prefix (eliminating the '-').
    pattern2 = re.search(pattern, prefix).group()
    # Second we search the word for the prefix, starting with the start of 
    # string. I've added additional tests to include the phrase inside the 
    # target word to make it more interesting.
    # In addition , bool of a search object is True if it's not empty.
    return bool(re.search(f"^{pattern2}", word))

def is_suffix(word, suffix):
    """Finds whether a word ends with a given suffix."""
    # Same as above.
    pattern = '\w+$'
    pattern2 = re.search(pattern, suffix).group()
    return bool(re.search(f"{pattern2}$", word))