from ..utils.timeit import timeit

numbers_0_to_10 = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
numbers_10_to_20 = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
numbers_base_20_to_100 = [
    "unused",
    "unused",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def count_base10(n: int) -> int:
    nb_letters = 0
    if n < 10:
        nb_letters += len(numbers_0_to_10[n])
    elif 10 <= n < 20:
        nb_letters += len(numbers_10_to_20[n % 10])
    elif 20 <= n < 100:
        if str(n)[1] == "0":  # 20, 30, 40 .. etc.
            nb_letters += len(numbers_base_20_to_100[int(str(n)[0])])
        else:  # 21, 22.. 31, 32 .. 91.. 99
            nb_letters += len(numbers_base_20_to_100[int(str(n)[0])]) + len(
                numbers_0_to_10[int(str(n)[1])]
            )
    return nb_letters


def count_letters(n: int) -> int:
    nb_letters = 0
    if n < 100:  # 10 .. 99
        nb_letters += count_base10(n)
    elif n < 1000:
        base10 = int(str(n)[1:3])
        base100 = str(n)[0]
        if base10 == 0:  # 100, 200, 300 .. etc.
            nb_letters += len(numbers_0_to_10[int(base100)]) + len("hundred")
        else:  # 101, 102 .. etc.
            nb_letters += (
                len(numbers_0_to_10[int(base100)]) + len("hundred") + len("and")
            )
            nb_letters += count_base10(base10)
    else:  # 1000
        nb_letters += len("one") + len("thousand")
    return nb_letters


@timeit
def problem17():
    """
    Number letter counts
    Problem 17

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
    letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be
    used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
    (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
    British usage.
    """
    max_n = 1000
    nb_letters = 0
    for n in range(1, max_n + 1):
        nb_letters += count_letters(n)
    return nb_letters


if __name__ == "__main__":
    problem17()
