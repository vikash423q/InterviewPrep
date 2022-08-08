#   https://leetcode.com/problems/time-based-key-value-store


class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, [])
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        idx = l - 1
        return "" if idx < 0 else arr[idx][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
