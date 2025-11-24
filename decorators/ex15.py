"""
This script contains a decorator factory which ensures that the return type
of the decorated function is of one of the specified in decorators arguments.

*types variable is held in decorators closure and is then used in the wrapper
to check against.

A cool thing - isinstance works not only on a signle type, but also on an
iterable of types.
"""

from functools import wraps

def ensure_type(*types: type):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, types):
                type_names = " OR ".join(x.__name__ for x in types)
                raise TypeError(f"Return type mismatch. Expected {type_names} and got {type(result).__name__}")
            return result
        return wrapper
    return dec

@ensure_type(float, int)
def pi():
    return 3.14

@ensure_type(float, int)
def hello():
    return "hello"

if __name__ == "__main__":
    pi()
    hello()
