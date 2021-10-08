from project_euler.geometry.pythagorean import pythagorean_triples

from ..utils.timeit import timeit


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
    ans = 0
    for triple in triples:
        if sum(triple) == 1000:
            ans = triple[0] * triple[1] * triple[2]
            break
    return ans


if __name__ == "__main__":
    problem09()
