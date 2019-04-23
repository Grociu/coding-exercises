""" Prints odd numbers in range 1-100.

23.04.2019 Found as an example of a quick exercise to write on the spot
during a programmer job interview as a basic filtering question.
I learned about unpacking writing this as print(range(2)) won't work 
since range does not create a list that print recognises object.
"""
print(*range(1, 101, 2))