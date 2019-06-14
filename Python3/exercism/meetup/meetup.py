from datetime import date, timedelta


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"]

    first_day = date(year, month, 1)
    current_day, current_week = first_day, 1

    # Move current_date to the first day of the month that's equal
    # to the asked day_of_the_week.
    if current_day.weekday() != day_names.index(day_of_week):
        current_day += timedelta(
            days=(
                7
                - current_day.weekday()
                + day_names.index(day_of_week)
                ) % 7
        )

    # For the last day of the month, I want to move 21 or 28 days into the
    # future.
    if week == "last":
        current_day += timedelta(days=28)
        if current_day.month != first_day.month:
            current_day -= timedelta(days=7)

    # Week number is defined by cardinal statement starting with a number.
    if week in ['1st', '2nd', '3rd', '4th', '5th']:
        week_no = int(week[0])
        while current_week != week_no:
            current_day += timedelta(days=7)
            current_week += 1
        # It is possible, that the day is out of range.
        if current_day.month != first_day.month:
            raise MeetupDayException("No such day.")

    # The correct day is the first matching day between 13th and 19th.
    if week == "teenth":
        while current_day.day not in range(13, 20):
            current_day += timedelta(days=7)

    return current_day
