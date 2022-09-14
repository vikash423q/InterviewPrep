from typing import List


#   https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local = max_so_far = nums[0]

        for num in nums[1:]:
            local += num
            max_so_far = max(max_so_far, local, num)
            local = max(local, num, 0)

        return max_so_far
