from functools import reduce
from typing import List

from project_euler.utils.timeit import timeit


def make_distinct_primes_by_n(max_n: int) -> List[List[int]]:
    sieved = [[] for _ in range(max_n + 1)]
    for n in range(2, max_n + 1):
        if not sieved[n]:
            for x in range(n + n, max_n + 1, n):
                sieved[x].append(n)

    for n in range(2, max_n + 1):
        if not sieved[n]:
            sieved[n].append(n)
    return sieved


def generate_phi_by_n():
    max_n = int(1e6)
    distinct_primes_by_n = make_distinct_primes_by_n(max_n)
    for n, distinct_primes in enumerate(distinct_primes_by_n):
        if n >= 2:
            phi = int(
                reduce(
                    lambda result, prime: result * (1 - 1 / prime) if not (n % prime) else result,
                    distinct_primes,
                    n,
                )
            )

            yield phi


@timeit
def problem72():
    """
    Counting fractions
    Problem 72

    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced
    proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 21 elements in this set.

    How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

    The problem can be reformulated as find the sum of phi(n) : 2 <= n <= 1000000
    """
    return sum(generate_phi_by_n())


if __name__ == "__main__":
    problem72()
