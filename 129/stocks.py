from collections import defaultdict, Counter

import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0

    if cap.endswith('M'):
        return float(cap.strip('M').strip('$'))

    if cap.endswith('B'):
        return float(cap.strip('B').strip('$')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    total = sum(
        _cap_str_to_mln_float(sub['cap'])
        for sub in data
        if sub['industry'] == industry
    )

    return round(total, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    cap = [_cap_str_to_mln_float(d['cap']) for d in data if "cap" in d]
    symbol = [d["symbol"] for d in data if "symbol" in d]
    new_data = dict(zip(symbol, cap))
    new_data_sorted = dict(sorted(new_data.items(), key=lambda item: item[1], reverse=True))
    return list(new_data_sorted.keys())[0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    stock_data = Counter(
        stock["sector"]
        for stock in data
        if stock["sector"] != "n/a"
    )

    most_stocks, _ = stock_data.most_common()[0]
    least_stock, _ = stock_data.most_common()[-1]

    return most_stocks, least_stock
