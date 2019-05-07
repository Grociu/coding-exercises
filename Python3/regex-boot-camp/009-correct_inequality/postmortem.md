Issues:

Mixed type list, some are integers and some are strings.
String defines the operation.

1. This Edabit solution:

def correct_signs(txt):
	lst = [int(i) if i.isdigit() else i for i in txt.split()]
	
	for i in range(0,len(lst)-2,2):
		if lst[i+1] == '>':
			if lst[i] <= lst[i+2]:
				return False
		elif lst[i+1] == '<':
			if lst[i] >= lst[i+2]:
				return False
	return True

1a) Uses only one list of elements to iterate over the list.
    Uses range(0, len(lst)-2, 2) - which essentially is what I wanted to do,
    but sadly forgot the range function syntax allows this.
	The resulting code is more elegant.

2. The surprising 1-line solution:

def correct_signs(txt):
	return eval(txt)

The documentation says to us eval carefully, especaily when handling user input,
but with a given string after parsing should be ok in this case.
This returns the python evaluation of a code. Cool. Didn't know this existed.
