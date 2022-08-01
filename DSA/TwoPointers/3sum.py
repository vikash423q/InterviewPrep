from typing import List


#   https://leetcode.com/problems/3sum


class Solution:
    def threeSum(self, nums: List[int]):
        nums.sort()
        res = set()

        i = 0
        while i < len(nums) - 2:
            tgt = -nums[i]
            j, k = i + 1, len(nums) - 1

            while j < k:
                small = nums[j]
                big = nums[k]

                if small + big > tgt:
                    k -= 1
                elif small + big < tgt:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1

            i += 1

        return res
