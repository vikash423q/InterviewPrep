#   https://leetcode.com/problems/lru-cache


from collections import deque, OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cmap = {}
        self.ll = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cmap:
            return -1
        self.ll.remove(key)
        self.ll.appendleft(key)
        return self.cmap[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cmap:
            self.ll.appendleft(key)
            if len(self.ll) > self.capacity:
                prev = self.ll.pop()
                del self.cmap[prev]
        self.ll.remove(key)
        self.ll.appendleft(key)
        self.cmap[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache2(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        elif len(self) > self.capacity:
            self.popitem(last=True)
        self[key] = value
