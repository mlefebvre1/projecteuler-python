from project_euler.number_theory.series import fibonacci
from project_euler.utils.timeit import timeit
from project_euler.general import is_even
from itertools import takewhile


@timeit
def problem02():
    """
    Even Fibonacci numbers
    Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
    the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
    even-valued terms.
    """

    return sum(takewhile(lambda n: n < int(4e6), (n for n in fibonacci() if is_even(n))))


if __name__ == "__main__":
    problem02()
