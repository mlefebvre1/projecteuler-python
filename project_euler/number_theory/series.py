def fibonacci_generator():
    fn_minus1, fn = 0, 1
    while True:
        yield fn_minus1
        fn_minus1, fn = fn, fn + fn_minus1


def fibonacci_generator_recursive(f1, f2):
    f = f1 + f2
    yield f
    yield from fibonacci_generator_recursive(f2, f)
