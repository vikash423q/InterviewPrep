from math import inf
from typing import List


#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) + 1
        sold = [-inf] * n
        held = [-inf] * n
        reset = [0] * n

        for i in range(1, n):
            sold[i] = held[i - 1] + prices[i - 1]
            held[i] = max(held[i - 1], reset[i - 1] - prices[i - 1])
            reset[i] = max(reset[i - 1], sold[i - 1])

        return max(sold[-1], held[-1], reset[-1])
