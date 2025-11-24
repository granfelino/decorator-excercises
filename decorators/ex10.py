"""
This script contains a decorator that measures the execution time of the
decorated function using time.per_counter. Preserves metadata.
"""

from functools import wraps
import time

def duration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        delta = time.perf_counter() - start
        print(f"[duration] Executing {func.__name__} took {delta:.6f} seconds.")
        return result
    return wrapper

@duration
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
