from project_euler.geometry.pythagorean import pythagorean_triples

from project_euler.utils.timeit import timeit


@timeit
def problem75():
    """
    Singular integer right triangles
    Problem 75

    It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle
    triangle in exactly one way, but there are many more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

    In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and
    other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly
    three different integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

    Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right
    angle triangle be formed?
    """
    max_len = int(1.5e6)
    pythagorean_triples_gen = pythagorean_triples(max_len, "perimeter")
    L_cnt = [0] * (max_len + 1)  # Table of repetition for each length
    for triple in pythagorean_triples_gen:
        L_cnt[sum(triple)] += 1
    L_cnt_singular = filter(lambda len_: len_ == 1, L_cnt)
    return sum(L_cnt_singular)


if __name__ == "__main__":
    problem75()
