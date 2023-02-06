#!/usr/bin/env python3
""" asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function that waits for a random delay between 0 and
    max_delay and then returns.

    Parameters
    ----------
    max_delay : int (default = 10)
        maximum time in seconds the function should wait
    
    Returns
    -------
    x : float
        The amount of time the function actually waited

    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
