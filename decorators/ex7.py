"""
This script contains a decorator that ensures that all the parameters of the
decorated function are of a specific type. To be more precise this is a
decorator factory: it takes an argument and returns a decorator which is then
applied to the decorated function. This decorator preserves metadata using
functools.wraps
"""

from typing import Type, Any
from functools import wraps

def enforce_type(_type: Type[Any]):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for a in args:
                if not isinstance(a, _type):
                    raise TypeError(f"Invalid type. Positional argument '{a}' should be of type: {_type.__name__}")
            for name, val in kwargs.items():
                if not isinstance(val, _type):
                    raise TypeError(f"Invalid type. Keyword argument '{name}' should be of type: {_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return dec

@enforce_type(str)
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
    hello(123)
