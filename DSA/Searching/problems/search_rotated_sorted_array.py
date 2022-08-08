from typing import List


#   https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(l, r):
            while l <= r:
                m = (l + r )//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        l, r = 0, len(nums ) -1
        last = nums[0]

        start = 0
        while l <= r:
            m = (l + r )//2
            if nums[m] < nums[ m -1]:
                start = m
                break
            if last > nums[m]:
                r = m- 1
            else:
                l = m + 1

        a = bs(0, start - 1)
        if a != -1:
            return a

        b = bs(start, len(nums) - 1)
        if b != -1:
            return b

        return -1
