def collatz_steps(n):
    if n < 1: raise ValueError("Needs to be positive.")

    steps = 0
    while n != 1:
        steps += 1
        if n % 2: n = n*3 + 1
        else: n //= 2
    else:
        return steps
