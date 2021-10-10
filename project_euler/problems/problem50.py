from typing import List, Tuple, Iterable

from project_euler.number_theory.primes import sieves, is_prime

from project_euler.utils.timeit import timeit


def generator_consecutive_prime_sum(primes: List[int]) -> Iterable[Tuple[int, int]]:
    target = int(1e6)
    for i, pi in enumerate(primes):
        sum_ = pi
        nb_primes = 1
        for pj in primes[i + 1 :]:
            sum_ += pj
            nb_primes += 1
            if sum_ > target:
                sum_ -= pj  # remove the last prime that sum bust the target
                nb_primes -= 1
                break
        if is_prime(sum_):  # make sure we've got a prime number before adding the sum
            yield nb_primes, sum_


@timeit
def problem50():
    """
    Consecutive prime sum
    Problem 50

    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to
     953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    """
    max_prime = 100000
    primes = list(sieves(max_prime))
    consecutive_prime_sum_gen = generator_consecutive_prime_sum(primes)
    _, ans = max(consecutive_prime_sum_gen)
    return ans


if __name__ == "__main__":
    problem50()
