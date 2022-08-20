#   https://leetcode.com/problems/find-median-from-data-stream/


import heapq


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        while self.large and -1 * self.small[0] > self.large[0]:
            lval = -1 * heapq.heappop(self.small)
            sval = heapq.heappop(self.large)
            heapq.heappush(self.large, lval)
            heapq.heappush(self.small, -1 * sval)

        while len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2:
            return -1 * self.small[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
