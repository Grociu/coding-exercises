Best takeaway from this is that my edabit_test module is working.
I wrote a module so I just need to copy and paste the edabit test functions into and have a test function ready in my own workspace.

In this exercise I learned if re.match, and re.search return no matches, the group() function is going to give an Error. it is problematic.

Top solution for the exercise Edabit is this:

def format_num(n):
		return "{:,}".format(n)

which seems to be default way of doing this without regex. It looks like an in built function to split integers at every three digits