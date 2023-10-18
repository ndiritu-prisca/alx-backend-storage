#!/usr/bin/env python3
"""Writing strings to REDIS"""

import uuid
import redis
from typing import Union


class Cache:
    """The module's class Cache"""
    def __init__(self):
        """Initializing class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a key"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
