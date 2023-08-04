from project_euler.utils.timeit import timeit
from numpy import array, genfromtxt
from pathlib import Path


@timeit
def problem82() -> int:
    """
    The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left
    column and finishing in any cell in the right column, and only moving up, down, and
    right, is indicated in red and bold; the sum is equal to 994.

    https://projecteuler.net/problem=82

    Find the minimal path sum from the left column to the right column in matrix.txt
    (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
    """
    matrix = array(
        genfromtxt(
            Path(__file__).parent / "data/problem82.txt",
            delimiter=",",
            skip_header=False,
            dtype=int,
        )
    )

    x_len, y_len = matrix.shape
    _matrix = matrix.copy()

    # column only.. set worst cases
    for y in range(y_len):
        for x in range(1, x_len):
            _matrix[y][x] += _matrix[y][x - 1]

    min_path_stable_threshold = 10
    min_path_stable_cnt = 0
    previous_min_path = 0
    while True:
        for y in range(y_len):
            for x in range(1, x_len):
                if y == 0:
                    _matrix[y][x] = min(_matrix[y + 1][x], _matrix[y][x - 1]) + matrix[y][x]
                elif y == y_len - 1:
                    _matrix[y][x] = min(_matrix[y - 1][x], _matrix[y][x - 1]) + matrix[y][x]
                else:
                    _matrix[y][x] = min(_matrix[y + 1][x], _matrix[y - 1][x], _matrix[y][x - 1]) + matrix[y][x]
        min_path = min(_matrix[:, (x_len - 1)])
        if min_path == previous_min_path:
            min_path_stable_cnt += 1
        else:
            min_path_stable_cnt = 0
        if min_path_stable_cnt > min_path_stable_threshold:
            break
        previous_min_path = min_path

    return min(_matrix[:, (x_len - 1)])


if __name__ == "__main__":
    problem82()
