import re


def valid_color(color):
    pattern_type = '(rgba?)\('
    pattern_element = '[0-9.%-]+'
    # Is the color function is defined correctly? And which type is it?
    try:
        operation_type = re.match(pattern_type, color).group(1)
    except:
        return False
    elements = re.findall(pattern_element, color)
    # Internal function to check whether a list of three is a valid rgb
    def is_valid_rgb(triple):
        if len(triple) != 3:
            return False  
        for element in triple:
            # checks percentage values
            if element[-1] == '%':
                if int(element[:-1]) not in range(0,101):
                    return False
            # checks numerical values
            elif int(element) not in range(0,256):
                return False
        return True
        
    if operation_type == "rgb":
        return is_valid_rgb(elements)

    if operation_type == "rgba":
        # first three have to be valid rgb.
        if not is_valid_rgb(elements[:-1]):
            return False
        # alpha needs to be between 0 and 1
        alpha = float(elements[-1])
        if alpha >=0 and alpha <= 1:
            return True
        return False