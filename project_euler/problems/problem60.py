from typing import List

from project_euler.number_theory.primes import sieves, is_prime

from project_euler.utils.timeit import timeit

_TARGET = 5


def find_5_concat_primes(_prime1: int, _primes: List[int], nb_primes: int) -> int:
    """for a given prime, test each prime up to 10000 if the property of concatenation and generate a new primes holds.
    Keep every primes that holds the property. Pass that new list and the next prime in that new list to this function
    again. Keep doing this recursively until we get a sequence of 5 primes which holds the property. At that point
    de-stack and return the value of each prime in the list."""
    if nb_primes >= _TARGET:  # found five primes!!, start un-stacking the primes!
        return _prime1
    concat_with_prime1_and_is_prime = list(
        filter(
            lambda _prime2: is_prime(int(f"{_prime1}{_prime2}"))
            and is_prime(int(f"{_prime2}{_prime1}")),
            _primes,
        )
    )
    for prime2 in concat_with_prime1_and_is_prime:
        ans = find_5_concat_primes(
            prime2, concat_with_prime1_and_is_prime, nb_primes + 1
        )
        if ans:  # de-stack here
            return ans + _prime1
    return 0


@timeit
def problem60():
    """
    Problem 60

    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
    the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
    primes, 792, represents the lowest sum for a set of four primes with this property.

    Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
    """
    max_n = 10000
    primes = list(sieves(max_n))
    for prime1 in primes:
        ans = find_5_concat_primes(prime1, primes, 1)
        if ans:
            return ans


problem60()
