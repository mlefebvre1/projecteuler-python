from project_euler.utils.timeit import timeit


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
    mem = [[0 for _ in range(20 + 1)] for _ in range(20 + 1)]
    # Initialize the first row and column
    for col in range(1, 20 + 1):
        mem[1][col] = col + 1
    for row in range(1, 20 + 1):
        mem[row][1] = row + 1
    for row in range(2, 20 + 1):
        for col in range(2, 20 + 1):
            mem[row][col] = mem[row - 1][col] + mem[row][col - 1]
    return mem[20][20]


problem15()
