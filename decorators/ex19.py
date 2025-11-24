"""
This script contains a decorator created using a class and its magic function
__call__. Works both with and without arguments
"""

from typing import Callable, Any
from functools import wraps

class RunTwice():
    def __init__(self, arg: Any):
        if callable(arg):
            self.func = arg
            self.arg = None
        else:
            self.func = None
            self.arg = arg

    def __call__(self, func: Any = None):
        if func is not None:
            self.func = func

        @wraps(self.func)
        def wrapper(*args, **kwargs):
            if self.arg is not None:
                print(f"Class-based decorator with argument: {self.arg}")
            result = None
            result = self.func(*args, **kwargs)
            result = self.func(*args, **kwargs)
            return result
        return wrapper

@RunTwice("argument")
def hello(name):
    print(f"Hello {name}!")

@RunTwice
def hi():
    print("Hi!")

if __name__ == "__main__":
    hello("Mike")
    hi()
