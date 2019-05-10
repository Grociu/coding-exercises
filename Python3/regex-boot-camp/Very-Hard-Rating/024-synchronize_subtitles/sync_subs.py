import re
import datetime


def sync_subs(subtitles, timeIncrement):
    pattern = '\d{2}:[0-5][0-9]:[0-5][0-9],\d{3}'
    # Finds all the patterns in the subtitles and the Increment
    timer_str =  re.findall(pattern, subtitles + timeIncrement)
    # If the timeIncrement is formatted incorectly, the list will be even.
    if len(timer_str) % 2 == 0:
        return "There is a problem with the second argument"
    # Parses the timer into a timedelta object.
    timer_t = []
    for timer in timer_str:
        MatchObj = re.match('(\d{2}):([0-5][0-9]):([0-5][0-9]),(\d{3})', timer)
        timer_t.append(
            datetime.timedelta(
                hours = int(MatchObj.group(1)),
                minutes = int(MatchObj.group(2)),
                seconds= int(MatchObj.group(3)),
                microseconds = int(MatchObj.group(4)) * 1000)
            )
    # perform operation, and construct the result
    for i in range(len(timer_t) - 1):
        timer_t[i] += timer_t[-1]
        subtitles = subtitles.replace(
            timer_str[i], 
            f"{(timer_t[i].seconds) // 3600:02d}:" +
            f"{((timer_t[i].seconds // 60) % 60):02d}:"+
            f"{timer_t[i].seconds % 60:02d}," 
            f"{timer_t[i].microseconds}"[:-3]
            )
    return subtitles

