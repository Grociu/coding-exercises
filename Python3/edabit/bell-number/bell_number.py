"""
The Bell numbers can easily be calculated by creating the so-called Bell 
triangle, also called Aitken's array or the Peirce triangle after Alexander 
Aitken and Charles Sanders Peirce.

1. Start with the number one. 
2. Put this on a row by itself. x(0, 1) = 1
3. Start a new row with the rightmost element from the previous row as the 
leftmost number x(i, 1) = x(i−1, r) where r is the last element of (i-1)-th row).
4. Determine the numbers not on the left column by taking the sum of the number 
to the left and the number above the number to the left, that is, the number 
diagonally up and left of the number we are calculating 
x(i, j) = x(i, j-1) + x(i−1, j−1)
5. Repeat step three until there is a new row with one more number than the 
previous row (do step 4 until j = r + 1
6.The number on the left hand side of a given row is the Bell number for that 
row.

Here are the first five rows of the triangle constructed by these rules:

 1
 1   2
 2   3   5
 5   7  10  15
15  20  27  37  52

The Bell numbers appear on both the left and right sides of the triangle. 
"""
def bell_triangle_row(n):
    if n <= 1: return [1]
    previous = bell_triangle_row(n-1) 
    result, i = [previous[-1]], 1
    while len(result) <= len(previous):
        result.append(result[i-1] + previous[i-1])
        i += 1
    return result

def bell(n):
    return bell_triangle_row(n)[-1]