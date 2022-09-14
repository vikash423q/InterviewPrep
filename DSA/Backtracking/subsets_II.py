from typing import List

#   https://leetcode.com/problems/subsets-ii/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def subset(i: int, sub: List[int]):
            if i >= len(nums):
                res.add(tuple(sub))
                return

            subset(i + 1, sub)
            subset(i + 1, sub + [nums[i]])

        res = set()
        subset(0, [])
        return res
