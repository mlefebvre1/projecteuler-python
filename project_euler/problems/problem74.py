from functools import reduce
from math import factorial

from project_euler.utils.timeit import timeit

chain_map = [0] * (6 * factorial(9) + 1)  # worst case is the starting number 999999
factorials = [factorial(n) for n in range(10)]
chain_ending = [1, 2, 145, 169, 363601, 1454, 871, 45361, 872, 45362, 40585]
chain_ending_value = {
    "1": 1,
    "2": 1,
    "169": 3,
    "363601": 3,
    "1454": 3,
    "871": 2,
    "45361": 2,
    "872": 2,
    "45362": 2,
    "145": 0,
    "40585": 0,
}


def chain(n: int) -> int:
    cnt = 1
    while True:
        n = get_next_n(n)
        if n in chain_ending:
            return cnt + chain_ending_value[str(n)]
        cnt += 1


def get_next_n(n: int) -> int:
    if chain_map[n] == 0:
        next_n = reduce(lambda total, digit: total + factorials[int(digit)], str(n), 0)
        chain_map[n] = next_n
        return next_n
    else:
        return chain_map[n]


@timeit
def problem74():
    """
    Digit factorial chains
    Problem 74

    The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

    Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
    that there are only three such loops that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

    It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)

    Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
    number below one million is sixty terms.

    How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
    """
    max_n = int(1e6)
    cnt = 0
    for n in range(0, max_n):
        if chain(n) == 60:
            cnt += 1
    return cnt


if __name__ == "__main__":
    problem74()
