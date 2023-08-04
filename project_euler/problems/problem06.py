from project_euler.utils.timeit import timeit


@timeit
def problem06():
    """
    Sum square difference
    Problem 6

    The sum of the squares of the first ten natural numbers is 385,

    The square of the sum of the first ten natural numbers is 3025,

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    2640

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
    sum.

    Solution : pretty straight forward...
    """
    return sum(range(0, 101)) ** 2 - sum(map(lambda n: n**2, range(0, 101)))


if __name__ == "__main__":
    problem06()
