from typing import Iterable

from ..number_theory.primes import sieves_range, is_prime
from ..number_theory.rotations import rotations

from ..utils.timeit import timeit


def circular(all_rotations: Iterable[int]) -> bool:
    for n in all_rotations:
        if not is_prime(int(n)):
            return False
    else:
        return True


@timeit
def problem35():
    """
    Circular primes
    Problem 35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
    prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
    """
    max_prime = int(1e6)
    primes = sieves_range(2, max_prime)
    nb_circular = (
        2  # add 2 and 5, the only numbers that does not start with 1, 3, 7 or 9
    )
    for prime in primes:
        prime = str(prime)
        # consider checking only numbers that start with 1,3,7 or 9, else they are not prime
        if prime[0] == "1" or prime[0] == "3" or prime[0] == "7" or prime[0] == "9":
            if circular(rotations(prime)):
                nb_circular += 1
    return nb_circular


if __name__ == "__main__":
    problem35()
