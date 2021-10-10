from functools import reduce
from typing import Iterable

from project_euler.utils.timeit import timeit


def generate_digit_sum() -> Iterable[int]:
    for a in range(100):
        for b in range(100):
            yield reduce(lambda sum_, digit: sum_ + int(digit), str(a ** b), 0)


@timeit
def problem56():
    """
    Powerful digit sum
    Problem 56

    A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
    followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
    """
    digit_sums = generate_digit_sum()
    return max(digit_sums)


if __name__ == "__main__":
    problem56()
