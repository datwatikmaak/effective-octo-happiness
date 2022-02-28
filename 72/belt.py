from collections import OrderedDict
from itertools import filterfalse

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()

ninjas = OrderedDict(zip(scores, belts))
minimum_score, maximum_score = min(scores), max(scores)


def get_belt(user_score):
    if user_score < minimum_score:
        return None
    return ninjas[list(filterfalse(lambda x: x > user_score, ninjas.keys()))[-1]]
