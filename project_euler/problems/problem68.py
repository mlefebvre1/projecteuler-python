from itertools import permutations
from typing import List, Iterator, Tuple

from ..utils.timeit import timeit


def is_all_arms_sum_equal(gon_ring: List[Tuple[int, int, int]]) -> bool:
    arm_sum_gen = (sum(arm) for arm in gon_ring)
    arm_sum_to_match = next(arm_sum_gen)
    for arm_sum in arm_sum_gen:
        if arm_sum != arm_sum_to_match:
            return False
    else:
        return True


def is_first_node_the_smallest_external_node(
    gon_ring: List[Tuple[int, int, int]]
) -> bool:
    external_nodes = [arm[0] for arm in gon_ring]
    return external_nodes.index(min(external_nodes)) == 0


def build_magic_gon_ring(nodes: Tuple[int]) -> List[Tuple[int, int, int]]:
    """Greedy approach, to maximise the gon ring result, 6 should be the smallest node of the outer graph"""
    return [
        (6, nodes[0], nodes[1]),
        (nodes[2], nodes[1], nodes[3]),
        (nodes[4], nodes[3], nodes[5]),
        (nodes[6], nodes[5], nodes[7]),
        (nodes[8], nodes[7], nodes[0]),
    ]


def build_string_repr_from_gon_ring(gon_ring: List[Tuple[int, int, int]]) -> str:
    result = ""
    for arm in gon_ring:
        for node in arm:
            result += str(node)
    return result


def filter_permutation_with_10_on_inner_graph(nodes):
    inner_graph_node_id = [1, 3, 5, 7, 0]
    for id_ in inner_graph_node_id:
        if nodes[id_] == 10:
            return False
    else:
        return True


def generate_solutions() -> Iterator[str]:
    """Produce 16 digit string solutions"""
    nodes = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    nodes_permutations = permutations(nodes)
    nodes_permutations_filtered = filter(
        filter_permutation_with_10_on_inner_graph, nodes_permutations
    )
    for nodes_permutation in nodes_permutations_filtered:
        gon_ring = build_magic_gon_ring(nodes_permutation)
        if is_all_arms_sum_equal(gon_ring) and is_first_node_the_smallest_external_node(
            gon_ring
        ):
            yield build_string_repr_from_gon_ring(gon_ring)


@timeit
def problem68():
    """
    Magic 5-gon ring

    Problem 68
    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

    Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this
    example), each solution can be described uniquely. For example, the above solution can be described by the set:
    4,3,2; 6,2,1; 5,1,3.

    See https://projecteuler.net/problem=68 for the diagram

    It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in
    total.

    Total	Solution Set
    9	4,2,3; 5,3,1; 6,1,2
    9	4,3,2; 6,2,1; 5,1,3
    10	2,3,5; 4,5,1; 6,1,3
    10	2,5,3; 6,3,1; 4,1,5
    11	1,4,6; 3,6,2; 5,2,4
    11	1,6,4; 5,4,2; 3,2,6
    12	1,5,6; 2,6,4; 3,4,5
    12	1,6,5; 3,5,4; 2,4,6
    By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is
    432621513.

    Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is
    the maximum 16-digit string for a "magic" 5-gon ring?
    """
    solutions = generate_solutions()
    solutions_as_int = (int(solution) for solution in solutions)
    return max(solutions_as_int)


if __name__ == "__main__":
    problem68()
