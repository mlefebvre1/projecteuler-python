from project_euler.number_theory.factor import proper_divisors_sum

from project_euler.utils.timeit import timeit


def get_abundants(max_n):
    for n in range(1, max_n):
        pds = proper_divisors_sum(n)
        if pds > n:
            yield n


@timeit
def problem23():
    """
    Non-abundant sums
    Problem 23

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
    the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
    sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
    of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
    be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
    even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
    less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """
    abundants = list(get_abundants(28123))
    # In a table identify all numbers that can be written by the sum of two abundant numbers

    can_be_written = [False] * 28123
    for n in (n for a in abundants for b in abundants if (n := a + b) < 28123):
        can_be_written[n] = True

    # Now that we know all the numbers that can be written as the sum of two abundants, find the sum of all n which
    # are not written as the sum of two abundants
    return sum(n for n, can in enumerate(can_be_written) if not can)


if __name__ == "__main__":
    problem23()
