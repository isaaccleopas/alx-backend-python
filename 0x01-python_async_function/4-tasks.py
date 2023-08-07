#!/usr/bin/env python3
"""Takes the code from wait_n and alter it into a new function task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """2 int arguments (in this order): n and max_delay"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
