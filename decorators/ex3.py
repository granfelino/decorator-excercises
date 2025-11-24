"""
Script with a decorator that runs the function passed to it twice. The decorator
returns a function replacing the original one. Does not preserve metadata.
"""

def run_twice(func):
    def wrapper(*args, **kwargs):
        for _ in range(2):
            func(*args, **kwargs)
    return wrapper

@run_twice
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    hello("Mike")
