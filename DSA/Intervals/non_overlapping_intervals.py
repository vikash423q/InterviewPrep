from typing import List

#   https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda interval: interval)
        print(intervals)

        i = 1
        count = 0
        last = intervals[0]
        while i < len(intervals):
            # current start is smaller than last end
            if intervals[i][0] < last[1]:
                # last has greater end, deleting and setting current as last
                if intervals[i][1] < last[1]:
                    last = intervals[i]
                count += 1
            # no overlap found
            else:
                last = intervals[i]

            i += 1

        return count
