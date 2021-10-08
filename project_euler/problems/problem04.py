from ..number_theory.palindrome import is_palindrome

from ..utils.timeit import timeit


@timeit
def problem04():
    """
    Largest palindrome product
    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    largest = 0
    for n1 in range(100, 999):
        for n2 in range(100, 999):
            prod = n1 * n2
            if prod > largest:
                if is_palindrome(prod):
                    largest = prod
    return largest


if __name__ == "__main__":
    problem04()
