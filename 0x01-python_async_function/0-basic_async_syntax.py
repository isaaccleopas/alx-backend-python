#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer argument"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Returns a random float between 0 and 10"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
