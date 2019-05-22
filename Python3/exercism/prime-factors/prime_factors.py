def prime_factors(natural_number):
    operator = natural_number
    divisor = 2
    result = []
    while operator != 1:
        if operator % divisor == 0:
            result.append(divisor)
            operator = operator // divisor
        else:
            divisor += 1
    return result
