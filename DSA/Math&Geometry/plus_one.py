from typing import List

#   https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        summed = []

        i = len(digits) - 1
        c = 1
        while i >= 0:
            d = digits[i]

            n = d + c
            c = n // 10
            summed.append(n % 10)

            i -= 1

        if c:
            summed.append(c)

        return summed[::-1]
