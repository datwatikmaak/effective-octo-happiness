def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    accents = []
    for char in text.lower():
        if len(char) == len(char.encode()):
            continue
        if char in accents:
            continue
        else:
            accents.append(char)

    return sorted(accents)
