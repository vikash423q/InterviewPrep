from typing import List


#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i = 0
        for j in range(1, len(prices)):

            max_profit = max(max_profit, prices[j] - prices[i])

            if prices[i] > prices[j]:
                i = j

            j += 1

        return max_profit
