from functools import reduce
from math import factorial
from typing import Iterable

from project_euler.utils.timeit import timeit


def generate_curious_number(max_n: int) -> Iterable[int]:
    for n in range(3, max_n + 1):
        digits_factorial_sum = reduce(lambda sum_, digit: sum_ + factorial(int(digit)), str(n), 0)
        if digits_factorial_sum == n:
            yield n


@timeit
def problem34():
    """
    Digit factorials
    Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
    """
    _END = 100000  # found by trial and error..
    curious_numbers = generate_curious_number(_END)
    return sum(curious_numbers)


if __name__ == "__main__":
    problem34()
