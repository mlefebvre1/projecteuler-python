from math import log
from project_euler.utils.timeit import timeit
from pathlib import Path


@timeit
def problem99() -> int:
    """
    Largest exponential
    Problem 99
    Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that
    211 = 2048 < 37 = 2187.

    However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three
    million digits.

    Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a
    base/exponent pair on each line, determine which line number has the greatest numerical value.

    NOTE: The first two lines in the file represent the numbers in the example given above.

    It is much easier to calculate if we apply the log on both side else it would lead to too big numbers
    -> log(base1^exp1) > log(base2^exp2)
    -> exp1*log(base1) > exp2*log(base2)
    """
    with open(Path(__file__).parent / "data/problem99.txt") as f:
        numbers = f.read().splitlines()

    def generate_numbers():
        for line, number in enumerate(numbers):
            base, exp = number.split(",")
            base, exp = int(base), int(exp)
            # because the line counter is 0 based, but euler wants it 1 based
            yield exp * log(base), line + 1

    _, line = max(generate_numbers())
    return line


if __name__ == "__main__":
    problem99()
