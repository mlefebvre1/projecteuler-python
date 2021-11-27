from project_euler.utils.timeit import timeit
import pandas as pd
import numpy as np
from pathlib import Path
from project_euler.graph.dgraph import DGraph, dijkstra_shortest_path


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
    """
    matrix = np.array(
        pd.read_csv(Path(__file__).parent / "data/problem81.txt", header=None)
    )
    graph = DGraph.make_from_matrix_down_right_only(matrix)
    dist, _ = dijkstra_shortest_path(graph, 0)
    return dist[len(graph) - 1] + matrix[0][0]


if __name__ == "__main__":
    problem81()
