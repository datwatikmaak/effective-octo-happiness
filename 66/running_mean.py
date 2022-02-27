def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    result = []
    total = 0

    for i, s in enumerate(sequence, 1):
        total += s
        result.append(round(total / i, 2))

    return result
