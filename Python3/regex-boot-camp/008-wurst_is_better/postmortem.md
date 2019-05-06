Here's top solution using regex:

import re
pattern = re.compile('|'.join(['kielbasa', ... , 'pepperoni']), re.IGNORECASE)
def wurst_is_better(txt):
    return pattern.sub('Wurst', txt)

first it compiles a pattern to use in the main function. 
joins all the names with the | (or) operator and uses the re.IGNORECASE flag!
This flag would save me some time in my scripts operations.

in the end the author recalls pattern and subs element 'Wurst' in the text.
Very useful!

The test function is working, so at least that's good.