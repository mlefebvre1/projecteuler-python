from ..utils.timeit import timeit


@timeit
def problem76():
    """
    Counting summations
    Problem 76

    It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

    How many different ways can one hundred be written as a sum of at least two positive integers?

    Same strategy as problem 31, use dynamic programming, it can be seen that the current nnb of ways will be
    the current nb of ways + the nb of ways of closest multiple current multiple i
    """
    max_n = 100
    nb_ways = [0] * (max_n + 1)
    nb_ways[0] = 1
    for multiple in range(1, max_n):
        for n in range(multiple, max_n + 1):
            nb_ways[n] = nb_ways[n] + nb_ways[n - multiple]
    return nb_ways[max_n]


if __name__ == "__main__":
    problem76()
