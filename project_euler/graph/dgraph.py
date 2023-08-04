from __future__ import annotations
import numpy as np
import numpy.typing as npt
from contextlib import suppress


class DGraph:
    def __init__(self, nb_vertices=0) -> None:
        self.vertices = np.array([None] * nb_vertices)

    def __len__(self) -> int:
        return self.vertices.shape[0]

    def __str__(self) -> str:
        ret = ""
        for id, v in enumerate(self.vertices):
            ret += f"Vertex {id} --> connected vertices : {v}\n"
        return ret

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
        graph = DGraph(nb_vertices=(matrix.size))  # exclude last vertex because it has no connections anyway..
        x_len, y_len = matrix.shape
        for vertex_id in range(len(graph.vertices) - 1):
            x, y = vertex_id % x_len, vertex_id // x_len

            v_right, v_down = (
                vertex_id + 1,
                vertex_id + x_len,
            )
            with suppress(IndexError):
                w_right = matrix[y][x + 1]
            with suppress(IndexError):
                w_down = matrix[y + 1][x]

            if y == (y_len - 1) and x == (x_len - 1):
                continue
            elif y == (y_len - 1):  # last line only has right connections
                graph.add_edge(vertex_id, {v_right: w_right})
            elif x == (x_len - 1):  # last column only has down connections
                graph.add_edge(vertex_id, {v_down: w_down})
            else:
                graph.add_edge(vertex_id, {v_right: w_right, v_down: w_down})

        return graph

    @classmethod
    def make_from_matrix_up_down_right_only(cls, matrix: npt.NDArray) -> DGraph:
        """Create a graph from a matrix of edges. Only up, down and right connections are allowed"""
        graph = DGraph(nb_vertices=(matrix.size))  # exclude last vertex because it has no connections anyway..
        x_len, y_len = matrix.shape
        for vertex_id in range(len(graph.vertices) - 1):
            x, y = vertex_id % x_len, vertex_id // x_len

            v_right, v_down, v_up = (
                vertex_id + 1,
                vertex_id + x_len,
                vertex_id - x_len,
            )
            with suppress(IndexError):
                w_right = matrix[y][x + 1]
            with suppress(IndexError):
                w_down = matrix[y + 1][x]
            with suppress(IndexError):
                w_up = matrix[y - 1][x]

            if y == (y_len - 1) and x == (x_len - 1):
                continue
            elif y == (y_len - 1):  # last line
                graph.add_edge(vertex_id, {v_right: w_right, v_up: w_up})
            elif x == (x_len - 1):  # last column.. can't go right
                if y == 0:  # first line.. can't go up
                    graph.add_edge(vertex_id, {v_down: w_down})
                else:
                    graph.add_edge(vertex_id, {v_down: w_down, v_up: w_up})
            else:
                graph.add_edge(vertex_id, {v_right: w_right, v_down: w_down, v_up: w_up})

        return graph

    @classmethod
    def make_from_matrix_up_down_right_left(cls, matrix: npt.NDArray) -> DGraph:
        """Create a graph from a matrix of edges. Only up, down and right connections are allowed"""
        graph = DGraph(nb_vertices=(matrix.size))  # exclude last vertex because it has no connections anyway..
        x_len, y_len = matrix.shape
        for vertex_id in range(len(graph.vertices) - 1):
            x, y = vertex_id % x_len, vertex_id // x_len

            v_right = vertex_id + 1
            v_left = vertex_id - 1
            v_down = vertex_id + x_len
            v_up = vertex_id - x_len

            with suppress(IndexError):
                w_right = matrix[y][x + 1]
            with suppress(IndexError):
                w_left = matrix[y][x - 1]
            with suppress(IndexError):
                w_down = matrix[y + 1][x]
            with suppress(IndexError):
                w_up = matrix[y - 1][x]

            if y == 0:
                if x == 0:
                    graph.add_edge(vertex_id, {v_right: w_right, v_down: w_down})
                elif x == x_len - 1:
                    graph.add_edge(vertex_id, {v_left: w_left, v_down: w_down})
                else:
                    graph.add_edge(vertex_id, {v_right: w_right, v_left: w_left, v_down: w_down})
            elif y == (y_len - 1):  # last line
                if x == 0:
                    graph.add_edge(vertex_id, {v_right: w_right, v_up: w_up})
                elif x == x_len - 1:
                    continue
                else:
                    graph.add_edge(vertex_id, {v_right: w_right, v_left: w_left, v_up: w_up})
            elif x == 0:
                graph.add_edge(vertex_id, {v_right: w_right, v_down: w_down, v_up: w_up})
            elif x == (x_len - 1):  # last column.. can't go right
                graph.add_edge(vertex_id, {v_left: w_left, v_down: w_down, v_up: w_up})
            else:
                graph.add_edge(
                    vertex_id,
                    {v_right: w_right, v_left: w_left, v_down: w_down, v_up: w_up},
                )

        return graph


def dijkstra_shortest_path(graph: DGraph, src: int, dst: int) -> int:
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

    dist[src] = 0

    while True:
        cur_vertex_id = min_dist(dist, visited)
        if graph.vertices[cur_vertex_id] is None:
            break
        visited[cur_vertex_id] = True
        for next_vertex_id, weight in graph.vertices[cur_vertex_id].items():
            new_dist = dist[cur_vertex_id] + weight
            if new_dist < dist[next_vertex_id]:
                dist[next_vertex_id] = new_dist
                prev[next_vertex_id] = cur_vertex_id

    return dist[dst]
