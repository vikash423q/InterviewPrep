#   https://leetcode.com/problems/reverse-bits


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            bit = n % 2
            n = n >> 1
            res = (res << 1) + bit
            i += 1

        return res
