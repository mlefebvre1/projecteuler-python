from project_euler.number_theory.primes import is_prime

from project_euler.utils.timeit import timeit


@timeit
def problem69():
    """
    Totient maximum
    Problem 69
    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less
    than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
    prime to nine, φ(9)=6.

    n	Relatively Prime	φ(n)	n/φ(n)
    2	1	                1	2
    3	1,2	                2	1.5
    4	1,3	                2	2
    5	1,2,3,4	            4	1.25
    6	1,5	2	            3
    7	1,2,3,4,5,6	        6	1.1666...
    8	1,3,5,7	4	        2
    9	1,2,4,5,7,8	        6	1.5
    10	1,3,7,9	            4	2.5
    It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

    Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

    The solution is simply the smallest number n ≤ 1,000,000 which has the most divisors. That is, multiply the prime
    numbers until the next prime, make the product exceeds 1,000,000:

        2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510
    """
    n = 1
    max_totient = 1
    while True:
        if is_prime(n):
            max_totient *= n
        if max_totient > int(1e6):
            return int(max_totient / n)
        n += 1


if __name__ == "__main__":
    problem69()
