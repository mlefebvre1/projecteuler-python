from project_euler.utils.timeit import timeit


@timeit
def problem16():
    """
    Power digit sum
    Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

    I guess it's too easy in python..
    """
    return sum(int(d) for d in str(pow(2, 1000)))


if __name__ == "__main__":
    problem16()
