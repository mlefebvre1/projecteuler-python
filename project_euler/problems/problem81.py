from project_euler.utils.timeit import timeit
from numpy import array, genfromtxt
from pathlib import Path


@timeit
def problem81() -> int:
    """
    Path sum: two ways
    Problem 81
    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
    by only moving to the right and down, is indicated in bold red and is equal to 2427.

    https://projecteuler.net/problem=81

    Find the minimal path sum from the top left to the bottom right by only moving right and down
    in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

    The original solution was using dijkstra shortest path algorithm. But it turns out it was much slower than
    the matrix dynamic programming solution.

    Code using dijsktra_shortest_path :

    matrix = array(
        genfromtxt(
            Path(__file__).parent / "data/problem81.txt",
            delimiter=",",
            skip_header=False,
            dtype=int,
        )
    )
    graph = DGraph.make_from_matrix_down_right_only(matrix)
    dist = dijkstra_shortest_path(graph, source=0, dst=len(graph) - 1)
    return dist + matrix[0][0]
    """
    matrix = array(
        genfromtxt(
            Path(__file__).parent / "data/problem81.txt",
            delimiter=",",
            skip_header=False,
            dtype=int,
        )
    )
    x_len, y_len = matrix.shape
    for y in range(y_len):
        for x in range(x_len):
            if x == 0 and y == 0:
                continue
            elif y == 0:
                matrix[y][x] += matrix[y][x - 1]
            elif x == 0:
                matrix[y][x] += matrix[y - 1][x]
            else:
                matrix[y][x] += min(matrix[y][x - 1], matrix[y - 1][x])
    return matrix[y_len - 1][x_len - 1]


if __name__ == "__main__":
    problem81()
