import re

def split_code(item):
	split = []
	letters = '[A-Z]+'
	digits = '\d+'
	split.append(re.search(letters, item).group())
	split.append(int(re.search(digits, item).group()))
	return split
	