from typing import List


#   https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)

        cost.append(0)
        dp0 = cost[0]
        dp1 = cost[1]

        i = 2
        while i < len(dp):
            dp[i] = min(dp1, dp0) + cost[i]
            i += 1

        return dp[-1]