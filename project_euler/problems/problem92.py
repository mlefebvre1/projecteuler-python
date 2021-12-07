from project_euler.utils.timeit import timeit
from typing import List


def generate_digit_sum_values(max_digit_sum: int) -> List[int]:
    mem = [0] * (max_digit_sum + 1)
    for n in range(2, max_digit_sum + 1):
        stack = []
        _n = n
        while True:
            digit_sum = sum((int(digit) * int(digit)) for digit in str(_n))
            if digit_sum == 89 or mem[digit_sum] == 89:
                mem[n] = 89
                for id_ in stack:
                    mem[id_] = 89
                break
            if digit_sum == 1 or mem[digit_sum] == 1:
                mem[n] = 1
                for id_ in stack:
                    mem[id_] = 1
                break
            if mem[digit_sum] == 0:
                stack.append(digit_sum)
                _n = digit_sum
    return mem


@timeit
def problem92():
    """
    Square digit chains
    Problem 92
    A number chain is created by continuously adding the square of the digits in a number to form a new number
    until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that
    EVERY starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """
    max_n = int(10e6)
    max_digit_sum = (
        9 * 9 * (len(str(max_n)) - 1)
    )  # max digit square sum would be 9^2 * 7

    mem = generate_digit_sum_values(max_digit_sum)

    nb_89 = len(list(filter(lambda x: x == 89, mem)))

    for n in range(max_digit_sum + 1, max_n):
        digit_sum = sum((int(digit) * int(digit)) for digit in str(n))
        if mem[digit_sum] == 89:
            nb_89 += 1

    return nb_89


if __name__ == "__main__":
    problem92()
