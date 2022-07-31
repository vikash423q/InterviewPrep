from typing import List
from heapq import heappush, heappop

#   https://leetcode.com/problems/longest-consecutive-sequence


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heap = []
        for num in nums:
            heappush(heap, num)

        i = 0
        count = max_count = 1
        last_val = heappop(heap)
        while i < len(nums) - 1:
            val = heappop(heap)
            if val - last_val == 1:
                count += 1
            elif val - last_val > 1:
                count = 1

            last_val = val
            if count > max_count:
                max_count = count
            i += 1

        return max_count


#   More Cleaner Solution
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # check if it's start of the sequence
            if n - 1 not in num_set:
                length = 1

                # check how long is the sequence is
                while n + length in num_set:
                    length += 1

                longest = max(length, longest)

        return longest
