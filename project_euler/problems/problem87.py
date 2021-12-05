from project_euler.utils.timeit import timeit
from project_euler.number_theory.primes import sieves


@timeit
def problem87() -> int:
    """
    Prime power triples
    Problem 87
    The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact,
    there are exactly four numbers below fifty that can be expressed in such a way:
    28 = 2^2 + 2^3 + 2^4
    33 = 32 + 23 + 24
    49 = 52 + 23 + 24
    47 = 22 + 33 + 24
    How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth
    power?
    Solution : Create list 3 of primes for each power using the fact that for x^2 < 50e6 and x^3 < 50e6 and x^4 < 50e6
                Next simply use 3 nested loops to calculate each sum. For each sum below 50e6 make sure the sum was not
                written already.
    """

    k = int(50e6)
    mem = [0] * (k + 1)
    primes_pow2 = list(sieves(int(pow(k, 1 / 2))))
    primes_pow3 = list(sieves(int(pow(k, 1 / 3))))
    primes_pow4 = list(sieves(int(pow(k, 1 / 4))))
    nb = 0
    for prime2 in primes_pow2:
        for prime3 in primes_pow3:
            for prime4 in primes_pow4:
                sum_ = prime2 ** 2 + prime3 ** 3 + prime4 ** 4
                if (
                    sum_ <= k and mem[sum_] == 0
                ):  # make sure the sum was not written yet
                    mem[sum_] = 1
                    nb += 1
    return nb


if __name__ == "__main__":
    problem87()
