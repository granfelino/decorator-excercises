"""
A decorator that does nothing else other than showcase preserving the 
decorated function's metadata. This decorator does basically nothing.
"""

from functools import wraps

def preserved(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@preserved
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
