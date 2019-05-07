import re

def correct_signs(txt):
    # this is the list of all elements, numbers and signs
    elements = [int(n) if n.isdecimal() else n for n in re.split(" ",txt)]
    # this is the list of only numbers
    numbers = elements[::2]
    # depending on the sign between numbers perform the appropreate comparison
    for i in range(len(numbers) - 1):
        if elements[2*i+1] == "<":
            if numbers[i] >= numbers[i+1]:
                return False
        if elements[2*i+1] == ">":
            if numbers[i] <= numbers[i+1]:
               return False
        return True