def is_equilateral(sides):
    return is_a_triangle(sides) and len(set(sides)) == 1
        

def is_isosceles(sides):
    return is_a_triangle(sides) and len(set(sides)) <= 2


def is_scalene(sides):
    return is_a_triangle(sides) and len(set(sides)) == 3


def is_a_triangle(sides):
    return len(sides) == 3 \
    and [side for side in sides if side <= 0] == [] \
    and max(sides) <= sum(sides) - max(sides)
