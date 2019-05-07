I had an unneccessary f"delimiter", that was scrapped as f" was not needed.

Could not figure out how to do the ending bits as I originally had "." * num
as pattern which was leaving the endings of words. 

Adding fstrings to regex is tricky because regex uses a lot of / and {} in a 
different way than f-strings

The final solution is not perfectly elegant, but I am happy with it.
