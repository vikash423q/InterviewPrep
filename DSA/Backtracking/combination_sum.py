from typing import List


#   https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(i: int, choices: List[int], sums: int):
            if i >= len(candidates) or sums > target:
                return
            if sums == target:
                res.append(choices)
                return

            combination(i, choices + [candidates[i]], sums + candidates[i])
            combination(i + 1, choices, sums)

        res = []
        combination(0, [], 0)
        return res
