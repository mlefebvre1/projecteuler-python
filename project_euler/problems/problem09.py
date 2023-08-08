from project_euler.geometry.pythagorean import pythagorean_triples
from project_euler.utils.timeit import timeit
from project_euler.general import prod


@timeit
def problem09():
    """
    Special Pythagorean triplet
    Problem 9

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    triples = list(pythagorean_triples(2000))
    return prod(next(triple for triple in triples if sum(triple) == 1000))


if __name__ == "__main__":
    problem09()
