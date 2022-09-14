#   https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        min_limit = -2 ** 31
        max_limit = 2 ** 31 - 1

        def recur(num, x):
            if x <= 0:
                return num // 10
            if min_limit > num or num > max_limit:
                return 0
            return recur((num + x % 10) * 10, x // 10)

        sign = 1 if x > 0 else -1
        return sign * recur(0, abs(x))
