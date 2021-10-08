from math import factorial

from project_euler.utils.timeit import timeit


def generate_combinatorics():
    factorials = [factorial(n) for n in range(0, 101)]
    for n in range(23, 100 + 1):
        for r in range(0, n):
            yield factorials[n] / (factorials[r] * factorials[n - r])


@timeit
def problem53():
    """
    Combinatoric selections
    Problem 53

    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    It is not until n = 23 that the value exceed one-million c(23,10) = 1144066

    How many, not necessarily distinct, values of c(n,r) for 1 n < 100 are greater than one-million
    """
    target_value = int(1e6)
    combinatorics = generate_combinatorics()
    combinatorics_greater_than_target = filter(
        lambda c: c > target_value, combinatorics
    )
    return len(list(combinatorics_greater_than_target))


problem53()
