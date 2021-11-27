from __future__ import annotations
import numpy as np
import numpy.typing as npt


class DGraph:
    def __init__(self, nb_vertices=0) -> None:
        self.vertices = np.array([None] * nb_vertices)

    def __len__(self) -> int:
        return self.vertices.shape[0]

    def add_edge(self, vertex_id: int, edges):
        """
        Edges connecting vertex 0 to vertex 1 with weight 673 and vertex 0 to vertex 5 with weight 201
        0 ---> 1 (weight=673)
        0 ---> 5 (weight=201)
        Arguments should be as follow
        vertex_id=0, edges={1: 673, 5: 201}
        """
        if vertex_id >= self.vertices.shape[0]:
            raise IndexError(
                f"Vertex is not present in the graph. "
                f"Given index is {vertex_id}, max index is {self.vertices.shape[0]}"
            )
        self.vertices[vertex_id] = edges

    @classmethod
    def make_from_matrix_down_right_only(cls, matrix: npt.NDArray) -> DGraph:
        """Create a graph from a matrix of edges. Only down and right connections are allowed"""
        graph = DGraph(
            nb_vertices=(matrix.size)
        )  # exclude last vertex because it has no connections anyway..
        x_len, y_len = matrix.shape
        for vertex_id in range(len(graph.vertices) - 1):
            # for vertex_id, _ in enumerate(graph.vertices):
            x, y = vertex_id % x_len, vertex_id // x_len
            if y == (y_len - 1) and x == (x_len - 1):
                continue
            elif y == (y_len - 1):  # last line only has right connections
                n1 = vertex_id + 1
                v1 = matrix[y][x + 1]
                graph.add_edge(vertex_id, {n1: v1})
            elif x == (x_len - 1):  # last column only has down connections
                n2 = vertex_id + x_len
                v2 = matrix[y + 1][x]
                graph.add_edge(vertex_id, {n2: v2})
            else:
                n1, n2 = vertex_id + 1, vertex_id + x_len
                v1, v2 = matrix[y][x + 1], matrix[y + 1][x]
                graph.add_edge(vertex_id, {n1: v1, n2: v2})

        return graph


def dijkstra_shortest_path(graph: DGraph, source: int) -> int:
    def min_dist(dist, visited):
        min_dist, min_vertex_id = float("inf"), None
        for _vertex_id, vertex_dist in enumerate(dist):
            if (vertex_dist < min_dist) and not visited[_vertex_id]:
                min_dist = vertex_dist
                min_vertex_id = _vertex_id
        return min_vertex_id

    dist = [float("inf")] * len(graph)
    prev = [None] * len(graph)
    visited = [False] * len(graph)

    dist[source] = 0

    while True:
        cur_vertex_id = min_dist(dist, visited)
        if (
            graph.vertices[cur_vertex_id] is None
        ):  # len(graph.vertices[cur_vertex_id]) == 0:
            break
        visited[cur_vertex_id] = True
        for next_vertex_id, weight in graph.vertices[cur_vertex_id].items():
            new_dist = dist[cur_vertex_id] + weight
            if new_dist < dist[next_vertex_id]:
                dist[next_vertex_id] = new_dist
                prev[next_vertex_id] = cur_vertex_id

    return dist, prev
