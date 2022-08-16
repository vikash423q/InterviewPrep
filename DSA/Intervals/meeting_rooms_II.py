from typing import List

#   https://leetcode.com/problems/meeting-rooms-ii/


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([n[0] for n in intervals])
        end = sorted([n[1] for n in intervals])

        i = j = 0
        max_so_far = count = 0
        while i < len(start) and j < len(end):
            # meeting starts -> + 1
            if start[i] < end[j]:
                count += 1
                i += 1
            # meeting ends -> - 1
            else:
                count -= 1
                j += 1

            max_so_far = max(max_so_far, count)

        return max_so_far
