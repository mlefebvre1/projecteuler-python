from functools import reduce

from project_euler.utils.timeit import timeit


@timeit
def problem48():
    """
    Self powers
    Problem 48

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """

    k = 1000
    m = 10000000000
    return reduce(lambda sum_, n: (sum_ + pow(n, n) % m) % m, range(1, k + 1), 0)


if __name__ == "__main__":
    problem48()
