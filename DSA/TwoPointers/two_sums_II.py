from typing import List

#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted


# same solution as two_sum works here, but since it's sorted we can use two pointers approach mentioned below
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_set = {num: i for i, num in enumerate(numbers)}

        for i, num in enumerate(numbers):
            if target - num in num_set:
                return [i + 1, num_set[target - num] + 1]


class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            small = numbers[i]
            big = numbers[j]

            # if sum is greater than target decrease from last
            if small + big > target:
                j -= 1
            # if sum is lesser than target increase from start
            elif small + big < target:
                i += 1
            else:
                return [i + 1, j + 1]
