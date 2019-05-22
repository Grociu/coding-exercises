def largest_palindrome(max_factor, min_factor=0):
    is_valid_input(max_factor, min_factor)
    palin, factors = None, set()
    # Main iterator going from the largest number in range down.
    for a in range(min_factor, max_factor + 1)[::-1]:
        # Condition to break the loop. If a palindrome exists and the main
        # iterator (going down) multiplied by the maximum of the range is lower
        # that the palindrome, all other values will be lower.
        if palin and a * max_factor < palin:
            break
        # Second iterator going from the largest number to a, tries to minimise
        # the number of calculations done until a candidate is found.
        for b in range(a, max_factor + 1)[::-1]:
            product = a * b
            # Main working loop, a candidate is found.
            if num_is_palindrome(product):
                # If it's larger that the current palindrome or the first one,
                # assign the value to palin and define its factors.
                if not palin or product > palin:
                    palin = product
                    factors = {(a, b)}
                # If it's the same as the current palindrome, add it's new
                # factors to the set of factors.
                if product == palin:
                    factors.add((a, b))
                # Since the b loop is going down to a, all other products will
                # be smaller that currently analized palindrome.
                break
    return palin, factors


def smallest_palindrome(max_factor, min_factor=0):
    is_valid_input(max_factor, min_factor)
    palin, factors = None, set()
    for a in range(min_factor, max_factor + 1):
        if palin and a * min_factor < palin:
            break
        for b in range(min_factor, a + 1):
            product = a * b
            if num_is_palindrome(product):
                if not palin or product < palin:
                    palin = product
                    factors = {(a, b)}
                if product == palin:
                    factors.add((a, b))
                break
    return palin, factors


def is_valid_input(a, b):
    if b <= a:
        return True
    else:
        raise ValueError("Entered value for minimum is larger than max.")


def num_is_palindrome(num):
    return str(num) == str(num)[::-1]
