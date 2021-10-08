from math import pow, floor, log

from ..number_theory.primes import sieves

from ..utils.timeit import timeit


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
    max_n = 20
    primes = sieves(max_n)
    prime_occurence = [0] * (max_n + 1)
    for prime in primes:
        prime_occurence[prime] = floor(log(max_n) / log(prime))

    smallest_positive_number = 1
    for prime, occurence in enumerate(prime_occurence):
        smallest_positive_number *= int(pow(prime, occurence))
    return smallest_positive_number


if __name__ == "__main__":
    problem05()
