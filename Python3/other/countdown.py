""" Countdown from 700 to 200 in increments of 13.

23.04.2019 Found as an example of a quick exercise to write on the spot
during a programmer job interview as a basic filtering question.
"""
def countdown(high, low, increment):
    return range(high, low+1, -increment)

print(*countdown(700,200,13))