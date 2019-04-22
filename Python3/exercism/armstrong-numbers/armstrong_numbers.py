def is_armstrong(number):
    """ This function checks if a number is an Armstrong number.
    
    An Armstrong number is an integer for which the sum of it's digits to the 
    power of it's length is equal to the number itself.
    """
    armstrong = 0
    digits = [int(x) for x in str(number)]
    for i in range(len(digits)):
        armstrong += digits[i] ** len(digits)

    return (armstrong == number)