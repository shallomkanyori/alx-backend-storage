#!/usr/bin/env python3
"""Implement an expiring web cache and tracker

Functions:
    get_page(url)
"""
import functools
import redis
import requests
from typing import Callable

r = redis.Redis()


def cacher(method: Callable) -> Callable:
    """Returns a function that caches HTML content of url."""

    @functools.wraps(method)
    def wrapper(url) -> str:
        """ Calls the method and caches the result
        """

        ckey = "count:" + url
        rkey = "result:" + url

        r.incr(ckey)

        res = r.get(rkey)
        if res:
            return res.decode("utf-8")

        result = method(url)
        r.set(ckey, 1)
        r.setex(rkey, 10, result)

        return result

    return wrapper


@cacher
def get_page(url: str) -> str:
    """Tracks how many time a URL was accessed."""
    return requests.get(url).text
