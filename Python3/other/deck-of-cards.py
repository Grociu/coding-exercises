""" 
Make a standard deck of cards, and draw two random cards from it.

23.04.2019 Found as an example of a quick exercise to write on the spot
during a programmer job interview as a basic filtering question.
"""
import random
# define the deck
values = range(1, 14)
colors = ["H", "S", "D", "C"]
deck = [f"{value}{color}" for value in values for color in colors]

def draw_random_card():
    return random.randint(0, len(deck)-1)

rand1 = draw_random_card()
rand2 = draw_random_card()
# ensure uniqueness
while rand2 == rand1:
    rand2 == draw_random_card()
else:
    print(deck[rand1], deck[rand2])

