from math import sqrt
from typing import Iterator, Tuple


def triangular(n: int) -> int:
    return n * (n + 1) // 2


def infinite_triangle_generator() -> Iterator[int]:
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1


def square(n: int) -> int:
    return n**2


def pentagonal(n: int) -> int:
    return n * (3 * n - 1) // 2


def hexagonal(n: int) -> int:
    return n * (2 * n - 1)


def heptagonal(n: int) -> int:
    return n * (5 * n - 3) // 2


def octagonal(n: int) -> int:
    return n * (3 * n - 2)


def is_triangular(n: int, tol=0.00000001) -> bool:
    a, b, c = 0.5, 0.5, -n
    coefs = a, b, c
    return _is_root_an_integer(coefs, tol)


def is_pentagonal(n: int, tol=0.00000001) -> bool:
    a, b, c = 3, -1, -2 * n
    coefs = a, b, c
    return _is_root_an_integer(coefs, tol)


def is_hexagonal(n: int, tol=0.00000001) -> bool:
    a, b, c = 2, -1, -n
    coefs = a, b, c
    return _is_root_an_integer(coefs, tol)


def _is_root_an_integer(coefs: Tuple[int, int, int], tol=0.00000001) -> bool:
    a, b, c = coefs
    discriminant = pow(b, 2) - (4 * a * c)
    x = (-b + sqrt(discriminant)) / (2 * a)
    if abs(x - int(x)) < tol:
        return True
    else:
        return False
