"""
This script contains a decorator factory which ensures that the calls of the
decorated function are limited within a specified timeframe.
"""

from functools import wraps
import time

class CallError(Exception):
    def __init__(self, msg: str, delta: float):
        self.delta = delta
        super().__init__(msg)

def call_limit(count: int, secs: float):
    current_count = 0
    start = time.perf_counter()
    end = start + secs

    def dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal current_count, start, end

            if time.perf_counter() > end:
                current_count = 0
                start = time.perf_counter()
                end = start + secs

            if current_count < count:
                result = func(*args, **kwargs)
                current_count += 1
                return result
            else:
                retry_delta = end - time.perf_counter()
                raise CallError(f"Call limit reached in a specified timeframe. Retry in {retry_delta:.6f} seconds.", retry_delta)
        return wrapper
    return dec

@call_limit(5, 1)
def hello(name):
    print(f"Hello {name}!")

if __name__ == "__main__":
    while True:
        try:
            hello("mike")
        except CallError as e:
            time.sleep(e.delta)
