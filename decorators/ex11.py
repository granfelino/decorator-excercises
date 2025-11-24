"""
This script contains a decorator that caches the result of the decorated
function for each specified set of parameters. The parameters are saved using
the closure attribute of the function object. Preserved metadata using
functools.wraps.
"""

from functools import wraps

def caches(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_tup = tuple(args) + tuple(sorted(kwargs.items()))
        if arg_tup in cache:
            return cache[args_set]

        result = func(*args, **kwargs)
        cache[arg_tup] = result

        return result
    return wrapper

@caches
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
