from project_euler.utils.timeit import timeit
from typing import List, Iterator, Tuple


@timeit
def problem95():
    """
    Amicable chains
    Problem 95

    The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors
    of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

    Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
    forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

    Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

    12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

    Since this chain returns to its starting point, it is called an amicable chain.

    Find the smallest member of the longest amicable chain with no element exceeding one million.

    Solution : First we find the sum proper divisor for each entry. Using this we can layout the chains without
               calculating twice or more the same sum proper divisor. By observation we only check even numbers
               because no amicable chain exists starting with odd numbers. The chain is not amicable if a number
               in the chain repeats but it's not the starting number. The chain is also considered invalid if any
               number of the chain is greater than 1e6.

    """

    """
    10
    -----
    2               -> 2
    2x2             -> 4
    2x2x2           -> 8
    2x3             -> 6
    2x5             -> 10
    3               -> 3
    3x3             -> 9
    5               -> 5
    7               -> 7

    """
    max_n = int(1e6)

    def get_proper_divisor_sums() -> List[int]:
        """
        Basically a modified sieves, but instead of marking true for visited,
        we add the value of the prime visiting
        """
        sums = [0] * (max_n + 1)
        for n in range(1, max_n + 1):
            for x in range(n + n, max_n + 1, n):
                sums[x] += n
        return sums

    div_sums = get_proper_divisor_sums()

    def make_chains() -> Iterator[Tuple[int, int]]:
        for n in range(max_n + 1):
            if n % 2 == 0:
                current = n
                chain = [n]
                while 1:
                    div_sum = div_sums[current]
                    if div_sum > max_n:  # Not amicable with all under 1M in the chain
                        yield n, 0
                        break
                    if div_sum in chain:
                        if div_sum == n:
                            yield n, len(chain)
                        else:
                            yield n, 0
                        break
                    chain.append(div_sum)
                    current = div_sum

    n, _ = max(make_chains(), key=lambda x: x[1])
    return n


if __name__ == "__main__":
    problem95()
