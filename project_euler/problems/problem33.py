from math import gcd
from typing import Iterable

from project_euler.utils.timeit import timeit


def is_non_trivial_two_digits_curious_fraction(numerator: int, denominator: int) -> bool:
    fraction = numerator / denominator
    simplified_fraction = 0.0
    numerator, denominator = str(numerator), str(denominator)
    if numerator[0] == denominator[1] and numerator[1] == denominator[0]:
        return False
    if numerator[0] == denominator[1] and denominator[0] != "0":
        simplified_fraction = int(numerator[1]) / int(denominator[0])
    elif numerator[1] == denominator[0] and denominator[1] != "0":
        simplified_fraction = int(numerator[0]) / int(denominator[1])
    if simplified_fraction == fraction:
        return True
    else:
        return False


def generate_non_trivial_two_digits_curious_fraction() -> Iterable[int]:
    _MAX = 99
    for numerator in range(10, _MAX + 1):
        for denominator in range(numerator, _MAX + 1):
            if is_non_trivial_two_digits_curious_fraction(numerator, denominator):
                yield numerator, denominator


@timeit
def problem33():
    """
    Digit cancelling fractions
    Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
    incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
    digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """
    numerator_total, denominator_total = 1, 1
    for numerator, denominator in generate_non_trivial_two_digits_curious_fraction():
        numerator_total *= numerator
        denominator_total *= denominator
    return int(denominator_total / gcd(denominator_total, numerator_total))


if __name__ == "__main__":
    problem33()
