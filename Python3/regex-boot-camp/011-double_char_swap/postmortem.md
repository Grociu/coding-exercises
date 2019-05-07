The authors used a real curve ball here by including a test with all the
signs that are used in regex syntax. I had to be a little creative in filtering 
for those cases.

This can be solved without regex using .replace() string method, though, there 
needs to be a characer not used in the string to do it.

Best way is probably this:

def double_swap(txt, c1, c2):
	return txt.translate(str.maketrans(c1+c2, c2+c1))

uses the translation string method that I used before. This makes a translation
matrix with c1 - > c2 and c2 - > c1, and then uses that to switch the chars.
Neat.