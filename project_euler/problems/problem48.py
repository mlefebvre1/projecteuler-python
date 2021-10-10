from functools import reduce

from project_euler.utils.timeit import timeit


@timeit
def problem48():
    """
    Self powers
    Problem 48

    The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
    """

    k = 1000
    m = 10000000000
    return reduce(lambda sum_, n: (sum_ + pow(n, n) % m) % m, range(1, k + 1), 0)


if __name__ == "__main__":
    problem48()
