I got the idea for the pattern quite quick, I'm happy with this code.

Edabit has this:

import re

def can_complete(initial, word):
	pattern = r'.*?'.join(initial)
	return bool(re.match(pattern, word))

which implies that I don't need to turn a string into list to join it with something element by element (the string works like a list in that case).