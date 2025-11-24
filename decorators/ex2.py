"""
Script with a decorator that prints the date and time of decorated function.

The decorator accepts a callable and returns a wrapper which replaces the
original function with the one printing the timestamp before running the 
decorated function - does not preserve metadata (missing functools.wraps).
"""

import datetime as dt

def exec_time(func):
    def wrapper(*args, **kwargs):
        print(f"Executing function {func.__name__} at: {dt.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

@exec_time
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
