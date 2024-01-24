#!/usr/bin/env python3
"""Contains the Cache class that represents a Redis cache.

Classes:
    Cache
"""
import functools
import redis
import uuid
from typing import Union, Callable, TypeVar, Any, cast


T = TypeVar("T", str, bytes, int, float)


def count_calls(method: Callable) -> Callable:
    """Returns a function that counts the number of times a method is called"""

    @functools.wraps(method)
    def counter(*args: Any, **kwargs: Any) -> Any:
        """The counter function."""
        self = args[0]
        key = method.__qualname__

        self._redis.incr(key)
        return method(*args, **kwargs)

    return counter


class Cache():
    """Represents a Redis cache."""

    def __init__(self):
        """Initializes and instance of Cache."""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a random key and returns the key."""

        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable[[bytes], T] = None) -> Union[T, None]:
        """Returns the value associated with `key`.
        Optionally converts it back to the desired format using `fn`.
        """

        data = self._redis.get(key)
        if data and fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """Returns the string value at `key`"""

        return self.get(key, lambda x: str(x))

    def get_int(self, key: str) -> Union[int, None]:
        """Returns the int value at `key`"""

        return self.get(key, lambda x: int(x))
