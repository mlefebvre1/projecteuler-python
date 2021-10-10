from typing import List
from pathlib import Path
from project_euler.utils.timeit import timeit


def prepare_data() -> List[List[int]]:
    with open(f"{Path(__file__).parent}/data/problem67.txt", "r") as file:
        data = file.readlines()
    grid = []
    for line in data:
        _line = line.split("\n")[0].split(" ")
        line_n = []
        for n in _line:
            line_n.append(int(n))
        grid.append(line_n)  # prepare data
    return grid


@timeit
def problem67():
    """
    Maximum path sum II
    Problem 67

    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
     top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text
    file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
    problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over
    twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
    """
    grid = prepare_data()
    for y in range(1, len(grid)):
        for x in range(0, len(grid[y])):
            # the first and last element of a line can only take 1 value
            if x == 0:  # first element of the line
                grid[y][x] += grid[y - 1][x]
            elif x == len(grid[y]) - 1:  # last element of the line
                grid[y][x] += grid[y - 1][x - 1]
            else:  # any other element
                grid[y][x] += max(grid[y - 1][x - 1], grid[y - 1][x])
    max_path = max(grid[len(grid) - 1])
    return max_path


if __name__ == "__main__":
    problem67()
