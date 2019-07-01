def is_triangle(trio):
    """Determine whether a three element list of integers (length of sides)
    creates a valid triangle.

    A valid triangle has the sum of two shorter sides longer that the longest
    side.
    """
    trio = sorted(trio)
    return trio[0] + trio[1] > trio[2]


def does_triangle_fit(brick, hole):
    """Given the sides of two triangles as lists of three integers. Determine
    whether a triangular brick will fit into a triangular hole.

    It will fit if all the sides of the brick sorted are smaller that the
    sides of the hole also sorted.
    """
    if not (is_triangle(brick) and is_triangle(hole)):
        return False
    zipper = zip(sorted(brick), sorted(hole))
    # Size criteria.
    if all(side_brick <= side_hole for side_brick, side_hole in zipper):
        return True
    return False
