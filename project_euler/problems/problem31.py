from ..utils.timeit import timeit


@timeit
def problem31():
    """

    Coin sums
    Problem 31

    In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
    circulation :

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?
        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  ...
    1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   ...
    2   1   2   2   3   3   4   4   5   5   6   6   7   7   8   8   9   9   10  10  11  11  ...
    5   1   2   2   3   4   5   6   7   8   10  11  13  14  16  18  20  22  24  26  29  31  ...
    10  1   2   2   3   4   5   6   7   8   11  12  15  16  19  22  25  28  31  34  40  43  ...
    """

    amount_max = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    nb_ways = [0] * (amount_max + 1)
    nb_ways[0] = 1
    for coin in coins:
        for amount in range(coin, amount_max + 1):
            nb_ways[amount] += nb_ways[amount - coin]
    return nb_ways[amount_max]


if __name__ == "__main__":
    problem31()
