from typing import List

#   https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combination(i: int, subset: List[int], summ: int):
            if summ == target:
                res.add(tuple(subset))
                return
            if summ > target:
                return

            prev = -1
            print(i)
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue

                subset.append(candidates[j])
                combination(j + 1, subset, summ + candidates[j])
                subset.pop()

                prev = candidates[j]

        res = set()
        combination(0, [], 0)
        return res
