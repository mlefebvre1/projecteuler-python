from project_euler.arithmetic.arithmetic import pandigital_validation

from project_euler.utils.timeit import timeit


@timeit
def problem32():
    """
    Pandigital products
    Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for
    example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
    through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
    pandigital.

    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """
    prod_list = []
    for m1 in range(1, 100):
        for m2 in range(1, 10000):
            prod = m1 * m2
            n = str(m1) + str(m2) + str(prod)
            if pandigital_validation(n, 1, 9):
                if prod not in prod_list:
                    prod_list.append(prod)
    return sum(prod_list)


if __name__ == "__main__":
    problem32()
