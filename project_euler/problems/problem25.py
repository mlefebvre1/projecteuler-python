from ..number_theory.series import fibonacci_generator

from ..utils.timeit import timeit


@timeit
def problem25():
    """
    The Fibonacci sequence is defined by the recurrence relation:

        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
    """
    term = 0
    generator = fibonacci_generator()
    while True:
        f = next(generator)
        if len(str(f)) >= 1000:
            break
        term += 1
    return term


if __name__ == "__main__":
    problem25()
