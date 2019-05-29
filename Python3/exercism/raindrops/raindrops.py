def raindrops(number):
    """ If the number is divisible by an argument in args, add corresponding
    string to the result. If no divisors are contained in the args dictionary, 
    return the number as string.
    """
    args = {3 : "Pling", 5 : "Plang", 7 : "Plong"}
    result = [args[i] for i in args.keys() if number % i == 0]
    if not result:
        result.append(str(number))
    return "".join(result)
