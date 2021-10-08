from ..number_theory.primes import sieves

from ..utils.timeit import timeit


@timeit
def problem10():
    """
    Summation of primes
    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million
    """
    max_prime = int(2e6)
    primes = sieves(max_prime)
    return sum(primes)


if __name__ == "__main__":
    problem10()
