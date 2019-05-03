Solved. I forced my solution to use Regex as that's what I'm learning to use.
There is a number of one line solutions (both copied from Edabit).

def convert_to_decimal(perc):
	return [float(item[:-1])/100 for item in perc]

or:

def convert_to_decimal(perc):
	return [float(x.strip("%"))/100 for x in perc]

My regex pattern was

pattern = '[\d]+[\.\d]*'

Which differs from a proposed solutions pattern:

r'\d+\.*\d*

This would not catch a string like 4.44.0, from the input, so it's better.
