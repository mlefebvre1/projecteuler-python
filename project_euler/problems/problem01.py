from project_euler.utils.timeit import timeit
from project_euler.general import is_divisible_by


@timeit
def problem01():
    """
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    return sum((n for n in range(1000) if is_divisible_by(n, 3) or is_divisible_by(n, 5)))


if __name__ == "__main__":
    problem01()
