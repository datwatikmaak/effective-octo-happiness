april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    lines = calendar_output.splitlines()
    day_chars = lines[1].split()

    result = {}
    for line in lines[2:]:
        for i in range(7):
            if day_numbers := line[i * 3: i * 3 + 2].strip():
                result[int(day_numbers)] = day_chars[i]

    return result


get_weekdays(april_1981)
