def saddle_points(matrix):
    if not matrix:
        return set()
    if not is_regular(matrix):
        raise ValueError("Irregular matrix.")
    # Defines columns of the matrix.
    columns = [
            [matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))
        ]
    # Defines potential saddle points - maximums in rows.
    potential = [
            (element, (i_row, i_col))
            for i_row, row in enumerate(matrix)
            for i_col, element in enumerate(row)
            if element == max(row)
        ]

    result = set()
    # Search potential saddle points, if they are minimums in their columns.
    for element, coords in potential:
        if element == min(columns[coords[1]]):
            result.update([(coords[0]+1, coords[1]+1)])

    return result


def is_regular(matrix):
    return all(len(row) == len(matrix[0]) for row in matrix)
