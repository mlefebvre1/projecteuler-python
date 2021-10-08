from ..utils.timeit import timeit


def digit_uniqueness(n: int) -> bool:
    digit_array = [0] * 10
    for digit in str(n):
        digit_array[int(digit)] += 1
    for repetition in digit_array:
        if repetition > 1:
            return False
    else:
        return True


def same_digits(n1: int, n2: int) -> bool:
    for digit in str(n1):
        if digit not in str(n2):
            return False
    else:
        return True


@timeit
def problem52():
    """
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
    order.
    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """
    k = 1659999999  # Max will start with 16XXXXXXXX else 6x it would add a digit !!
    for n in range(
        100, k
    ):  # Could be optimize to wrap to restart to the next base 10 when the first digits are 166..
        if digit_uniqueness(n):
            for mult in range(2, 7):
                if not same_digits(n * mult, n):
                    break
            else:
                return n


if __name__ == "__main__":
    problem52()
