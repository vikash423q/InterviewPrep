from typing import List


#   https://leetcode.com/problems/trapping-rain-water


class Solution:
    def trap(self, height: List[int]) -> int:

        trapped = 0
        max_left, max_right = 0, 0
        i, j = 0, len(height) - 1

        while i < j:
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])

            min_so_far = min(max_right, max_left)

            if height[i] < height[j]:
                if height[i] < min_so_far:
                    trapped += min_so_far - height[i]
                i += 1
            else:
                if height[j] < min_so_far:
                    trapped += min_so_far - height[j]
                j -= 1

        return trapped
