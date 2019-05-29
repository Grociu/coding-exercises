def classify(number):
    if number <= 0: 
        raise ValueError(f"{number} is not a natural greater than 1.")
    result = []
    # This algorithm lists factors iterating only through nums torawds 
    # sqrt(number). It's complexity is O(sqrt(n)). Finds pairs of divisors,
    # appends them to a list of all divisors.
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            if number // i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(number // i)
    # The number itself is excluded from the aliquot sum.
    sum_factors = sum(result) - number
    if sum_factors < number:
        return "deficient"
    elif sum_factors == number:
        return "perfect"
    else:
        return "abundant"
