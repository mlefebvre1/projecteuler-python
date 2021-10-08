from collections import defaultdict
from typing import Iterator, List, DefaultDict

from project_euler.utils.timeit import timeit


def cubics_generator() -> Iterator[int]:
    n = 1
    while True:
        yield pow(n, 3)
        n += 1


def is_a_permutation(n1: int, n2: int) -> bool:
    digits_presence = {"n1": [0] * 10, "n2": [0] * 10}
    for digit_n1, digit_n2 in zip(str(n1), str(n2)):
        digits_presence["n1"][int(digit_n1)] += 1
        digits_presence["n2"][int(digit_n2)] += 1
    for presence_n1, presence_n2 in zip(digits_presence["n1"], digits_presence["n2"]):
        if presence_n1 != presence_n2:
            return False
    else:
        return True


def cubics_by_digits_generator() -> Iterator[List[int]]:
    n = 1
    nb_digits = 1
    cubics = []
    while True:
        cubic = pow(n, 3)
        if len(str(cubic)) > nb_digits:
            yield cubics
            cubics = [cubic]
            nb_digits += 1
        else:
            cubics.append(cubic)
        n += 1


def map_by_sorted_digits(cubics: List[int]) -> DefaultDict[str, List[int]]:
    hashmap = defaultdict(list)
    for cubic in cubics:
        hash_ = "".join(sorted(str(cubic)))
        hashmap[hash_].append(cubic)
    return hashmap


def search_hash_with_correct_len_generator(
    hashmap: DefaultDict[str, List[int]], len_: int
) -> Iterator[int]:
    for hash_ in hashmap:
        if len(hashmap[hash_]) == len_:
            yield sorted(hashmap[hash_])[0]


@timeit
def problem62():
    """
    Cubic permutations
    Problem 62

    The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
    41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are cube.
    """
    cubics_gen = cubics_by_digits_generator()
    while True:
        cubics = next(cubics_gen)
        hashmap = map_by_sorted_digits(cubics)
        candidates = list(search_hash_with_correct_len_generator(hashmap, 5))
        if len(candidates) > 0:
            return min(candidates)


problem62()
