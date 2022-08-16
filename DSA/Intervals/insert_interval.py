from typing import List

#   https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                newInterval = [min(newInterval[0], interval[0]),
                               max(newInterval[1], interval[1])]
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

        return res + [newInterval]
