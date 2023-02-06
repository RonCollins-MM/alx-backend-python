#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async function that spawns `wait_random` function `n` times.

    Parameters
    ----------
    n : int
        The number of times to spawn the `wait_random` function
    max_delay: int
        The maximum number of times a function should wait

    Returns
    -------
    list: float
        A list of all delays
    """
    fcts = [
        wait_random(max_delay) for i in range(n)
    ]
    rs = []
    for x in asyncio.as_completed(fcts):
        r = await x
        rs.append(r)
    return rs
