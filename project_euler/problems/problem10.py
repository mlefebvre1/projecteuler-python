from project_euler.number_theory.primes import sieves

from project_euler.utils.timeit import timeit


@timeit
def problem10():
    """
    Summation of primes
    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million
    """
    return sum(sieves(int(2e6)))


if __name__ == "__main__":
    problem10()
