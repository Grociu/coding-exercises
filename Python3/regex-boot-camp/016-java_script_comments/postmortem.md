The problem here was the construction of the pattern, but the test function helped with that.

The Edabit solution:

import re

def comments_correct(txt):
	return True if re.match(r'^(/\*\*/|//)+$', txt) else False

checks with caret ^ and dollar $ that the pattern is the whole text. If the match is at the start of the string and the match is at the end string the match is the string. Clever. Would save 3 lines.

Also the construct return True if <statement> else False is new to me, but I'd just use bool()
This might be faster? 

Test say they return True is <> else False is just a little faster, but it's neglegible.
My function takes twice as long for 100k iterations.