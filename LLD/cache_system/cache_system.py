# Should have multiple caching strategies
# should have only instance of the cache system
#

import time
from typing import Any, Dict
from collections import OrderedDict
from threading import Lock
from heapq import heappush, heappop
from abc import ABC, abstractmethod
from enum import Enum, auto


class CacheStrategy(Enum):
    LRU = auto()
    LFU = auto()


class DateItem:
    def __init__(self, key: str, value: Any, ttl: int = -1):
        self.key = key
        self.value = value
        self.ttl = ttl
        self.timestamp = time.time()


    def is_expired(self) -> bool:
        if self.ttl == -1:
            return False
        return time.time() - self.timestamp > self.ttl

    def __repr__(self):
        return f'{self.key}: {self.value}'


class CachingStrategy(ABC):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lock = Lock()

    @abstractmethod
    def put(self, item: DateItem, data: Dict[str, DateItem]):
        pass

    @abstractmethod
    def get(self, key, data: Dict[str, DateItem]) -> Any:
        pass

    @abstractmethod
    def evict(self, key, data: Dict[str, DateItem]):
        pass


class LRUStrategy(CachingStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.meta = OrderedDict()

    def put(self, item: DateItem, data: Dict[str, DateItem]):
        with self.lock:
            if len(data) == self.capacity:
                k, _ = self.meta.popitem()
                del data[k]

            data[item.key] = item
            self.meta[item.key] = item.key
            self.meta.move_to_end(item.key, last=False)


    def get(self, key, data: Dict[str, DateItem]) -> Any:
        with self.lock:
            if key not in data or data[key].is_expired():
                if key in data:
                    del data[key]
                    del self.meta[key]
                return
            self.meta.move_to_end(key, last=False)
            return data[key].value

    def evict(self, key, data: Dict[str, DateItem]):
        with self.lock:
            if key in data:
                del data[key]
                del self.meta[key]


class LFUStrategy(CachingStrategy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heap = []
        self.freq = {}

    def put(self, item: DateItem, data: Dict[str, DateItem]):
        with self.lock:
            if len(data) == self.capacity:

                f, key = heappop(self.heap)

                while key not in self.freq or f < self.freq[key]:
                    f, key = heappop(self.heap)

                del data[key]
                del self.freq[key]

            self.freq[item.key] = self.freq.get(item.key, 0) + 1
            heappush(self.heap, (self.freq[item.key], item.key))
            data[item.key] = item


    def get(self, key, data: Dict[str, DateItem]) -> Any:
        with self.lock:
            if key not in data or data[key].is_expired():
                if key in data:
                    del data[key]
                    del self.freq[key]
                return


            self.freq[key] = self.freq.get(key, 0) + 1
            heappush(self.heap, (self.freq[key], key))

            return data[key].value

    def evict(self, key, data: Dict[str, DateItem]):
        with self.lock:
            if key in data:
                del data[key]
                del self.freq[key]


class StrategyFactory:
    @staticmethod
    def get_strategy(cache_strategy: CacheStrategy, capacity: int):
        if cache_strategy == CacheStrategy.LRU:
            return LRUStrategy(capacity)
        elif cache_strategy == CacheStrategy.LFU:
            return LFUStrategy(capacity)

        raise Exception('Unknown strategy found!')


class Cache:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance

    def __init__(self, capacity: int, strategy_type: CacheStrategy):
        self.data: Dict[str, DateItem] = {}
        self.capacity = capacity
        self.strategy = StrategyFactory.get_strategy(strategy_type, capacity)


    def put(self, key: str, value: Any, ttl: int = -1):
        data_item = DateItem(key, value, ttl)
        self.strategy.put(data_item, self.data)

    def get(self, key: str) -> Any:
        return self.strategy.get(key, self.data)

    def evict(self, key: str):
        return self.strategy.evict(key, self.data)

    def list(self):
        print(self.data)


if __name__ == '__main__':
    # caches = [Cache(0, LRUStrategy(10)) for _ in range(10)]
    # print([id(cache) for cache in caches])

    cache = Cache(4, CacheStrategy.LFU)

    cache.put('1', 12343)
    cache.put('2', 765, ttl=2)
    print(cache.get('1'))
    cache.put('3', 12324354)
    print(cache.get('3'))
    print(cache.get('3'))
    time.sleep(2)
    print(cache.get('2'))
    cache.put('4', 6543)
    cache.put('5', 121)
    cache.get('5')
    cache.put('6', 121)
    cache.evict('4')
    cache.put('7', 121)
    cache.list()

