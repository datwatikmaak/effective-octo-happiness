import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive an utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    zones = []
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError

        if pytz.utc.localize(utc).astimezone(pytz.timezone(tz)).hour in MEETING_HOURS:
            zones.append(True)

    return len(zones) == len(timezones)
