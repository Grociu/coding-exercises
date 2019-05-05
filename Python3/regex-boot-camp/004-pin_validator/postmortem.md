I spend a lot of time writing the test function, as it contained 19 entries.
I need to automate that better (so I just can just straight copy paste from 
Edabit for example)

3 solutions on edabit are interesting

import re
def is_valid_PIN(pin):
	return bool(re.search("^(\d{4}|\d{6})$",pin))

import re
def is_valid_PIN(pin):
    return bool(re.match('^(?:\d{4}|\d{6})$', pin))

These applies DRY to the formula, puts ^ and $ berore and after parenthesis.
    
    
import re
def is_valid_PIN(pin):
    return bool(re.fullmatch(r'\d{4}|\d{6}',pin))

As I'm unfamiliar with fullmatch, turns out the whole string has to fit the 
pattern for this to return match object, which would solve my problem with 
catching 5 digits.
