"""
This calculates the score of a dart throw based on coordinates.
If the dart lands outside the target, player earns no points (0 points).
If the dart lands in the outer circle of the target, player earns 1 point.
If the dart lands in the middle circle of the target, player earns 5 points.
If the dart lands in the inner circle of the target, player earns 10 points.

The outer circle has a radius of 10 units (This is equivalent to the total radius for the entire target)
The middle circle a radius of 5 unit. 
The inner circle a radius of 1 unit.
"""
# Define the board
o_circle_radius = 10
m_circle_radius = 5
i_circle_radius = 1

def distance_from_center(x,y):
    """This function returns the distance from the center of the board"""
    return (x ** 2 + y ** 2) ** 0.5

def score(x, y):
    """This function returns your score for a single throw"""
    if distance_from_center(x,y) > o_circle_radius:
        return 0
    elif distance_from_center(x,y) > m_circle_radius:
        return 1
    elif distance_from_center(x,y) > i_circle_radius:
        return 5
    else:
        return 10
