from math import sqrt, ceil
from typing import List, Iterator, Tuple

from project_euler.utils.timeit import timeit


def matrix2x2_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def apply_shifts(a_init: int, b_init: int, c_init: int) -> Iterator[str]:
    a, b, c = a_init, b_init, c_init
    while 1:
        T = a + 2 * b + c
        if T < 0:  # The total is less than 0, we need to apply a right shift
            a, b, c = right_step(a, b, c)
            yield "R"
        else:  # The total is greater than 0, we need to apply a left shift
            a, b, c = left_step(a, b, c)
            yield "L"
        if a == a_init and b == b_init and c == c_init:  # If we recover the initial matrix, this indicates we are done
            break


def left_step(a: int, b: int, c: int) -> Tuple[int, int, int]:
    return a + 2 * b + c, b + c, c


def right_step(a: int, b: int, c: int) -> Tuple[int, int, int]:
    return a, a + b, a + 2 * b + c


def generate_d_solutions(_Ds: Iterator[int]) -> [Tuple[int, int]]:
    step_matrix = {"L": [[1, 0], [1, 1]], "R": [[1, 1], [0, 1]]}
    for D in _Ds:
        steps = apply_shifts(1, 0, -D)
        _N = matrix2x2_mult(step_matrix[next(steps)], step_matrix[next(steps)])  # initial step
        for step in steps:
            _N = matrix2x2_mult(_N, step_matrix[step])
        yield D, _N[0][0]


@timeit
def problem66():
    """
    Diophantine equation

    Problem 66

    Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

    For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

    It can be assumed that there are no solutions in positive integers when D is square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

    32 – 2×22 = 1
    22 – 3×12 = 1
    92 – 5×42 = 1
    52 – 6×22 = 1
    82 – 7×32 = 1

    Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

    Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

    The solution is based on this paper by N.J. Wilberger : https://arxiv.org/pdf/0806.2490.pdf
    """

    end = 1000
    squared = [n * n for n in range(1, ceil(sqrt(end + 1)))]
    _Ds = filter(lambda x: x not in squared, range(2, end + 1))
    solutions = generate_d_solutions(_Ds)
    _D, _ = max(solutions, key=lambda i: i[1])
    return _D


if __name__ == "__main__":
    problem66()
