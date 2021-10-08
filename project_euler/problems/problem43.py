import itertools
from typing import List

from ..number_theory.primes import sieves

from ..utils.timeit import timeit


def is_sub_string_divisible(n: str, primes: List[int]) -> bool:
    if n[5] == "5":  # Digit 6 needs to always be 5 because it always divided by 5
        for d, prime in enumerate(primes):
            if int(n[d + 1 : d + 4]) % prime != 0:
                return False
        else:
            return True
    else:
        return False


@timeit
def problem43():
    """
    Sub-string divisibility
    Problem 43

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
    order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    a = "1234567890"
    permutations = itertools.permutations(a)
    primes = list(sieves(17))

    sub_string_divisibles = filter(
        lambda permutation: True
        if is_sub_string_divisible("".join(permutation), primes)
        else False,
        permutations,
    )
    sub_string_divisibles_int = map(lambda n: int("".join(n)), sub_string_divisibles)
    return sum(sub_string_divisibles_int)


if __name__ == "__main__":
    problem43()
