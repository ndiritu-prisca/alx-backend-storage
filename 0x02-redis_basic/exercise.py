#!/usr/bin/env python3
"""Writing strings to REDIS"""

import uuid
import redis
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None):
        """
        A method that take a key string argument and an optional Callable
        argument named fn
        """
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn:
                return fn(data)
            return data
        return None

    def get_str(self, key: str):
        """Method that gets a string"""
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str):
        """Method that gets an int"""
        return self.get(key, fn=int)


# Test cases
cache = Cache()


TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
