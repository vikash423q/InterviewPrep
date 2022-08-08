from typing import List


#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m, last = 0, nums[0]
        while l <= r:
            if nums[m] <= nums[m-1]:
                return nums[m]
            if nums[m] < last:
                r = m - 1
            else:
                l = m + 1
            last = nums[m]
            m = (l + r)//2



