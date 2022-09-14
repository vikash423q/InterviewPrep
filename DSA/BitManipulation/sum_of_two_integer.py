#   https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        sign = -1 if a * b < 0 else 1
        a, b = abs(a), abs(b)
        if a == 0 or b == 0:
            return a or b
        return sign * self.getSum(a ^ b, (a & b) << 1)
