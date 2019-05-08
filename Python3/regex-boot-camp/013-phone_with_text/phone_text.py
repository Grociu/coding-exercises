import string

def text_to_num(phone):
    letters = string.ascii_uppercase
    numbers = "22233344455566677778889999"
    cipher = phone.maketrans(letters, numbers)
    return phone.translate(cipher)