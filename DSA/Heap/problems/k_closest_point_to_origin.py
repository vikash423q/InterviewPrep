#   https://leetcode.com/problems/k-closest-points-to-origin/


from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x ** 2 + y ** 2, x, y) for x, y in points]
        heapq.heapify(points)

        res = [heapq.heappop(points) for _ in range(k)]
        return [[x, y] for _, x, y in res]
