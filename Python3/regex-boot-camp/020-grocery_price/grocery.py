import re

def get_prices(lst):
    return [float(price) for price in re.findall("\d+\.\d+", "".join(lst))]
