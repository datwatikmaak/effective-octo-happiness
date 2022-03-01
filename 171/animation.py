from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
       Takes seconds argument = time for the spinner to run.
       Does not return anything, only prints to stdout."""
    time_end = time() + seconds
    spin = cycle(SPINNER_STATES)
    for s in spin:
        print(f"{s}\r", end="", flush=True)
        sleep(STATE_TRANSITION_TIME)
        if time() > time_end:
            break


if __name__ == '__main__':
    spinner(2)
