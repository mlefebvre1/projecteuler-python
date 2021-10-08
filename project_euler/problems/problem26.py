from typing import Iterable

from project_euler.arithmetic.arithmetic import decimal_recurring_len
from ..number_theory.primes import sieves

from ..utils.timeit import timeit


def generate_reciprocal_len(limit_d: int) -> Iterable[int]:
    primes = sieves(limit_d)
    for prime in primes:
        yield decimal_recurring_len(prime), prime


@timeit
def problem26():
    """
    Reciprocal cycles
    Problem 26

    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
    2 to 10 are given:

        1/2	= 	0.5
        1/3	= 	0.(3)
        1/4	= 	0.25
        1/5	= 	0.2
        1/6	= 	0.1(6)
        1/7	= 	0.(142857)
        1/8	= 	0.125
        1/9	= 	0.(1)
        1/10	= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
    cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    """
    limit = 1000
    _, ans = max(generate_reciprocal_len(limit))
    return ans


if __name__ == "__main__":
    problem26()
