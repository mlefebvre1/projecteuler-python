from math import sqrt

from ..utils.timeit import timeit


def sqrt_cf_expansion_generator(n):
    m0, d0, a0 = 0, 1, int(sqrt(n))
    mn, dn, an = m0, d0, a0
    criteria = 2 * a0
    yield a0
    while an != criteria:
        mn = dn * an - mn
        dn = (n - pow(mn, 2)) / dn
        an = int((a0 + mn) / dn)
        yield an


@timeit
def problem64():
    """
    Odd period square roots
    Problem 64

    All square roots are periodic when written as continued fractions and can be written in the form:

    For example, let us consider

    If we continue we would get the following expansion:

    The process can be summarised as follows:

    It can be seen that the sequence is repeating. For conciseness, we use the notation
    sqrt(23) = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

    The first ten continued fraction representations of (irrational) square roots are:

    See : https://projecteuler.net/problem=64

    Exactly four continued fractions, have an odd period.

    How many continued fractions for have an odd period?
    """
    k = 10000
    exclude_list = [n * n for n in range(2, k)]
    possible_n = filter(lambda n: n not in exclude_list, range(2, k + 1))
    odd_period_sqrts = filter(
        lambda n: (len(list(sqrt_cf_expansion_generator(n))) - 1) % 2, possible_n
    )
    return len(list(odd_period_sqrts))


if __name__ == "__main__":
    problem64()
