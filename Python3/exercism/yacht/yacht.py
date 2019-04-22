# Score categories
YACHT = "YACHT"
ONES = [1]
TWOS = [2]
THREES = [3]
FOURS = [4]
FIVES = [5]
SIXES = [6]
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = [1, 2, 3, 4, 5]
BIG_STRAIGHT = [2, 3, 4, 5, 6]
CHOICE = [1, 2, 3, 4, 5, 6]


def score(dice, category):
    """Takes a roll of 5 dice, and returns the score in a game of Yacht"""
    dice = sorted(dice)
    # A numer of categories returns the sum of matching elements.
    if category in [
        ONES, TWOS, THREES,
        FOURS, FIVES, SIXES,
        CHOICE
        ]:
        calc = 0
        for roll in dice:
            if roll in category:
                calc += roll
        return calc
    # Straights return 30, sorted dice should be the sam as the only solution.
    elif category in [
        LITTLE_STRAIGHT, BIG_STRAIGHT
        ]:
        if dice == category:
            return 30
    # Yacht returns 50, if all elements (sorted!) are the same.
    elif category == YACHT:
        if dice[-1] == dice[0]:
            return 50
    # Four of a kind, since list is sorted, the outlier is on the edge.
    elif category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) >= 4:
            return dice[0] * 4
        elif dice.count(dice[-1]) == 4:
            return dice[-1] * 4
    # Full house is tricky, two pair is not a FH, yacht is not a FH.
    elif category == FULL_HOUSE:
        if dice.count(dice[0]) == 2:
            if dice.count(dice[-1]) == 3:
                return sum(dice)
        elif dice.count(dice[0]) == 3:
            if dice.count(dice[-1]) == 2:
                return sum(dice)
    return 0