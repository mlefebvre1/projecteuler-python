from project_euler.utils.timeit import timeit

from project_euler.geometry.geometry import infinite_triangle_generator


@timeit
def problem85() -> int:
    """
    Counting rectangles
    Problem 85

    By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

    https://projecteuler.net/problem=85

    Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the
    grid with the nearest solution.

    For 1D rectangle the number of rectangles is given by the triangle serie
    """
    k = 100  # tryed many value, but it turns out it settles around k == 100
    best_rect = {"err": 2e6, "shape": (0, 0)}

    gen = infinite_triangle_generator()
    triangles = [next(gen) for _ in range(k)]

    for m in range(2, k):
        for n in range(m, k):
            rect2d = (
                triangles[m] * triangles[n]
            )  # For 2D rect it is simply the multiplication of both value in 1D rect.
            err = abs(int(2e6) - rect2d)
            if err < best_rect["err"]:  # keep the solution only if it's the best so far
                best_rect["err"] = err
                best_rect["shape"] = (m, n)

    m, n = best_rect["shape"]
    area = m * n
    print(area)
    return area


if __name__ == "__main__":
    problem85()
