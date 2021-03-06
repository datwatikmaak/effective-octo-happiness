import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentences = re.findall(r"([A-Z].+?[.?!])\s(?=[A-Z]|$)", text, re.DOTALL)
    return [sentence.replace("\n", " ") for sentence in sentences]
