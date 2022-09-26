from math import sqrt

from project_euler.number_theory.primes import is_prime

from project_euler.utils.timeit import timeit


@timeit
def problem03():
    """
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    k = 600851475143
    candidates = filter(lambda n: (k % n == 0) and is_prime(n), range(1, int(sqrt(k))))
    return max(candidates)


if __name__ == "__main__":
    problem03()
