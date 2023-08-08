#!/usr/bin/env python3
"""This coroutine will loop 10x, each time asynchronously wait 1 second"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Returns a random num in range 10 and await i sec"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
