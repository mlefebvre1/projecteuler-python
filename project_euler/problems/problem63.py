from project_euler.utils.timeit import timeit


def generate_digit_power_match(power):
    for digit in range(1, 10):
        n = pow(digit, power)
        if len(str(n)) == power:
            yield 1


@timeit
def problem63():
    """
    Powerful digit counts
    Problem 63

    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth
     power.

    How many n-digit positive integers exist which are also an nth power?
    """
    total = 0
    power = 1
    while len(str(9**power)) == power:
        total += sum(generate_digit_power_match(power))
        power += 1

    return total


if __name__ == "__main__":
    problem63()
