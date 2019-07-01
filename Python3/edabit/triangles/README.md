
Does the Triangle Fit into the Triangular Hole?

Create a function that takes the dimensions of two triangles (as lists) and 
checks if the first triangle fits into the second one.
Examples

does_triangle_fit([1, 2, 3], [1, 2, 3]) ➞ True

does_triangle_fit([1, 2, 3], [3, 2, 1]) ➞ True

does_triangle_fit([1, 2, 3], [1, 2, 2]) ➞ False

does_triangle_fit([1, 2, 4], [1, 2, 6]) ➞ False

Notes

    Triangle fits if it has the same or smaller size as the hole.
    The function should return False if the triangle with that dimensions
     is not possible.

