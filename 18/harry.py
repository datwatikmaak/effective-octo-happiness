import os
import string
import urllib.request

# data provided
from collections import Counter

tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

# open harry_text and make text lowercase
with open(harry_text, 'r', encoding='utf-8') as f:
    text_words = f.read().lower()

# open stopwords_file
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = f.read()

# remove all punctuations from the text
for char in string.punctuation:
    text_words = text_words.replace(char, "")

# remove all stopwords from text
no_stopwords = [word
                for word in text_words.split()
                if word not in stopwords]


def get_harry_most_common_word():
    # get the most common word from no_stopwords
    most_common_word = Counter(no_stopwords).most_common(1)[0][0]
    frequency = Counter(no_stopwords).most_common(1)[0][1]
    return most_common_word, frequency


get_harry_most_common_word()
