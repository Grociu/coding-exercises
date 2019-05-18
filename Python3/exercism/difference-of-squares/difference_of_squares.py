def square_of_sum(count):
    """Returns a square of the sum of natural nums up to count."""
    sum = 0
    for i in range(1, count+1):
        sum += i
    return sum ** 2


def sum_of_squares(count):
    """Returns a sum of the squares of natural nums up to count."""
    sum = 0
    for i in range(1, count+1):
        sum += i ** 2
    return sum


def difference(count):
    """Difference between sum of squares and square of sum."""
    return square_of_sum(count) - sum_of_squares(count)
