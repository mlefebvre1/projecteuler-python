from typing import List
from pathlib import Path
from project_euler.utils.timeit import timeit


def prepare_data() -> List[List[int]]:
    with open(f"{Path(__file__).parent}/data/problem18.txt", "r") as file:
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
def problem18():
    """
    Maximum path sum I
    Problem 18

    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
    from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

    NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However,
    Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
    and requires a clever method! ;o)
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


problem18()
