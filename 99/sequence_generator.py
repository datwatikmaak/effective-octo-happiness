from string import ascii_uppercase


def sequence_generator():
    while True:
        for char in enumerate(ascii_uppercase, start=1):
            yield char[0]
            yield char[1]
