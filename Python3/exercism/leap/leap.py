def is_leap_year(year):
    """ This functions checks if a given year is a leap year."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0