from pathlib import Path
import numpy as np
from numpy.typing import NDArray
from project_euler.utils.timeit import timeit


class Sudoku:
    def __init__(self, grid: NDArray) -> None:
        self.grid = grid

    def solve(self) -> NDArray:
        x_max, y_max = self.grid.shape

        def backtrack(x: int, y: int) -> bool:
            """returns True when it reaches the end of the grid, returns False if it needs to backtrack"""
            while True:
                if self.grid[y][x] == 0:
                    for n in range(1, x_max + 1):
                        if self._is_possible(n, x, y):
                            self.grid[y][x] = n
                            if x < x_max - 1:
                                next_x, next_y = x + 1, y
                            elif y < y_max - 1:
                                next_x, next_y = 0, y + 1
                            else:
                                return True
                            if backtrack(next_x, next_y):
                                return True
                            self.grid[y][x] = 0
                    return False
                if x < x_max - 1:
                    x += 1
                elif y < y_max - 1:
                    x, y = 0, y + 1
                else:
                    return True

        backtrack(0, 0)
        return self.grid

    def _is_possible(self, n, x, y) -> bool:
        """Check if it is possible to insert n at the location provided in the grid"""
        # Line Validation
        if n in self.grid[y]:
            return False

        # Column Validation
        if n in self.grid[:, x]:
            return False

        # Square Validation
        sqr_x, sqr_y = x // 3, y // 3
        if n in self.grid[sqr_y * 3 : sqr_y * 3 + 3, sqr_x * 3 : sqr_x * 3 + 3]:
            return False

        return True


def grid_generator():
    with open(Path(__file__).parent / "data/problem96.txt") as f:
        data = f.read().splitlines()
    grid = []
    for line in data:
        if line.startswith("Grid"):
            if len(grid) > 0:
                yield np.array(grid)
                grid = []
        else:
            grid.append(list(map(lambda x: int(x), list(line))))
    # last grid because we won't hit a line that starts with "Grid*"!
    yield np.array(grid)


@timeit
def problem96():
    """
    Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but
    credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called
    Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in
    such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical
    starting puzzle grid and its solution grid. See https://projecteuler.net/problem=96

    A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to
    employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The
    complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it
    can be solved by straight forward direct deduction.

    The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
    ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

    By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
    for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
    """
    # Generate the sudoku grids from a file
    grids = grid_generator()

    sum_ = 0
    for idx, grid in enumerate(grids):
        sudoku = Sudoku(grid)
        solved_grid = sudoku.solve()
        digits = f"{solved_grid[0][0]}{solved_grid[0][1]}{solved_grid[0][2]}"
        print(f"Grid {idx+1}")
        print(solved_grid, digits)
        print("\n")
        sum_ += int(digits)
    return sum_


if __name__ == "__main__":
    problem96()
