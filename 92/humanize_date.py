from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2 * MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2 * HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2 * DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime):
        raise ValueError
    delta = (NOW - date)
    days, seconds = delta.days, delta.seconds
    if days < 0:
        raise ValueError
    print(days, seconds)
    total_seconds = seconds + days * DAY
    time_offset = list(filter(lambda x: total_seconds < x.offset, TIME_OFFSETS))
    if not time_offset:
        return date.strftime("%m/%d/%y")
    time_offset = time_offset[0]
    if time_offset.divider:
        return f"{time_offset.date_str.format(int(seconds / time_offset.divider))}"
    return f"{time_offset.date_str if seconds > MINUTE else time_offset.date_str.format(seconds)}"
