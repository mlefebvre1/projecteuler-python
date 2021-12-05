from project_euler.utils.timeit import timeit


@timeit
def problem91():
    """
    Right triangles with integer coordinates
    Problem 91
    The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0),
    to form ΔOPQ.
    There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between
    0 and 2 inclusive; that is,
    0 ≤ x1, y1, x2, y2 ≤ 2.
    Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

    Solution : For every set of coordinate possible P[x1,y1] and Q[x2,y2], determine the distance power of 2 from the
    origin O(0,0). of P and Q, namely OP and OQ. Then find the distance power of 2 between P and Q (PQ). Finally,
    determine the hypotenuse which is max(OP, OQ, PQ) and check the equality --> hyp power of two == the sum of the two
    other distance power of 2 (a^2 = b^2 + c^2). If the equation is satisfied, this tells us that the triangle has a
    right angle.
    """
    k = 50
    nb_triangles = 0
    for y2 in range(0, k + 1):
        for y1 in range(0, k + 1):
            for x1 in range(0, k + 1):
                for x2 in range(0, k + 1):
                    OP2 = x1 ** 2 + y1 ** 2
                    OQ2 = x2 ** 2 + y2 ** 2
                    QP2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
                    if OP2 != 0 and OQ2 != 0 and QP2 != 0:
                        if OP2 > OQ2 and OP2 > QP2:  # OP is the hyp
                            if OP2 == (OQ2 + QP2):
                                nb_triangles += 1
                        elif OQ2 > OP2 and OQ2 > QP2:  # OQ is the hyp
                            if OQ2 == (OP2 + QP2):
                                nb_triangles += 1
                        else:  # QP is the hyp
                            if QP2 == (OP2 + OQ2):
                                nb_triangles += 1

    return nb_triangles // 2


if __name__ == "__main__":
    problem91()
