from math import ceil, gcd

from project_euler.utils.timeit import timeit


@timeit
def problem73():
    """
    Counting fractions in a range
    Problem 73

    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced
    proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 3 fractions between 1/3 and 1/2.

    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
    """
    k = int(12000)
    lower_bound = 1 / 3
    upper_bound = 1 / 2
    nb_fractions = 0
    for d in range(4, k + 1):
        n_lower = ceil(d * lower_bound)
        n_upper = ceil(d * upper_bound)
        for n in range(n_lower, n_upper):
            if (
                n % 2 or d % 2
            ):  # make sure n and d are not both even, so we can save the gcd calculation
                if gcd(n, d) == 1:
                    nb_fractions += 1
    return nb_fractions


problem73()
