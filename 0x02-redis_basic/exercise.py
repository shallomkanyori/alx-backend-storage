#!/usr/bin/env python3
"""Contains the Cache class that represents a Redis cache.

Classes:
    Cache
"""
import functools
import redis
import uuid
from typing import Union, Callable, TypeVar, Any


T = TypeVar("T", str, bytes, int, float)


def count_calls(method: Callable) -> Callable:
    """Returns a function that counts the number of times a method is called"""

    @functools.wraps(method)
    def counter(self, *args, **kwargs) -> Any:
        """The counter function."""

        if isinstance(self._redis, redis.Redis):
            key = method.__qualname__
            self._redis.incr(key)

        return method(self, *args, **kwargs)

    return counter


def call_history(method: Callable) -> Callable:
    """Returns a function that stores the input/output history for a function.
    """

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Stores input and outputs"""
        pref = method.__qualname__
        outputs = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(pref + ":inputs", str(args))
            self._redis.rpush(pref + ":outputs", outputs)

        return outputs

    return wrapper


class Cache():
    """Represents a Redis cache."""

    def __init__(self):
        """Initializes and instance of Cache."""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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