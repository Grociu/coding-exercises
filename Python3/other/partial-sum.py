""" 
Assuming you have two integers x and y with y bigger than x. Sum all the
numbers from x to y. For example if x = 1 and y = 5, sum =1+..+5

23.04.2019 Found as an example of a quick exercise to write on the spot
during a programmer job interview as a basic filtering question.
"""
def partial_sum(x, y):
    sum = 0
    while x <= y:
        sum += x
        x += 1
    else:
        return sum