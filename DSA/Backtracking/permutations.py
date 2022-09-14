from typing import List


#   https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(i: int, curr):
            if i >= len(curr):
                res.append(curr)
                return

            j = i
            while j < len(curr):
                x = list(curr)
                x[i], x[j] = x[j], x[i]
                permutation(i + 1, list(x))
                j += 1

        res = []
        permutation(0, list(nums))
        return res
