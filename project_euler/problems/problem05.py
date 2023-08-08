from math import pow, floor, log

from project_euler.number_theory.primes import sieves
from project_euler.utils.timeit import timeit
from project_euler.general import prod


@timeit
def problem05():
    """
    Smallest multiple
    Problem 5
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    Solution : Find the prime numbers up to 20. For each prime number, use the distinct prime numbers of each number
    from 1 to 20 to find the greatest number of occurences. Finally, the smallest positive number is the multiplication
    of all the primes numbers up to 20 with their greatest occurance.
    """
    return int(prod([pow(prime, floor(log(20, prime))) for prime in sieves(20)]))


if __name__ == "__main__":
    problem05()
