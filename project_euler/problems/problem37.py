from typing import Iterable

from ..number_theory.primes import sieves_range, is_prime

from ..utils.timeit import timeit


def is_truncatable(prime: int) -> bool:
    prime = str(prime)
    nb_digits = len(prime)
    for digit in range(1, nb_digits):
        trunc_left_to_right = int(prime[digit:nb_digits])
        trunc_right_to_left = int(prime[0 : nb_digits - digit])
        if not is_prime(trunc_left_to_right) or not is_prime(trunc_right_to_left):
            return False
    else:
        return True


def generate_truncatable_primes(max_n: int, max_truncatable: int) -> Iterable[int]:
    truncatable = 0
    primes = sieves_range(10, max_n)
    for prime in primes:
        if is_truncatable(prime):
            yield prime
            truncatable += 1
            if truncatable == max_truncatable:
                return


@timeit
def problem37():
    """
    Truncatable primes
    Problem 37

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
    left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
    379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """
    max_n, max_trunc = int(1e6), 11
    truncatable_primes = generate_truncatable_primes(max_n, max_trunc)
    return sum(truncatable_primes)


if __name__ == "__main__":
    problem37()
