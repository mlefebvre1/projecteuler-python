from project_euler.utils.timeit import timeit


def generate_dices():
    for f1 in range(0, 10):
        for f2 in range(f1 + 1, 10):
            for f3 in range(f2 + 1, 10):
                for f4 in range(f3 + 1, 10):
                    for f5 in range(f4 + 1, 10):
                        for f6 in range(f5 + 1, 10):
                            yield f"{f1}{f2}{f3}{f4}{f5}{f6}"


def two_dices_pairs(dice1, dice2):
    for f1 in dice1:
        for f2 in dice2:
            yield "".join(f1 + f2)
    for f2 in dice1:
        for f1 in dice2:
            yield "".join(f1 + f2)


def squares_validation(dice1, dice2):
    squares = {
        "presence": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        "val": [
            ["01"],
            ["04"],
            ["09", "06"],
            ["16", "19"],
            ["25"],
            ["36", "39"],
            ["49", "46"],
            ["64", "94"],
            ["81"],
        ],
    }
    pairs = list(two_dices_pairs(dice1, dice2))
    for i, square in enumerate(squares["val"]):
        for pos in square:
            if pos in pairs:
                squares["presence"][i] = 1
    for presence in squares["presence"]:
        if presence == 0:
            return False
    else:
        return True


@timeit
def problem90():
    """
    Cube digit pairs
    Problem 90
    Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By
    placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
    For example, the square number 64 could be formed:
    In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below
    one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
    For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the
    other cube.
    However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
    {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be
    impossible to obtain 09.
    In determining a distinct arrangement we are interested in the digits on each cube, not the order.
    {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
    {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
    But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the
    extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
    How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
    """
    arrangements = []
    dice_candidates = list(generate_dices())
    for dice1 in dice_candidates:
        for dice2 in dice_candidates:
            if squares_validation(dice1, dice2):
                if (dice1, dice2) not in arrangements and (
                    dice2,
                    dice1,
                ) not in arrangements:
                    arrangements.append((dice1, dice2))
    return len(arrangements)


if __name__ == "__main__":
    problem90()
