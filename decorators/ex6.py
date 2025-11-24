"""
This script contains a decorator that logs the result of the decorated function
using the logging module. This decorator preserves metadata of the decorated
function using functools.wraps
"""

from functools import wraps
import logging

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

def log_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Result of {func.__name__}: {result}")
        return result
    return wrapper

@log_return
def hello(name: str):
    return f"Hello {name}!"

if __name__ == "__main__":
    hello("Mike")
