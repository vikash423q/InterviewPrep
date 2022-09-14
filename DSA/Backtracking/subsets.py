from typing import List


#   https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(i: int, choices: List[int]):
            if i >= len(nums):
                ans.append(choices)
                return

            sub(i + 1, choices)
            sub(i + 1, choices + [nums[i]])

        ans = []
        sub(0, [])
        return ans
