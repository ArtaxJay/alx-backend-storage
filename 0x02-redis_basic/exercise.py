#!/usr/bin/env python3
"""Module declares a redis class and methods"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count how many times methods of Cache class are called'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''store the history of inputs and outputs for a particular function'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    '''display the history of calls of a particular function.'''
    r = redis.Redis()
    func_name = fn.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))


class Cache:
    '''Creates a Redis Cache class'''
    def __init__(self):
        '''stores instance of d redis client as a private variable & flush'''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Method does:
            takes a ~data~ arg and rets a str
            generates a random key using ~uuid~
        '''
        uuid_generated_random_key = str(uuid4())
        self._redis.set(uuid_generated_random_key, data)
        return uuid_generated_random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
        Method does:
        parses redis byte str, b"str", data frm server back 2 desired utf-8 str
        '''
        parsed_utf_8_str = self._redis.get(key)
        if fn:
            parsed_utf_8_str = fn(parsed_utf_8_str)
        return parsed_utf_8_str

    def get_str(self, key: str) -> str:
        '''automatically parametrize Cache.get with correct conversion func'''
        parsed_utf_8_str = self._redis.get(key)
        return parsed_utf_8_str.decode("utf-8")

    def get_int(self, key: str) -> int:
        '''same as get_str() above, but with ints'''
        parsed_utf_8_str = self._redis.get(key)
        try:
            parsed_utf_8_str = int(parsed_utf_8_str.decode("utf-8"))
        except Exception:
            parsed_utf_8_str = 0
        return
