from project_euler.number_theory.primes import sieves

from project_euler.utils.timeit import timeit


def generate_above_target():
    max_n, target = 100, 5000
    primes = sieves(max_n)
    nb_ways = [0] * (max_n + 1)
    nb_ways[0] = 1
    for prime in primes:
        for n in range(prime, max_n + 1):
            nb_ways[n] += nb_ways[n - prime]
            if nb_ways[n] > target:
                yield n


@timeit
def problem77():
    """
    Prime summations
    Problem 77

    It is possible to write ten as the sum of primes in exactly five different ways:

    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

    What is the first value which can be written as the sum of primes in over five thousand different ways?

    Same strategy as problem 76. Generate some n's above the target and find the smallest n above the target
    """
    candidates = generate_above_target()
    return min(candidates)


problem77()
