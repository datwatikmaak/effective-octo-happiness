from itertools import combinations


def find_number_pairs(numbers, N=10):
    return sorted([(a, b) for a, b in combinations(numbers, 2) if a + b == N])
