"""
This script contains a decorator that executes the decorated function only if
the decorated funciton's parameters are 'approved' by the condition function.

This function preserves metadata using functools.wraps
"""

from functools import wraps
from collections.abc import Callable

def conditional(cond: Callable[..., bool]):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if cond(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Condition not met.")
        return wrapper
    return dec



@conditional(lambda _: True)
def hello(name):
    print(f"Hello {name}!")

@conditional(lambda _: False)
def bye(name):
    print(f"Bye {name}")

if __name__ == "__main__":
    hello("Mike")
    bye("Mike")
