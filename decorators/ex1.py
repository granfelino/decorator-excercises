"""
Script with a decorator that prints something before running the decorated
function.

The decorator function takes a callable as an argument and returns a wrapper
which, before running the callable, prints a string. The wrapper replaces the
passed callable - does not preserve metadata (missing functools.wraps).
"""

def func_started(func):
    def wrapper(*args, **kwargs):
        print("Function started.")
        return func(*args, **kwargs)
    return wrapper

@func_started
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")

    hello("Jack")
