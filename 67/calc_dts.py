from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return (start_100days + timedelta(days=100)).strftime("%Y-%m-%d")


print(get_hundred_days_end_date())


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    num_days = pycon_date - pybites_founded
    return int(num_days.days)


print(get_days_between_pb_start_first_joint_pycon())
