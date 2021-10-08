from project_euler.geometry.pythagorean import pythagorean_triples

from project_euler.utils.timeit import timeit


@timeit
def problem39():
    """
    Integer right triangles
    Problem 39
    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
    solutions for p = 120.

    For which value of p ≤ 1000, is the number of solutions maximised?
    """
    max_p = 1000
    perimeters = [0] * (max_p + 1)
    triples = pythagorean_triples(max_p)
    for triple in triples:
        p = sum(triple)
        if p <= max_p:
            perimeters[p] += 1
    return perimeters.index(max(perimeters))


problem39()
