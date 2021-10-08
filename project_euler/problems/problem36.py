from typing import Iterable

from ..number_theory.palindrome import is_palindrome

from ..utils.timeit import timeit


def generate_both_bases_palindrome(max_n: int) -> Iterable[int]:
    for n in range(0, max_n):
        n_bin = bin(n)[2:]
        if is_palindrome(n) and is_palindrome(n_bin):
            yield n


@timeit
def problem36():
    """
    Double-base palindromes
    Problem 36

    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """
    max_n = int(1e6)
    palindromes = generate_both_bases_palindrome(max_n)
    return sum(palindromes)


if __name__ == "__main__":
    problem36()
