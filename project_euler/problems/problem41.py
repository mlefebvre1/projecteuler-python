import itertools
from typing import Iterable

from project_euler.number_theory.primes import is_prime

from project_euler.utils.timeit import timeit


def generate_candidates() -> Iterable[int]:
    _N_LIST = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
    for n in _N_LIST:
        permutations = itertools.permutations(str(n))
        for permutation in permutations:
            permutation = int("".join(permutation))
            if is_prime(permutation):
                yield permutation


@timeit
def problem41():
    """
    Pandigital prime
    Problem 41

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    candidates = generate_candidates()
    return max(candidates)


if __name__ == "__main__":
    problem41()
