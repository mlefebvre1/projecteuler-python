from project_euler.utils.timeit import timeit


def month_nb_days(month_index: int, year: int) -> int:
    # jan(31), feb(28), mars(31), april(30), may(31), june(30), july(31), august(31), september(30), october(31),
    # november(30), december(31)
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 400:
        leap = True
    else:
        leap = False
    if leap and month_index == 1:  # leap years only affect february
        return month[month_index] + 1
    else:
        return month[month_index]


@timeit
def problem19():
    """
    Counting Sundays
    Problem 19

    You are given the following information, but you may prefer to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """

    day = 0
    nb_sundays = 0
    for year in range(1901, 2000):  # for each year of the twentieth century
        for month in range(0, 12):  # for each month in the year
            nb_days = month_nb_days(
                month, year
            )  # this gives the number of days in for the current month
            while day < nb_days:
                day += 7
            day -= nb_days  # this gives the first day of the next month
            if day == 6:
                nb_sundays += 1
    return nb_sundays


problem19()
