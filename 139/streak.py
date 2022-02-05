import re
from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = re.findall(r" (\d{4}-\d\d-\d\d) ", data)
    return {datetime.strptime(d, "%Y-%m-%d").date() for d in dates}


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    yesterday = TODAY - timedelta(days=1)
    count = 0
    while yesterday in dates:
        yesterday -= timedelta(days=1)
        count += 1

    return count + (1 if TODAY in dates else 0)
