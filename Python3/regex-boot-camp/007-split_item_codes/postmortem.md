As Very Easy and Easy excersises were easily solved by non regex thinking, I moved up to Medium.

I think I like my statements of patterns to be more clear on regex. I am a big fan of readability.

Edabit top solution is this:

import re

def split_code(item):
    parts = re.search(r'(\D*)(\d*)', item)
    return [parts.group(1), int(parts.group(2))]

which uses regex groups and /D (non alpha numeric), which I also find efficient. 

My original function was trying to look for /d* and was returning empty, making it a /d+ helped.