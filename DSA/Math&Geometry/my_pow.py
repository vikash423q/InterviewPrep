#   https://leetcode.com/problems/powx-n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1 or n == 1:
            return x

        x = 1 / x if n < 0 else x
        n = abs(n)

        if n % 2:
            pw = self.myPow(x, n // 2)
            pw *= pw * x
        else:
            pw = self.myPow(x, n // 2)
            pw *= pw

        return pw
