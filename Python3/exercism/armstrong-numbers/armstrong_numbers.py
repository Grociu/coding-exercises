def is_armstrong(number):
    """
    This function checks if the number is an Armstrong number -
    (If the sum of it's digits to the power of it's length is equal
    to the number itself).
    """
    armstrong = 0
    # lists the digits of the number
    digits = [int(x) for x in str(number)]
    # increments the armstrong value by each power
    for i in range(0,len(digits)):
        armstrong += digits[i] ** len(digits)
    # checks if the armstrong value is equal to the original
    return (armstrong == number)