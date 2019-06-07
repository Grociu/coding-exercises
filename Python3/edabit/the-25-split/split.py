def product(*args):
    """ Simple product function. """
    prod = 1
    for arg in args:
        prod *= arg
    return prod          

def split(number):
    """ Divides a number into parts that sum into it, that produse the highest
    possible product and returns that product.
    
    Example: 6 is 3+3 or 2+2+2 or 3+2+1, largest of those is 3*3 = 9 
    so 9 is returned. """
    
    parts, rest = [], number
    
    # the exercise suggests that 3 is the best component to extract, this loop
    # substracts 3 each time and appends those 3s to a new list.
    while rest >= 3: 
        parts.append(3)
        rest -= 3
    
    if parts and rest:
        if rest == 1: parts[-1] += rest 
        else: parts.append(rest)
    
    return product(*parts) if product(*parts) > number else number

""" Postmortem:

A much simpler solution exists using recursion:

def split(number):
    return number if numbef < 5 else 3*split(number-3)

Which is very elegant and smart, I wish I could see it while anlyzing the 
problem. The hint might be that there are some values that are constant
(up to 4) here and fib(1) = 1 fib(2) = 1 in Fibbonacci. The rest is derived by
removing 3s (here) or adding elements (Fib).
"""