from ..utils.timeit import timeit


@timeit
def problem01():
    """
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
    multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    max_n = 1000
    multipliers = [3, 5]
    multiples = set()
    for multiplier in multipliers:
        n = multiplier
        while n < max_n:
            multiples.add(n)
            n += multiplier
    return sum(multiples)


if __name__ == "__main__":
    problem01()
