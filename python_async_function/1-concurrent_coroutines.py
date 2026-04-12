#!/usr/bin/env python3
"""ResulShafili"""

import asyncio
import bisect
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """this is a function returns list of times"""
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        bisect.insort(delays, delay)
    return delays
