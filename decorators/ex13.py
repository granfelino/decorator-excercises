"""
This script contains a decorator that can be both parametrized or not.
This means that if the decorator is called without the parameter then
the decorator receives the decorated function as an argument. Based on
detecting whether or not the passed argument is a callable a wrapper is
returned or a decorator creator is called. Preserves metadata in both cases.
"""

from collections.abc import Callable
from typing import Any
from functools import wraps

def call_multiple(func=None, *, count=5):
    if func is not None and callable(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper

    def dec(real_func):
        @wraps(real_func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = real_func(*args, **kwargs)
            return result
        return wrapper
    return dec

@call_multiple
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
