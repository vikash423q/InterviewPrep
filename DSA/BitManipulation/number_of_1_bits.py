#   https://leetcode.com/problems/number-of-1-bits


# using bit shift
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n >> 1
        return count


# using bit and
class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count
