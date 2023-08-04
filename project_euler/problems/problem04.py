from project_euler.number_theory.palindrome import is_palindrome

from project_euler.utils.timeit import timeit


@timeit
def problem04():
    """
    Largest palindrome product
    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
    is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    return max(n1 * n2 for n1 in range(100, 999) for n2 in range(100, 999) if is_palindrome(n1 * n2))


if __name__ == "__main__":
    problem04()
