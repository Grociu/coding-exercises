import re

def format_num(n):
    n_string = ""
    if len(str(n)) < 4:
        n_string = str(n) + n_string
    else:
        pattern = '\d{3}$'
        segment = re.search(pattern, str(n)).group()
        n_string = format_num(n // 1000) + "," + segment
    return n_string