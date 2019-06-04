""" This file are the three examples of generators I made for 
execises from Linuxtopia tutorial.
"""

# Example 1

""" 
The Sieve of Eratosthones. 
This exercise has three parts: initialization, generating the list (or set) or 
prime numbers, then reporting. In the list version, we had to filter the 
sequence of boolean values to determine the primes. In the set version, the set
contained the primes. Within the Generate step, there is a point where we know 
that the value of p is prime. At this point, we can yield p. If yield each 
value as we discover it, we eliminate the entire "report" step from the 
function.
"""

def sieve(num):
    primes = set(range(2, num+1))
    for prime_candidate in range(2, num+1):
        if prime_candidate not in primes:
            continue
        yield prime_candidate
        multiples = set(range(prime_candidate, num+1, prime_candidate))
        primes.difference_update(multiples)
        

# generator_sieve = sieve(5000)

# print(list(generator_sieve))

# Example 2

"""
The Generator Version of range. 
The range function creates a sequence. For very large sequences, this consumes 
a lot of memory. You can write a version of range which does not create the 
entire sequence, but instead yields the individual values. Using a generator 
will have the same effect as iterating through a sequence, but won't consume 
as much memory.

Define a generator, genrange, which generates the same sequence of values as 
range, without creating a list object.
"""

def genrange(number):
    index = 0
    while index < number:
        yield index
        index += 1

# generator_genrange = genrange(101)

# print(next(generator_genrange) - 7)
# for i in generator_genrange:
#     print(i**3)

# print(", ".join(str(element) for element in genrange(25)))

# Exercise 3

""" 
Prime Factors. 
There are two kinds of positive numbers: prime numbers and composite numbers. 
A composite number is the product of a sequence of prime numbers. You can write
a simple function to factor numbers and yield each prime factor of the number.

Your factor function can accept a number, n, for factoring. The function will 
test values, f, between 2 and the square root of n to see if the expression 
n % f == 0 is true. If this is true. then the factor, f, divides n with no 
remainder; f is a factor.

Don't use a simple-looking for -loop; the prime factor of 128 is 2, 
repeated 7 times.
"""

def factors(num):
    f = 2
    operator = num
    while f <= num // 2 + 1:
        if operator % f == 0:
            yield f
            operator = operator / f
        else: f += 1
    if operator == num:
        yield num

# generator_factors = factors(333333)
# print(list(generator_factors))
