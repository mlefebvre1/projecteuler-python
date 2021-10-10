from math import sqrt
from typing import Iterator, Tuple

from project_euler.number_theory.primes import sieves

from project_euler.utils.timeit import timeit


def generate_phi_from_2_primes() -> Iterator[Tuple[int, int]]:
    """
    For n/phi(n) to be minimal, we need a large number with not many factors, hence 2. This means, we are
    looking for the product of 2 primes which produces the closest number possible to 10^7. The answer should be 2
    primes near sqrt(10^7). To give us room, we extend the search space with primes up to 2*sqrt(10^7) which is large
    enough to find the answer we are looking for.
    """
    max_n = int(1e7)
    primes = list(sieves(2 * int(sqrt(max_n))))
    for i, p1 in enumerate(primes):
        for p2 in primes[i:]:
            n, phi = p1 * p2, (p1 - 1) * (p2 - 1)
            if n > max_n:
                break
            yield n, phi


def generate_ratios(candidates) -> Iterator[Tuple[int, float]]:
    for n, phi in candidates:
        if sorted(str(n)) == sorted(str(phi)):
            yield n, n / phi


@timeit
def problem70():
    """
    Totient permutation
    Problem 70
    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
    numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
    than nine and relatively prime to nine, φ(9)=6.
    The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

    Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
    """
    candidates = generate_phi_from_2_primes()
    ratios = generate_ratios(candidates)
    return min(ratios, key=lambda x: x[1])[0]


if __name__ == "__main__":
    problem70()
