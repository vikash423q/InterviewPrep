from typing import List


#   https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i, n in enumerate(nums):
            if n > target:
                continue
            for i in range(len(dp), -1, -1):
                if i + n <= target and dp[i]:
                    dp[i + n] = True

        return dp[target]
