from functools import reduce
from typing import Iterable

from project_euler.arithmetic.arithmetic import generate_binary_strings_n_digits
from project_euler.number_theory.primes import is_prime

from project_euler.utils.timeit import timeit


def make_number(i_: int, j_: int, s_: int, binary_string_: str) -> int:
    i_, i_index = str(i_), 0
    result = ""
    for digit in binary_string_:
        if digit == "0":
            result += i_[i_index]
            i_index += 1
        else:
            result += str(s_)
    return int(result + str(j_))


def generate_combination_values(i_: int, j_: int, binary_string_: str) -> Iterable[int]:
    for star in range(1, 10):
        yield make_number(i_, j_, star, binary_string_)


@timeit
def problem51():
    """
    Prime digit replacements
    Problem 51

    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
     13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
    seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
    56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same
    digit, is part of an eight prime value family.

    Candidates will be constructed like this :

    i: some number in a defined range. If i is 3 digits then i will be tested for 100 to 999
    * : replace all * on the number with the numbers 1 to 9
    j : the lat digit should be either 1,3,7 or 9

    i i i * j
    i i * i j
    i i * * j
    i * i i j
    i * i * j
    i * * i j
    i * * * j
    * i i i j
    * i i * j
    * i * i j
    * i * * j
    * * i i j
    * * i * j
    * * * i j
    * * * * j
    """
    nb_digits = 5  # we know the number we seek is at least 5 digits or more
    _LAST_DIGIT = [1, 3, 7, 9]
    while True:
        for j in _LAST_DIGIT:
            for binary_string in filter(
                lambda x: x != "".zfill(nb_digits - 1),
                generate_binary_strings_n_digits(nb_digits - 1),
            ):  # ignore the binary string with all 0's
                i_nb_digits = reduce(
                    lambda tot, x: tot + 1 if x == "0" else tot, binary_string, 0
                )
                for i in range(int(10 ** (i_nb_digits - 1)), int(10 ** i_nb_digits)):
                    combination_values = generate_combination_values(
                        i, j, binary_string
                    )
                    combination_values_that_are_prime = list(
                        filter(lambda x: is_prime(x), combination_values)
                    )
                    if len(combination_values_that_are_prime) == 8:
                        return combination_values_that_are_prime[0]
        nb_digits += 1


if __name__ == "__main__":
    problem51()
