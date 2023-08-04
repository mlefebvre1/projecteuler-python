import itertools
from math import log, ceil
from project_euler.utils.timeit import timeit


def next_bit(bit, base):
    _next = int(bit) + 1
    if _next >= base:
        _next = 0
    return str(_next)


def base_n_expr(max_n, base):
    nb_dim = ceil(log(max_n, base))
    digits = ["0"] * nb_dim
    yield digits.copy()
    for n in range(1, max_n):
        for dim in range(nb_dim):
            if n % base**dim == 0:
                digits[(nb_dim - 1) - dim] = next_bit(digits[(nb_dim - 1) - dim], base)
            if base**dim > n:
                break
        yield digits.copy()


def math_expr(base_expr, operations, var_expr):
    for var in var_expr:
        for bexpr in base_expr:
            op_expr = []
            for op in bexpr:
                op_expr.append(operations[int(op)])
            expr = (var[0], op_expr[0], var[1], op_expr[1], var[2], op_expr[2], var[3])
            yield expr


def paranthesis_expr(op_expr):
    """
    Generating the following expressions : (+ can be any operations of +,-,*,/)
    a+b+c+d
    (a+b)+c+d
    (a+b)+(c+d)
    (a+b+c)+d
    a+(b+c+d)
    a+(b+c)+d
    a+((b,c)+d)
    a+(b+(c+d))
    (a+(b+c))+d
    ((a+b)+c)+d
    """
    for expr in op_expr:
        a, op1, b, op2, c, op3, d = expr
        yield a + op1 + b + op2 + c + op3 + d
        yield "(" + a + op1 + b + ")" + op2 + c + op3 + d
        yield "(" + a + op1 + b + ")" + op2 + "(" + c + op3 + d + ")"
        yield "(" + a + op1 + b + op2 + c + ")" + op3 + d
        yield a + op1 + "(" + b + op2 + c + op3 + d + ")"
        yield a + op1 + "(" + b + op2 + c + ")" + op3 + d
        yield "(" + a + op1 + "(" + b + op2 + c + ")" + ")" + op3 + d
        yield a + op1 + "(" + "(" + b + op2 + c + ")" + op3 + d + ")"
        yield "(" + "(" + a + op1 + b + ")" + op2 + c + ")" + op3 + d
        yield a + op1 + "(" + b + op2 + "(" + c + op3 + d + ")" + ")"


def get_expr(a, b, c, d, base_expr, operations):
    var = [a, b, c, d]
    var_expr = list(itertools.permutations(var, len(var)))
    op_expr = list(math_expr(base_expr, operations, var_expr))
    return paranthesis_expr(op_expr)


def get_results(expressions, max_score):
    results = [0] * (max_score + 1)
    for expr in expressions:
        try:
            result = eval(expr)
            error = int(result) - result
            if 0 <= result <= max_score and error == 0:
                results[int(result) - 1] = 1
        except ZeroDivisionError:
            pass
    return results


def get_score(result_tab):
    for i, result in enumerate(result_tab):
        if result == 0:
            return i
    else:
        return len(result_tab)


@timeit
def problem93() -> int:
    """
    Arithmetic expressions
    Problem 93

    By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic
    operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

    For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) − 1
    36 = 3 * 4 * (2 + 1)

    Note that concatenations of the digits, like 12 + 34, are not allowed.

    Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the
    maximum , and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

    Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers,
    1 to n, can be obtained, giving your answer as a string: abcd.
    """
    max_score = 10000
    max_digit = 9
    operations = ["+", "-", "*", "/"]
    base_expr = list(base_n_expr(64, 4))
    best = {"score": 0, "var": "xxxx"}
    a, b = 1, 2
    for c in range(b + 1, max_digit + 1):
        for d in range(c + 1, max_digit + 1):
            expressions = get_expr(str(a), str(b), str(c), str(d), base_expr, operations)
            results = get_results(expressions, max_score)
            score = get_score(results)
            if score > best["score"]:
                best = {"score": score, "var": f"{a}{b}{c}{d}"}
    return int(best["var"])


if __name__ == "__main__":
    problem93()
