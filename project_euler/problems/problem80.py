from functools import reduce
from math import sqrt

from ..utils.timeit import timeit


class SqrtDigitExpansion:
    def __init__(self, nb_digits: int):
        self._nb_digits = nb_digits
        self._n = 0
        self._r = 0
        self._ans = ""

    def __str__(self):
        return f"{self._ans[0]}.{self._ans[1:]}"

    def calculate(self, n: int) -> str:
        self._n = n
        self._r = n * 100
        self._ans = str(self._find_first_digit())
        for _ in range(self._nb_digits - 1):
            self._ans += str(self._generate_next_digit())
            self._r *= 100
        return self._ans

    def get_ans_digit_sum(self) -> int:
        return reduce(lambda total, digit: total + int(digit), self._ans, 0)

    def calculate_and_get_digit_sum(self, n: int) -> int:
        self.calculate(n)
        return self.get_ans_digit_sum()

    def _find_first_digit(self) -> int:
        n = self._n
        for i in range(1, n + 1):
            if i * i > n:
                return i - 1

    def _generate_next_digit(self) -> int:
        for digit in range(1, 10):
            n = int(self._ans + str(digit))
            if (n * n) > self._r:
                return digit - 1
        else:
            return 9


@timeit
def problem80():
    """
    Square root digital expansion
    Problem 80

    It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
    expansion of such square roots is infinite without any repeating pattern at all.

    The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is
    475.

    For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal
    digits for all the irrational square roots.

    Solution : First we find all rational sqrt ( [1*1, 2*2, 3*3, ...]. Afterward for each irrational sqrt
    we do the sqrt using a special function that use integers to find the sqrt up to n digits by avoiding floating point
    because the precision is not good enough for 100 digits. It's important to note that the digit sum actually includes
    left and right digits from the comma. My initial error was to take only digits at the right of the comma.
    """
    nb_digits, nb_numbers = 100, 100
    exclude = [i * i for i in range(1, int(sqrt(nb_numbers)))]
    numbers = filter(lambda n_: n_ not in exclude, range(1, nb_numbers))
    sqrt_digit_expansion = SqrtDigitExpansion(nb_digits)
    return sum(sqrt_digit_expansion.calculate_and_get_digit_sum(n) for n in numbers)


if __name__ == "__main__":
    problem80()
