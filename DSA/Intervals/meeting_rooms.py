from typing import List

#   https://leetcode.com/problems/meeting-rooms/


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        for i in range(len(intervals) - 1):
            curr = intervals[i]
            nxt = intervals[i + 1]

            if nxt[0] < curr[1]:
                return False

        return True
