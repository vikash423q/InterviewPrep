from typing import List


#   https://leetcode.com/problems/container-with-most-water


class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:

            area = min(height[left], height[right]) * (right - left)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if area > max_area:
                max_area = area

        return max_area
