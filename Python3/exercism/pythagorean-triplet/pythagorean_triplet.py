"""
Leonard Eugene Dickson (1920) attributes to himself the following method for
generating Pythagorean triples.
To find integer solutions to x^2 + y^2 = z^2
find positive integers r, s, and t such that r^2 = 2*s*t is a perfect square.

Then:

    x = r + s ,
    y = r + t ,
    z = r + s + t

From this we see thatr is any even integer
and that s and t are factors of r^2/2
All Pythagorean triples may be found by this method.
When s and t are coprime, the triple will be primitive.
A simple proof of Dickson's method has been presented by
Josef Rukavicka (2013)

Example:
Choose r = 6. Then r^2/2 = 18
 The three factor-pairs of 18 are: (1, 18), (2, 9), and (3, 6).
 All three factor pairs will produce triples using the above equations.
s = 1, t = 18 produces the triple [7, 24, 25] because
x = 6 + 1 = 7,  y = 6 + 18 = 24,  z = 6 + 1 + 18 = 25.
s = 2, t =   9 produces the triple [8, 15, 17] because
x = 6 + 2 = 8,  y = 6 +  9 = 15,  z = 6 + 2 + 9 = 17.
s = 3, t =   6 produces the triple [9, 12, 15] because
x = 6 + 3 = 9,  y = 6 +  6 = 12,  z = 6 + 3 + 6 = 15.
(Since s and t are not coprime, this triple is not primitive.)
"""


def triplets_with_sum(sum_of_triplet):
    return {
        element
        for element in triplets_in_range(3, sum_of_triplet//2)
        if sum(element) == sum_of_triplet
    }


def triplets_in_range(range_start, range_end):

    result, start = [], range_start
    if start % 2:
        start -= 1

    for r in range(start, range_end-2, 2):
        r_check = r**2 // 2
        # For a tuple (x, y, z), this formula will return at most the largest
        # element z with vaule of r + s + t where s and t are smaller than
        # sqrt(r_check). 2 * sqrt(r_check) is r so this end condition for the
        # whole loop cuts the needed calculations.
        if 2 * r > range_end:
            break
        # Constructs a list of tuples that are factors of r_check
        factors = [
            (i, r_check//i)
            for i in range(1, int(r_check**0.5 // 1 + 1))
            if r_check % i == 0
        ]
        # Based on the formula constructs Pythagorean triples that are in range
        result.extend(
            [(r + s, r + t, r + s + t)
             for (s, t) in factors
             if r + s + t <= range_end and r + s >= range_start]
        )
    return result
