from typing import Iterator

from project_euler.number_theory.primes import is_prime

from project_euler.utils.timeit import timeit


def quadratic_consecutive_primes(a: int, b: int) -> int:
    n = 0
    while 1:
        s = n**2 + a * n + b
        if s % 2:
            if not is_prime(s):
                break
        else:
            break
        n += 1
    return n


def generate_quadratic_consecutive_primes(
    lowerbound: int, upperbound: int
) -> Iterator[int]:
    for a in range(lowerbound, upperbound):
        for b in range(lowerbound, upperbound):
            yield quadratic_consecutive_primes(a, b), a, b


@timeit
def problem27():
    """
    Quadratic primes
    Problem 27

    Euler discovered the remarkable quadratic formula:

            n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
    However, when  n=40, 40^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41
    is clearly divisible by 41.

    The incredible formula n^2 -79n +1601 was discovered, which produces 80 primes for the consecutive values
    0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n^2 + an + b, where |a|<1000 and |b|<1000

    where |n| is the modulus/absolute value of
    e.g. |11| = 11 and |-4| = 4

    Find the product of the coefficients, a nd b, for the quadratic expression that produces the maximum number of
    primes for consecutive values of n, starting with n=0.
    """

    n, a, b = max(generate_quadratic_consecutive_primes(-1000, 1000))
    return a * b


if __name__ == "__main__":
    problem27()
