from math import log2, floor
from typing import Iterable


def generate_binary_strings_up_to_n(n: int) -> Iterable[str]:
    size = floor(log2(n)) + 1
    for i in range(n + 1):
        yield format(i, "b").zfill(size)


def generate_binary_strings_n_digits(size: int) -> Iterable[str]:
    for i in range(2 ** size):
        yield format(i, "b").zfill(size)


def decimal_division(n, nb_digits):
    """
    Generate the decimal representation of 1/n up to 'nb_digits' digits
    """
    decimals = []
    a = 10
    for _ in range(nb_digits):
        decimals.append(int(a / n))
        a = (a % n) * 10
    return "".join(map(str, decimals))


def decimal_recurring_len(n: int) -> int:
    """
    Calculate the number of digits of the recurrence of decimal
    """
    nb_digits = len(str(n))
    decimal = decimal_division(n, n * 2)
    # Trying to find this sequence again, for relatively small numbers (< 1000) checking 3 digits only is enough
    target = decimal[0:nb_digits]
    for n in range(nb_digits, len(decimal)):
        if decimal[n : n + nb_digits] == target:
            return n
    else:
        return 1


def pandigital_validation(n, start, stop):
    presence_status = [0] * (stop + 1)
    for digit in str(n):
        presence_status[int(digit)] += 1
    for digit, presence in enumerate(presence_status):
        if digit < start:
            if presence != 0:
                return False
        else:
            if presence != 1:
                return False
    else:
        return True
