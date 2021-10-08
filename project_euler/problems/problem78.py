from typing import Iterator, List

from project_euler.geometry.geometry import triangular

from project_euler.utils.timeit import timeit


def generalized_pentagonal_number_generator() -> Iterator[int]:
    pn, tn_1 = 0, 0
    n = 1
    while True:
        yield pn
        pn = triangular(n) + 2 * triangular(n - 1)
        n = -n if n > 0 else (-n) + 1  # n = 0, 1, -1, 2, -2, 3, -3...


def partition(n: int, partitions: List[int], pentagonals) -> int:
    """Return Number partition p(n) using the Euler Function
    p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
    Keep going utils n-k is negative
    """
    pentagonal_index = 1
    sign, sign_counter = 1, 0
    result = 0
    while True:
        k = pentagonals[pentagonal_index]
        index = n - k
        if index < 0:
            return result % int(1e6)
        result += sign * partitions[index]
        sign_counter = (sign_counter + 1) % 4
        sign = -1 if int(sign_counter / 2) else 1
        pentagonal_index += 1


@timeit
def problem78():
    """
    Coin partitions
    Problem 78

    Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five
    coins can be separated into piles in exactly seven different ways, so p(5)=7.

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

    Find the least value of n for which p(n) is divisible by one million
    """
    max_n = int(100e3)
    partitions = [0] * max_n
    pentagonal_gen = generalized_pentagonal_number_generator()
    pentagonals = [next(pentagonal_gen) for _ in range(max_n)]

    partitions[0] = 1
    for n in range(1, max_n):
        pn = partition(n, partitions, pentagonals)
        if pn == 0:
            return n
        partitions[n] = pn


problem78()
