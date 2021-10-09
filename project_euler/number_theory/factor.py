from math import ceil, sqrt
from typing import List


def factorize(n: int) -> List[int]:
    """
    Factorize a number n
    :param int n: A number which we will enumerate its factors
    :return: A list of factors for the number n
    """
    factors = [1]
    if n < 2:
        return factors
    sqrt_n = sqrt(n)
    for divider in range(2, ceil(sqrt_n)):
        if n % divider == 0:
            factors.append(divider)
            factors.append(int(n / divider))
    if n == (int(sqrt_n) * int(sqrt_n)):
        factors.append(int(sqrt_n))
    factors.append(n)
    return sorted(factors)


def number_of_factors(n: int) -> int:
    nb_factors = 1
    if n < 2:
        return nb_factors
    sqrt_n = sqrt(n)
    for divider in range(2, ceil(sqrt_n)):
        if n % divider == 0:
            nb_factors += 2
    if n == (int(sqrt_n) * int(sqrt_n)):
        nb_factors += 1
    nb_factors += 1
    return nb_factors


def proper_divisors_sum(n: int) -> int:
    """
    Find the proper divisor sum for the number n. The proper divisors are the factors of a number excluding the number
    itself.
    :param int n: A number for which we find the proper divisor sum
    :return: The proper divisor sum for the number n
    """
    proper_div_sum = 1
    if n < 2:
        return proper_div_sum
    sqrt_n = sqrt(n)
    for divider in range(2, ceil(sqrt_n)):
        if n % divider == 0:  # if it's divisible, we found 2 divisors at once!
            proper_div_sum += divider
            proper_div_sum += int(n / divider)
    if n == (int(sqrt_n) * int(sqrt_n)):
        proper_div_sum += int(sqrt_n)
    return proper_div_sum


def factor_sum(n: int) -> int:
    """
    Find the factor sum for the number n.
    :param int n: A number for which we find the factor sum
    :return: The factor sum for the number n
    """
    return proper_divisors_sum(n) + n
