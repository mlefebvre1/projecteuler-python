from ..utils.timeit import timeit


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
    max_n = 100
    sum_of_square, square_of_sum = 0, 0
    for n in range(max_n + 1):
        sum_of_square += n * n
        square_of_sum += n
    square_of_sum = square_of_sum ** 2
    return square_of_sum - sum_of_square


if __name__ == "__main__":
    problem06()
