#   https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        v = set()
        v.add(n)

        num = n
        while num != 1:

            k = num
            num = 0
            while k:
                num += (k % 10) ** 2
                k = k // 10

            if num in v:
                return False
            v.add(num)

        return True
