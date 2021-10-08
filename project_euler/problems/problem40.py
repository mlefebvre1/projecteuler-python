from ..utils.timeit import timeit


@timeit
def problem40():
    """
    Champernowne's constant
    Problem 40

    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """
    max_n = 1000000
    expr = ""
    targets = [1, 10, 100, 1000, 10000, 100000, 1000000]
    target_index = 0
    target = targets[target_index]
    prod = 1
    for n in range(1, max_n):
        n = str(n)
        expr += n
        d = len(expr)
        if d >= target:  # Found the next target!
            # Here simply make sure that when d is greater than target we read the right index which is d - (d-target)
            prod *= int(expr[d - (d - target) - 1])
            target_index += 1
            if target_index >= len(targets):
                break
            else:
                target = targets[target_index]
    return prod


if __name__ == "__main__":
    problem40()
