def convert_isbn(isbn):
    """This converts a potential isbn number into a list of elements
    that are integers.

    First it converts all the characters in the string into a list,
    then replaces X at the last position with 10 (control)
    Then if an entry is a number converts it into an integer.
    """
    isbn_list = [isbn[i] for i in range(len(isbn))]
    if len(isbn_list) > 0:
        if isbn_list[-1] == 'X':
            isbn_list[-1] = '10'
    isbn_ints = [int(isbn_list[i]) for i in range(len(isbn_list)) if isbn_list[i].isnumeric()]
    return isbn_ints

def verify(isbn, type=10):
    """ Verifies a given string if it's a valid ISBN number.

    First it converts into a list of numbers, 
    then, if it's eligible it creates an ISBN sum.
    Has basic functionality or checking isbn13
    """
    nums = convert_isbn(isbn)
    if len(nums) != type:
        return False
    isbn_sum = 0
    if type == 10:
        multi = range(type,0,-1)
        for i in range(type):
            isbn_sum += multi[i]*nums[i]
        return isbn_sum % 11 == 0
    elif type == 13:
        for i in range(0,type,2):
            isbn_sum += nums[i]
            logging.debug(f"i is {i}, nums[i] was {nums[i]}, isbn_sum is {isbn_sum}")
        for i in range(1,type,2):
            isbn_sum += 3*nums[i]
            logging.debug(f"i is {i}, nums[i] was {nums[i]}, isbn_sum is {isbn_sum}")
        return isbn_sum % 10 == 0