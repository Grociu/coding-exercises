""" This program calculates the date when you lived longet than a gigasecond.

Function add_gigasecond takes your birthday as argument.
"""
from datetime import timedelta

INTERVAL = 10 ** 9
timeframe = timedelta(seconds = INTERVAL)


def add_gigasecond(moment):
    """ Adds a gigasecond to your birthdate."""
    return moment + timeframe