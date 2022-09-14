from typing import List


#   https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        nJumps = 0

        while r < len(nums) - 1:
            furthest = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, furthest
            nJumps += 1

        return nJumps
