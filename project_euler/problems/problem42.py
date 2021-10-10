from functools import reduce
from typing import List, Iterable
from pathlib import Path
from project_euler.geometry.geometry import triangular

from project_euler.utils.timeit import timeit


def generate_triangles(max_: int) -> List[int]:
    n = 0
    while True:
        t = triangular(n)
        yield t
        n += 1
        if t >= max_:
            return


def generate_words_sum(words: List[str]) -> Iterable[int]:
    for word in words:
        yield reduce(
            lambda total, char: total + (ord(char) - 64) if char != '"' else total,
            word,
            0,
        )


@timeit
def problem42():
    """
    Coded triangle numbers
    Problem 42

    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
    we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
    triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
    """
    with open(f"{Path(__file__).parent}/data/problem42.txt", "r") as fp:
        words = str(fp.read()).split(",")
        fp.close()

    triangles = list(generate_triangles(max(generate_words_sum(words))))
    return reduce(
        lambda total, word_sum: total + 1 if word_sum in triangles else total,
        generate_words_sum(words),
        0,
    )


if __name__ == "__main__":
    problem42()
