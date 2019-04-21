from datetime import timedelta

interval = 10 ** 9
timeframe = timedelta(seconds = interval)

def add_gigasecond(moment):
    return moment + timeframe
