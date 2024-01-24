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


def slow_response(method: Callable[[str], str]) -> Callable[[str], str]:
    """Returns a function that tests get_page by simulating a slow response."""

    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """ Calls the method with the url http://slowwly.robertomurray.co.uk
        """
        return method("http://slowwly.robertomurray.co.uk")

    return wrapper


def get_page(url: str) -> str:
    """Tracks how many time a URL was accessed."""

    key = "count:" + url

    if not r.exists(key):
        r.setex(key, 10, 1)
    else:
        r.incr(key)

    res = requests.get(url)
    return res.text
