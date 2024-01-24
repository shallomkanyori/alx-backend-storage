#!/usr/bin/env python3
"""Wrting strings to Redis

Classes:
    Cache
"""
import redis
import uuid
from typing import Union


class Cache():
    """Represents a Redis cache."""

    def __init__(self):
        """Initializes and instance of Cache."""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis with a random key and returns the key."""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
