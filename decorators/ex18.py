"""
This function contains a decorator which applies a callback to the decorated
function. Nice use of TypeVar and ParamSpec to hint a Callable's parameters
and return type.
"""

from typing import Callable, Any, TypeVar, ParamSpec
from functools import wraps

P = ParamSpec("P")
R = TypeVar("R")
S = TypeVar("S")

def callback(cb: Callable[R, S]):
    def dec(func: Callable[P, R]) -> Callable[P, S]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> S:
            result = func(*args, **kwargs)
            return cb(result)
        return wrapper
    return dec

def toupper(string: str):
    return string.upper()

@callback(toupper)
def hello(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    print(hello("Mike"))
