import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    exclude = set(string.punctuation)
    return ''.join(char for char in input_string if char not in exclude)
