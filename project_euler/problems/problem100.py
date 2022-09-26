from math import sqrt, floor

from project_euler.utils.timeit import timeit


def chance_is_50_50(x: int, y: int) -> bool:
    """
    (nb_blue/nb_total) * (nb_blue-1)/(nb_total-1) = 0.5
    2 * nb_blue * (nb_blue -1) = nb_total * (nb_total-1)
    let x be nb_blue and y be nb_total
    """
    return 2 * x * (x - 1) == y * (y - 1)


@timeit
def problem100():
    """
    Arranged probability
    Problem 100
    If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were
    taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
    The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
    containing eighty-five blue discs and thirty-five red discs.
    By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine the number
    of blue discs that the box would contain.

    The ratio blue disc on total disc ( x/y ) seems to converge to 1/sqrt(2) as y gets bigger. So x will always be
    y/sqrt(2) + 1 for working y value. The other observation is that the next total discs seems to converge to a ratio
    y(n)/y(n-1) ~5.82.. Every new solution found, simply multiply the total by y(n)/y(n-1) to converge faster.
    """
    nb_disk_total = 120  # 85 + 35
    ratio = 120 / 21  # initial ratio
    nb_disk_total_previous = nb_disk_total
    nb_disk_total = int(nb_disk_total * ratio)
    while 1:
        nb_blue_disk = floor(nb_disk_total / sqrt(2) + 1)
        if chance_is_50_50(nb_blue_disk, nb_disk_total):
            if nb_disk_total > 10**12:
                break
            ratio = nb_disk_total / nb_disk_total_previous  # Re-adjust the multiplier
            nb_disk_total_previous = nb_disk_total
            nb_disk_total = int(nb_disk_total * ratio)
        nb_disk_total += 1
    return nb_blue_disk


if __name__ == "__main__":
    problem100()
