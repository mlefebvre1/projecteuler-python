from project_euler.utils.timeit import timeit
from numpy import array, genfromtxt
from pathlib import Path
from project_euler.graph.dgraph import DGraph, dijkstra_shortest_path


@timeit
def problem83() -> int:
    """
    Path sum: four ways
    Problem 83

    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
    by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

    Find the minimal path sum from the top left to the bottom right by moving left, right, up,
    and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing
    an 80 by 80 matrix.

    Couldn't come up with a better algorithm than dijkstra for solving this one.. It's slow, but it's under 1 minute..
    """
    matrix = array(
        genfromtxt(
            Path(__file__).parent / "data/problem83.txt",
            delimiter=",",
            skip_header=False,
            dtype=int,
        )
    )
    graph = DGraph.make_from_matrix_up_down_right_left(matrix)
    dist = dijkstra_shortest_path(graph, src=0, dst=len(graph) - 1)
    return dist + matrix[0][0]


if __name__ == "__main__":
    problem83()
