from datetime import timedelta, date


def tomorrow(today=None):
    return (today or date.today()) + timedelta(1)
