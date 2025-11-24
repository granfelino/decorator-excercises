"""
This script contains a decorator that prints the positional and keyword
arguments of the decorated function. This decorator preserves metadata using
functools.wraps
"""

from functools import wraps

def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Positional arguments of {func.__name__}:")
        for a in args:
            print(a)

        if len(kwargs) > 0:
            print(f"Keyword arguments of {func.__name__}:")
            for name, val in kwargs.items():
                print(f"Name: {name}\t Value: {val}")

        return func(*args, **kwargs)
    return wrapper

@print_args
def hello(name, last_name=""):
    print(f"Hello {name} {last_name}!")

if __name__ == "__main__":
    hello("Mike", last_name="Johnson")
    hello("Mike")
