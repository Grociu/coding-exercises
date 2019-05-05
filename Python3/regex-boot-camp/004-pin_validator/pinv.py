import re

def is_valid_PIN(pin):
    """Returns whether a string is a valid 4 or 6 digit PIN number."""
    # Specified pattern had to include 4 or 6 digits. At the very start, I had
    # just \d{4}|\d{6} which was catching 5 digits, so after some searching I
    # added the ^ and $ operators.
    pattern = '^\d{4}$|^\d{6}$'
    return bool(re.search(pattern, pin))