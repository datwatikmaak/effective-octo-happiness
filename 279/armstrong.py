def is_armstrong(n: int) -> bool:
    number_of_digits = len(str(n))
    num_list = [int(i) for i in str(n)]
    total = sum((i ** number_of_digits) for i in num_list)
    return n < 10 or n == total
