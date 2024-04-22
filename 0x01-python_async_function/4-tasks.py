#!/usr/bin/env python3
"""The code is nearly identical to wait_n except
task_wait_random is being called."""
import asyncio
from typing import List, Callable

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n except
    task_wait_random is being called."""
    list = []
    for _ in range(n):
        list.append(wait_random(max_delay))
    res = await asyncio.gather(*list)
    return sorted(res)
