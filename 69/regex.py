import re
from string import punctuation


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    regex = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
    return bool(re.search(regex, text))


def is_integer(number):
    """Return True if number is an integer"""
    regex = r"^(-?[\d])$"
    return bool(re.search(regex, str(number)))


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    regex = r"[\d|\w]-[\d|\w]"
    return bool(re.search(regex, text))


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parentheses:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    regex = r"\s\((\w+|\d+.\d)\)"
    return re.sub(regex, "", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    regex = r"[^\w\s]"
    splitted = re.split(regex, text)
    return [x.lstrip() for x in splitted if x]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r"\s{2,}", " ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    regex = r"[aeiou]{3}"
    return bool(re.search(regex, word))


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    regex = re.compile(r"(\d+/)(\d+/)(\d+)")
    return regex.sub(r"\2\1\3", date)


print(convert_emea_date_to_amer_date("31/03/2018"))
