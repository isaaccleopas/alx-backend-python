#!/usr/bin/env python3
"""Regular function syntax that takes an integer"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task from wait_random() coroutine"""
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
