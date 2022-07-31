from typing import List

#   https://leetcode.com/problems/product-of-array-except-self


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans1 = [1] * len(nums)
        ans2 = [1] * len(nums)

        for i in range(1, len(nums)):
            ans1[i] = ans1[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            ans2[i] = ans2[i + 1] * nums[i + 1]

        ans = [i * j for i, j in zip(ans1, ans2)]
        return ans

