import collections


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    de = collections.deque(string)

    if string.count(" ") == 0:
        de.rotate(n + 1) if n > 0 else de.rotate(n - 1)
    else:
        de.rotate(-n)

    return "".join(de)
