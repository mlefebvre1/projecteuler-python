from project_euler.utils.timeit import timeit
from project_euler.geometry.pythagorean import pythagorean_triples
from typing import Iterator


def all_pythagorean_splits(M: int) -> Iterator[int]:
    for triplet in sorted(pythagorean_triples(M), key=lambda x: x[0]):
        yield from pythagorean_splits(triplet)


def pythagorean_splits(triplet) -> Iterator[int]:
    a, b, _ = triplet
    for n1 in range(1, a):
        n2 = b - n1
        if n1 > n2:
            break
        if n2 <= a:
            yield a
        if n1 == n2:
            break

    for n1 in range(1, b):
        n2 = a - n1
        if n1 > n2:
            break
        if n2 <= a:
            yield b
        if n1 == n2:
            break


@timeit
def problem86() -> int:
    """
    Cuboid route
    Problem 86
    A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
    By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is
    shown on the diagram.
    However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always
    have integer length.
    It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a
    maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value
    of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
    Find the least value of M such that the number of solutions first exceeds one million.
    """
    TRIPLET_MAX = 4000  # tryed multiple values, and it turns out that the the solution settles to 1818 for M > 4000
    nb = 0
    prev = 0
    for solution in sorted(all_pythagorean_splits(TRIPLET_MAX)):
        if prev != solution:
            if nb > int(1e6):
                return prev
            prev = solution
        nb += 1


if __name__ == "__main__":
    problem86()
