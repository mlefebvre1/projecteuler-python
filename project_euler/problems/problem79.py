from typing import Iterator, List
from pathlib import Path
from ..utils.timeit import timeit


def generate_digit_candidates(logins: List[str]) -> Iterator[str]:
    digit_presence = [False] * 10
    for login in logins:
        for digit in login:
            digit_presence[int(digit)] = True
    for digit, presence in enumerate(digit_presence):
        if presence:
            yield str(digit)


def find_largest_digit(logins: List[str], digits_to_place: List[str]) -> str:
    largest_digit = [
        True if str(digit) in digits_to_place else False for digit in range(10)
    ]
    for login in logins:
        # taking len - 1 because the left digit cannot be the last digit, we need a digit to compare with..
        for i, digit_to_the_left in enumerate(login[0 : len(login) - 1]):
            # try every digit until we get one that is a digit to place
            if digit_to_the_left in digits_to_place:
                for digit_to_the_right in login[i + 1 :]:
                    # if a digit is to the right of another digit, that means it can't be the largest digit..
                    largest_digit[int(digit_to_the_right)] = False
    for digit, still_true in enumerate(largest_digit):
        if still_true:
            return str(digit)


@timeit
def problem79():
    """
    Passcode derivation
    Problem 79

    A common security method used for online banking is to ask the user for three random characters from a passcode. For
    example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
    317.

    The text file, keylog.txt, contains fifty successful login attempts.

    Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
    possible secret passcode of unknown length.

    """
    with open(f"{Path(__file__).parent}/data/problem79.txt", "r") as fp:
        logins = fp.read()

    logins = logins.split("\n")
    logins.remove("")

    digits_to_place = list(generate_digit_candidates(logins))
    passcode = ""
    while len(digits_to_place) > 0:
        digit = find_largest_digit(logins, digits_to_place)
        digits_to_place.remove(digit)
        passcode += digit
    return passcode


if __name__ == "__main__":
    problem79()
