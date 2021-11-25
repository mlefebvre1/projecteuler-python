import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"{func.__name__} : the solution is {result}. The execution took : {end - start} seconds"
        )
        return result

    return wrapper
