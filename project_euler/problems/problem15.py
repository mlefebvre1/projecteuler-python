from project_euler.utils.timeit import timeit
import numpy as np


@timeit
def problem15():
    """
    Lattice paths
    Problem 15

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly
    6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?

    The solution is to re-use previously calculated solution : [col, row] = [col-1, row] + [col, row-1]

    Easy to visualize with the following grid..

         1   2   3   4
      ---------------------
    1 |  2   3   4   5   ...
    2 |  3   6   10  15  ...
    3 |  4   10  20  35  ...
    4 |  5   15  35  70  ...
    """
    a = np.zeros((21, 21), dtype=np.int64)
    # Initialize the first row and column
    for col in range(1, 20 + 1):
        a[1][col] = col + 1
    for row in range(1, 20 + 1):
        a[row][1] = row + 1
    for row in range(2, 20 + 1):
        for col in range(2, 20 + 1):
            a[row][col] = a[row - 1][col] + a[row][col - 1]
    return a[20][20]


if __name__ == "__main__":
    problem15()
