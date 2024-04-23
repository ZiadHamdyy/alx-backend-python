#!/usr/bin/env python3
"""should measure the total runtime and return it"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """should measure the total runtime and return it"""
    start_time = time.time()
    for _ in range(3):
        await asyncio.gather(async_comprehension())
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time / 3
