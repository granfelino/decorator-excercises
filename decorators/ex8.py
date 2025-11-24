"""
This script contains a decorator that retries running the function specified
number of types and catches the specified exception type. If all retries
fail the last exception is raised. This technically is a decorator factory.
It preserves metadata of the decorated function using the functools.wraps
"""

from functools import wraps
from typing import Type

def retry(count: int = 5, ex: Type[Exception] = Exception):
    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_ex = None
            for i in range(count):
                try:
                    result = func(*args, **kwargs)
                except ex as e:
                    last_ex = e
                    print(f"Attepmt {i+1} failed, retrying...")
                    continue
                else:
                    print(f"Succeeded on attempt {i+1}.")
                    return result

            raise last_ex
        return wrapper
    return dec

@retry()
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
