"""
This script contains a decorator that can be applied to class methods.
Actually nothing changes here, because self is contained within *args.
"""

from functools import wraps

def run_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        for _ in range(2):
            result = func(*args, **kwargs)
        return result
    return wrapper

@run_twice
def hello(name):
    print(f"Hello {name}!")

class SomeClass():
    def __init__(self, sth: str):
        self.sth = sth

    @run_twice
    def print(self, thing: str):
        print(self.sth)
        print(thing)

if __name__ == "__main__":
    hello("Mike")
    some = SomeClass("first")
    some.print("second")
