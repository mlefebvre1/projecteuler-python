from math import factorial

from project_euler.utils.timeit import timeit


@timeit
def problem20():
    """
    Factorial digit sum
    Problem 20

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """
    n = factorial(100)
    digits_sum = 0
    for digit in str(n):
        digits_sum += int(digit)
    return digits_sum


if __name__ == "__main__":
    problem20()
