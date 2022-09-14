from typing import List


#   https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]

        res = max_so_far
        for n in nums[1:]:
            temp = max(n, max_so_far * n, min_so_far * n)
            min_so_far = min(n, max_so_far * n, min_so_far * n)

            max_so_far = temp
            res = max(res, max_so_far)

        return res
