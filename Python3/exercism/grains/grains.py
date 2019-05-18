def on_square(integer_number):
    if is_valid_square(integer_number):
        return 2 ** (integer_number-1)

def total_after(integer_number):
    if is_valid_square(integer_number):
        return sum(on_square(i+1) for i in range(integer_number))

def is_valid_square(n):
    if 0 < n < 65: return True
    else: raise ValueError("Square number has to be between 1 to 64.")
