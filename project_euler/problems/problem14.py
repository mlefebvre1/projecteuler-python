from project_euler.utils.timeit import timeit
from project_euler.general import is_odd


def chain(n: int) -> int:
    chain_len = 0
    while n != 1:
        if is_odd(n):  # Skip a step since for an odd number : 3*n+1 always gives a even number
            n = (3 * n + 1) // 2
            chain_len += 2
        else:  # is even
            n = n // 2
            chain_len += 1
    return chain_len


@timeit
def problem14():
    """
    Longest Collatz sequence
    Problem 14

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
    proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    r = range(int(1e6 / 2), int(1e6))
    chains = zip(map(chain, r), r)
    (_, max_n) = max(chains)
    return max_n


if __name__ == "__main__":
    problem14()
