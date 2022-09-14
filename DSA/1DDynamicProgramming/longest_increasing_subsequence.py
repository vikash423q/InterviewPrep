from typing import List


#   https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [0] * len(nums)

        i = 1
        lis[0] = res = 1
        for n in nums[1:]:
            lis[i] = 1 + max([lis[j] for j in range(i) if nums[j] < n], default=0)
            res = max(res, lis[i])
            i += 1

        return res
