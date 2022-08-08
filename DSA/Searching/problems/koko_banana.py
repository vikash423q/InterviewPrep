import math
from typing import List


#   https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k: int):
            t = 0
            for p in piles:
                t += math.ceil( p /k)
            return t

        n = sum(piles)

        k_min = math.ceil( n /h)
        k_max = max(piles)

        while k_min <k_max:
            k = (k_min +k_max )//2
            t = finish(k)
            if t <= h:
                k_max = k
            else:
                k_min = k+ 1
        return k_max
