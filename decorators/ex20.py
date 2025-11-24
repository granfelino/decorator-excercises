"""
This script contains a decorator which applies decorators in a preserved order.
"""

from typing import Callable, TypeVar
from functools import wraps

F = TypeVar("F", bound=Callable)
DecoratorType = Callable[[F], F]

def signal(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing function `{func.__name__}`...")
        return func(*args, **kwargs)
    return wrapper

def run_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

def enforce_return(_type: type):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, _type):
                raise TypeError(f"Enforced type: {_type.__name__}, gotten: {type(result).__name__}")
        return wrapper
    return dec

def compose(*decs: DecoratorType):
    def dec(func):
        final = func
        for d in reversed(decs):
            final = d(final)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return final(*args, **kwargs)
        return wrapper
    return dec

@compose(enforce_return(str), run_twice, signal)
def hello():
    print("Inside the function")
    return "hello"

def main():
    hello()


if __name__ == "__main__":
    main()
