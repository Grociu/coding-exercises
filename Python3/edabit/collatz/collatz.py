def collatz(n):
    operations, maximum = 0, n
    while n != 1:
        operations += 1
        if n % 2:
            n = n*3 + 1
            maximum = max(maximum, n)
        else:
            n /= 2
    return [operations, maximum]
