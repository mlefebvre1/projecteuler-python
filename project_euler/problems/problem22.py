from functools import reduce
from typing import List
from pathlib import Path
from project_euler.utils.timeit import timeit


def scores(names: List[str]) -> List[int]:
    rebase_value = -ord("A") + 1
    for index, name in enumerate(names):
        yield reduce(lambda score, letter: ord(letter) + score + rebase_value, name, 0) * (index + 1)


@timeit
def problem22():
    """
    Names scores
    Problem 22

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply
    this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is
    the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
    What is the total of all the name scores in the file?
    """
    with open(f"{Path(__file__).parent}/data/problem22.txt", "r") as fp:
        names = sorted(name.replace('"', "") for name in fp.read().split(","))
    return sum(scores(names))


if __name__ == "__main__":
    problem22()
