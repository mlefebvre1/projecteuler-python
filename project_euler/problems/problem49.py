import itertools
from typing import Set, Iterable, List

from project_euler.number_theory.primes import sieves, is_prime

from project_euler.utils.timeit import timeit


def generate_candidates(primes: Iterable[int]) -> Iterable[Set[int]]:
    """For each primes generate the permutations, keep only the permutations that contains 4 digits and are primes"""
    for prime in primes:
        permutations = map(
            lambda x: int("".join(x)), itertools.permutations(str(prime))
        )
        permutations_4_digits = filter(lambda x: x >= 1000, permutations)
        yield sorted(set(filter(lambda x: is_prime(x), permutations_4_digits)))


def check_three_terms_increment(set_: Set[int]) -> bool:
    list_from_set = list(set_)
    for i, ki in enumerate(list_from_set):
        for kj in list_from_set[i + 1 :]:
            increment = kj - ki
            next_num = kj + increment
            if next_num in list_from_set:
                return True
    else:
        return False


def remove_duplicates(candidates: Iterable[Set[int]]) -> List[Set[int]]:
    result = list()
    for candidate in candidates:
        if candidate not in result:
            result.append(candidate)
    return result


def extract_the_correct_terms_and_concat(candidate: Set[int]) -> str:
    candidate_set_in_list = list(candidate)
    for i, ki in enumerate(candidate_set_in_list):
        for kj in candidate_set_in_list[i + 1 :]:
            increment = kj - ki
            next_num = kj + increment
            if next_num in candidate_set_in_list:
                return str(ki) + str(kj) + str(next_num)


@timeit
def problem49():
    """
    Prime permutations
    Problem 49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
     (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
     one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
    """
    k = 9876
    four_digit_primes = filter(lambda _prime: _prime >= 1000, sieves(k))
    candidates = generate_candidates(four_digit_primes)
    candidates_with_len_3_or_more = filter(lambda set_: len(set_) >= 3, candidates)
    candidates_with_no_duplicates = remove_duplicates(candidates_with_len_3_or_more)
    candidates_with_all_criteria = filter(
        lambda _candidate: check_three_terms_increment(_candidate),
        candidates_with_no_duplicates,
    )
    final_candidate = filter(
        lambda _candidate: 1487 not in _candidate, candidates_with_all_criteria
    )
    return extract_the_correct_terms_and_concat(next(final_candidate))


problem49()
