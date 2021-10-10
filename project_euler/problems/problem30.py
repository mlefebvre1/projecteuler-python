from functools import reduce
from typing import Iterable

from project_euler.utils.timeit import timeit


def generate_fifth_powers(max_n: int) -> Iterable[int]:
    _EXP = 5
    _POWER = [n ** _EXP for n in range(0, 10)]
    for n in range(2, max_n):
        sum_ = reduce(lambda total, digit: total + _POWER[int(digit)], str(n), 0)
        yield sum_, n


@timeit
def problem30():
    """
    Digit fifth powers
    Problem 30

    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
    """
    max_n = 1000000
    generator = generate_fifth_powers(max_n)
    solutions = filter(lambda comp: comp[0] == comp[1], generator)
    return reduce(lambda total, solution: total + solution[1], solutions, 0)


if __name__ == "__main__":
    problem30()
