def diagonalize(n, d):
    matrix = [list(range(i, n+i)) for i in range(n)]
    if d == "ul":
        return matrix
    if d == "ur":
        return [row[::-1] for row in matrix]
    if d == "ll":
        return matrix[::-1]
    if d == "lr":
        return [row[::-1] for row in matrix[::-1]]
