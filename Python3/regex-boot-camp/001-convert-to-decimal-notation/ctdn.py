import re

def convert_to_decimal(perc):
    """Converts a list of percentages, to a list of numerical values."""
   
    # each percentage is represnted by a string of numerical value
    # which can be a float, and the percent sign. I'm thinking of using 
    # findall for this one.
    # on second thaught maybe another function 
    
    pattern = '[\d]+[\.\d]*'
    # the pattern we're looking for is a number of digits, followed by 
    # a possible dot (if float), and some decimals.
    numbers = []
    # creates an empty list to store the matched patterns.
    
    for string in perc:
        numbers.append((re.match(pattern, string)).group())
    # I'm not using find all because for each string there would be 
    # a list of list. I'm looking to create a list of only numerical 
    # values. I'm matching the pattern for each string and appending 
    # empty list with results. 
    return [float(string) * 0.01 for string in numbers]
    # Then I'm switching the number to it's percentile. 
    # Can be done in 1 line, but I split it for readability.