from typing import List, Set

from project_euler.number_theory.primes import sieves, is_prime

from project_euler.utils.timeit import timeit


def make_twice_a_square_list(max_n: int) -> List[int]:
    n = 1
    twice_a_square_list = []
    while True:
        twice_a_square = 2 * (n * n)
        twice_a_square_list.append(twice_a_square)
        n += 1
        if twice_a_square >= max_n:
            return twice_a_square_list


def make_conjecture_candidates(max_n: int) -> Set[int]:
    primes = sieves(max_n)
    twice_a_square_list = make_twice_a_square_list(max_n)
    candidates = set()
    for prime in primes:
        for twice_a_square in twice_a_square_list:
            candidate = prime + twice_a_square
            if (
                (candidate % 2)
                and not is_prime(candidate)
                and candidate != 1
                and candidate < max_n
            ):
                candidates.add(candidate)
    return candidates


def make_conjecture_presence_list(
    max_n: int, conjecture_candidates: Set[int]
) -> List[bool]:
    conjecture_list = [False for _ in range(max_n)]
    for candidate in conjecture_candidates:
        conjecture_list[candidate] = True
    return conjecture_list


@timeit
def problem46():
    """
    Goldbach's other conjecture
    Problem 46

    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
    twice a square.

        9 = 7 + 2×1^2
        15 = 7 + 2×2^2
        21 = 3 + 2×3^2
        25 = 7 + 2×3^2
        27 = 19 + 2×2^2
        33 = 31 + 2×1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """
    max_n, ans = 10000, "not found"
    conjecture_candidates = make_conjecture_candidates(
        max_n
    )  # right side of the equation
    conjecture_presence_list = make_conjecture_presence_list(
        max_n, conjecture_candidates
    )
    odd_composites = [
        True if n % 2 and not is_prime(n) and n != 1 else False for n in range(max_n)
    ]  # left side of the equation
    for n, (conjecture, odd_composite) in enumerate(
        zip(conjecture_presence_list, odd_composites)
    ):
        if conjecture != odd_composite:
            ans = n
            break
    return ans


problem46()
