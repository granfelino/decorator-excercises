"""
This script contains a wrapper which works both on sync and async functions,
discerning between the two during function decoration. 

IMPORTANT:
Using wraps(func)(wrapper) ensures that only the used wrapper will wrap the
decorated function and is thus the correct way to do such a thing.
"""

from functools import wraps
from typing import Callable, Any
import asyncio

def decor(func: Callable[..., Any]) -> Callable[..., Any]:
    def sync_wrapper(*args, **kwargs):
        print("sync decorator")
        return func(*args, **kwargs)

    async def async_wrapper(*args, **kwargs):
        print("async decorator")
        return await func(*args, **kwargs)

    wrapper = async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
    return wraps(func)(wrapper)

@decor
def hello() -> None:
    print("hello")

@decor
async def hello_delay(delay: float) -> None:
    await asyncio.sleep(delay)
    print("hello delayed")

async def main() -> None:
    hello()
    await hello_delay(1)

if __name__ == "__main__":
    asyncio.run(main())
