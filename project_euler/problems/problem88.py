from project_euler.utils.timeit import timeit
from functools import reduce


def calc_k(arr):
    sum_arr = sum(arr)
    prod_arr = reduce(lambda tot, x: x * tot, arr, 1)
    k = (prod_arr - sum_arr) + len(arr)
    return k, prod_arr


def update_prod_sum_table(k, prod, prod_sum_table, max_k):
    if k <= max_k:
        if prod < prod_sum_table[k]:
            prod_sum_table[k] = prod


def comb_k(max_accepted, arr_len, table, max_k):
    indexes = [2 for _ in range(arr_len)]
    indexes_stop = [int(max_accepted ** (1 / (loop + 1))) for loop in range(arr_len)]
    k, prod = calc_k(indexes)
    update_prod_sum_table(k, prod, table, max_k)
    while 1:
        # inner loop
        inner_loop_stop_mult = 1
        for i in range(1, arr_len):
            inner_loop_stop_mult *= indexes[i]
        inner_loop_stop = int(max_accepted / inner_loop_stop_mult)
        for i in range(indexes[0], inner_loop_stop):
            indexes[0] += 1
            k, prod = calc_k(indexes)
            update_prod_sum_table(k, prod, table, max_k)
        # outer loops
        for i in range(1, arr_len):
            indexes[i] += 1
            k, prod = calc_k(indexes)
            update_prod_sum_table(k, prod, table, max_k)
            if indexes[i] < indexes_stop[i]:
                stop_index = i
                break
        else:
            return
        for i in range(stop_index):
            indexes[i] = indexes[stop_index]
        k, prod = calc_k(indexes)
        update_prod_sum_table(k, prod, table, max_k)


@timeit
def problem88():
    """
    Product-sum numbers
    Problem 88
    A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
    {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
    For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
    For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The
    minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
    k=2: 4 = 2 × 2 = 2 + 2
    k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
    k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
    k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
    k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
    Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once
    in the sum.
    In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
    What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
    """
    max_k = 12000
    max_accepted = 2 * max_k
    prod_sum_table = [float("inf")] * (max_k + 1)
    for loop in range(2, 15):
        comb_k(max_accepted, loop, prod_sum_table, max_k)

    mem = [0] * (max_accepted + 1)
    for k in range(2, len(prod_sum_table)):
        mem[prod_sum_table[k]] = 1

    prod_sum_total = 0
    for index, m in enumerate(mem):
        if m == 1:
            prod_sum_total += index
    return prod_sum_total


if __name__ == "__main__":
    problem88()
