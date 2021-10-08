from math import sqrt, ceil
from typing import List, Iterator


def sieves(k: int) -> Iterator[int]:
    """
    Generate the prime numbers <= k
    """
    sieved = [False] * (k + 1)
    if k <= 2:
        yield 2
    if k <= 3:
        yield 2
        yield 3

    for n in range(2, ceil(sqrt(k))):
        if not sieved[n]:
            for x in range(n + n, k + 1, n):
                sieved[x] = True
    for n in range(2, k + 1):
        if not sieved[n]:
            yield n


def sieves_range(n1: int, n2: int) -> List[int]:
    """
    Generate the prime numbers in the range n1 < primes <= n2
    """
    sieve = list(sieves(n2))
    if not n1 < n2:
        raise Exception("n1 must strictly be smaller than n2")
    for index, prime in enumerate(sieve):
        if prime >= n1:
            return sieve[index:]


def is_prime(n: int) -> bool:
    """
    Test if the integer n is a prime number or not.
    """
    i = 5
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif ((n % 2) == 0) or ((n % 3) == 0):
        return False
    while (i * i) <= n:
        if (n % i) == 0 or ((n % (i + 2)) == 0):
            return False
        i = i + 6
    return True


def distinct_primes_fast(n: int, primes: List[int]) -> Iterator[int]:
    """
    Return a generator object for the distinct primes of the number n.
    :param int n: A number for which we determine the distinct primes
    :param list primes: The list of prime numbers up to sqrt(n)
    :return: The list of distinct primes of the number n
    """

    primes = iter(primes)
    while 1:
        prime = next(primes)
        if n % prime == 0:
            yield prime
        while n % prime == 0:
            n /= prime
            if n == 1:
                return


def distinct_primes(n) -> Iterator[int]:
    """
    Return the list of the distinct primes of the number n. If sieves for the number n
    is already available, use the function "distinct_primes_fast" instead.
    :param int n: A number for which we determine the distinct primes
    :return: The list of distinct primes of the number n
    """
    sieve = list(sieves(n))
    yield from distinct_primes_fast(n, sieve)
