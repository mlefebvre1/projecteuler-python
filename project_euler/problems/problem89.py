from project_euler.utils.timeit import timeit
from pathlib import Path
from typing import Iterator


def roman_to_arab_number(roman_number) -> int:
    last_character_value = 1001
    roman_values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    arab_number = 0
    for roman_char in roman_number:
        current_character_value = roman_values[roman_char]
        if last_character_value < current_character_value:
            arab_number += current_character_value - (2 * last_character_value)
        else:
            arab_number += current_character_value
        last_character_value = current_character_value
    return arab_number


def arab_to_roman_number(arab_number) -> Iterator[str]:
    arab_num_cp = arab_number
    while arab_num_cp > 0:
        if arab_num_cp >= 1000:
            yield "M"
            arab_num_cp -= 1000
        elif arab_num_cp >= 900:  # CM case (900)
            yield "C"
            yield "M"
            arab_num_cp -= 900
        elif arab_num_cp >= 500:
            yield "D"
            arab_num_cp -= 500
        elif arab_num_cp >= 400:  # CD case (400
            yield "C"
            yield "D"
            arab_num_cp -= 400
        elif arab_num_cp >= 100:
            yield "C"
            arab_num_cp -= 100
        elif arab_num_cp >= 90:
            yield "X"
            yield "C"
            arab_num_cp -= 90
        elif arab_num_cp >= 50:
            yield "L"
            arab_num_cp -= 50
        elif arab_num_cp >= 40:
            yield "X"
            yield "L"
            arab_num_cp -= 40
        elif arab_num_cp >= 10:
            yield "X"
            arab_num_cp -= 10
        elif arab_num_cp >= 9:
            yield "I"
            yield "X"
            arab_num_cp -= 9
        elif arab_num_cp >= 5:
            yield "V"
            arab_num_cp -= 5
        elif arab_num_cp >= 4:
            yield "I"
            yield "V"
            arab_num_cp -= 4
        elif arab_num_cp >= 1:
            yield "I"
            arab_num_cp -= 1


def get_number_list() -> Iterator[str]:
    with open(Path(__file__).parent / "data/problem89.txt") as fp:
        data = fp.read()
    return data.split("\n")


@timeit
def problem89() -> int:
    """
    For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
    Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of
    writing a particular number.

    For example, it would appear that there are at least six ways of writing the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

    However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
    efficient, as it uses the least number of numerals.

    The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in
    valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this
    problem.

    Find the number of characters saved by writing each of these in their minimal form.

    Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

    """
    number_list = get_number_list()

    nb_initial_character = 0
    nb_character_after_opt = 0
    for n in number_list:
        nb_initial_character += len(n)
        arab_number = roman_to_arab_number(n)
        roman_number_optimized = list(arab_to_roman_number(arab_number))
        nb_character_after_opt += len(roman_number_optimized)

    return nb_initial_character - nb_character_after_opt


if __name__ == "__main__":
    problem89()
