from project_euler.utils.timeit import timeit


@timeit
def problem57():
    """
    Square root convergents
    Problem 57

    It is possible to show that the square root of two can be expressed as an infinite continued fraction.

    In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

    sqrt2 can be represented by the infinite fraction :
        sqrt(2) = h(n)/k(n)
        h(n) = a(n) * h(n-1) + h(n-2)
        k(n) = a(n) * k(n-1) + k(n-2)
        a(n) = 2
    """
    max_n = 1000
    a, h, k = 2, [3, 7], [2, 5]
    total = 0
    for n in range(2, max_n):
        hn = a * h[n - 1] + h[n - 2]
        kn = a * k[n - 1] + k[n - 2]
        h.append(hn), k.append(kn)
        if len(str(hn)) > len(str(kn)):
            total += 1
    return total


if __name__ == "__main__":
    problem57()
