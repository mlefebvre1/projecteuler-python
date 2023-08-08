from functools import reduce


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


def is_divisible_by(n, d):
    return n % d == 0


def prod(it):
    return reduce(lambda acc, x: acc * x, it, 1)
