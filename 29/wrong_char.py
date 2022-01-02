import collections
import string

LETTERS = list(string.ascii_lowercase + string.ascii_uppercase)
NUMBERS = list(range(0, 10))


def get_index_different_char(chars):
    lst = []
    for c in chars:
        if c not in LETTERS and c not in NUMBERS:
            lst.append(0)
        else:
            lst.append(1)

    least_common = collections.Counter(lst).most_common()[-1][0]
    return [i for i, x in enumerate(lst) if x == least_common][0]
