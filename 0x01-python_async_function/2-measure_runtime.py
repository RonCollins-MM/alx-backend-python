#!/usr/bin/env python3
""" asynchronous coroutine """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Async function that measures total runtime for various other async
    coroutines

    Parameters
    ----------
    n : int
        The number of times to measure
    max_delay: int
        Maximum allowed delay time

    Returns
    -------
    float
        The total time divided by n
    """
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - t0) / n)
