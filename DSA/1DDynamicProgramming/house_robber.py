from typing import List


#   https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        n = len(dp)

        dp[n - 1] = 0
        dp[n - 2] = nums[n - 2]

        i = n - 3
        while i >= 0:
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
            i -= 1

        return dp[0]
