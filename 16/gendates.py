from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date_list = []
    curr_date = PYBITES_BORN + timedelta(days=100)
    for _ in range(1, 11):
        date_list.append(curr_date)
        curr_date += timedelta(days=100)
    return date_list
