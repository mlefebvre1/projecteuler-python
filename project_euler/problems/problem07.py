from project_euler.number_theory.primes import sieves

from project_euler.utils.timeit import timeit


@timeit
def problem07():
    """
    10001st prime
    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """
    max_prime = int(1e6)
    prime_index = 10001
    primes = list(sieves(max_prime))
    return primes[prime_index - 1]


if __name__ == "__main__":
    problem07()
