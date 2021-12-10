from project_euler.utils.timeit import timeit


@timeit
def problem97() -> int:
    """
    Large non-Mersenne prime
    Problem 97
    The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
    26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been
    found which contain more digits.
    However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.
    Find the last ten digits of this prime number.

    I guess in python this is way too easy...
    """
    mod = int(1e10)  # since we only keep the last 10 digits
    return (28433 * pow(2, 7830457, mod) + 1) % mod


if __name__ == "__main__":
    problem97()
