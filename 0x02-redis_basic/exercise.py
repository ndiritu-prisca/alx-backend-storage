#!/usr/bin/env python3
"""Writing strings to REDIS"""

import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
        """
        A decorator that takes a single method Callable argument and returns
        a Callable
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

class Cache:
    """The module's class Cache"""
    def __init__(self):
        """Initializing class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
