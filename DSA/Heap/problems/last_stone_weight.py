#   https://leetcode.com/problems/last-stone-weight/


from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * st for st in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)

            if y - x:
                heapq.heappush(stones, x - y)

        return -1 * stones[0] if stones else 0
