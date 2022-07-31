from typing import List


# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {num: idx for idx, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if target - num in num_idx_map:
                j = num_idx_map[target - num]
                if i == j:
                    continue
                return [i, j]
