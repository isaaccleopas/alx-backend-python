#!/usr/bin/env python3
"""
This coroutine that will execute async_comprehension
4x in parallel using asyncio.gather.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime and return it"""
    start_time = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_time = time.perf_counter()
    return end_time - start_time
