#!/usr/bin/env python3
""" that takes in 2 int arguments (in this order):n and max_delay.
You will spawn wait_random n times with the specified max_delay."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ that takes in 2 int arguments (in this order):n and max_delay.
    You will spawn wait_random n times with the specified max_delay."""
    list = []
    for _ in range(n):
        list.append(wait_random(max_delay))
    res = await asyncio.gather(*list)
    return sorted(res)
