from typing import List

from ..number_theory.primes import distinct_primes_fast, sieves

from ..utils.timeit import timeit


def make_distinct_primes(n: int, primes: List[int]) -> List[int]:
    try:
        distinct_primes = list(distinct_primes_fast(n, primes))
    except:
        distinct_primes = []
    return distinct_primes


@timeit
def problem47():
    """
    Distinct primes factors
    Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
    numbers?
    """
    primes = list(sieves(1000))
    n = 646
    consecutive_integers = []
    while True:
        distinct_primes = make_distinct_primes(n, primes)
        if len(distinct_primes) == 4:
            consecutive_integers.append(n)
            if len(consecutive_integers) == 4:
                break
        else:
            consecutive_integers.clear()
        n += 1
    return consecutive_integers[0]


if __name__ == "__main__":
    problem47()
