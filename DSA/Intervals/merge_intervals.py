from typing import List

#   https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda interval: interval[0])

        res = []
        for i in range(len(intervals) - 1):
            curr, nxt = intervals[i], intervals[i + 1]

            if curr[0] <= nxt[1] and curr[1] >= nxt[0]:
                # overlapping
                intervals[i + 1] = [min(curr[0], nxt[0]), max(curr[1], nxt[1])]
            else:
                res.append(curr)

        res.append(intervals[-1])
        return res
