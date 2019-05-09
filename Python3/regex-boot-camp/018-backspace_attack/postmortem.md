My solution is nit that elegant, but it wors. I think this can be done better.

Yup, the top Edabit soluition is this gem:

def erase(txt):
	while '#' in txt:
		txt = re.sub(r'^#|[\w ]#', '', txt)
	return txt

I completely forgot about re.sub but at least it uses the same idea.
After checking this code is 4 times faster than mine. 
I need to do better on optimalization.
The while loop is needed here, because sometimes there will be a line of several
'#' at the start.