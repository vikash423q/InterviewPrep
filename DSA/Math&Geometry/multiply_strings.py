#   https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = ['0']*(len(num1) + len(num2))
        for i, n2 in enumerate(reversed(num2)):
            c = 0
            for j, n1 in enumerate(reversed(num1)):
                n = int(n1) * int(n2) + c + int(res[i +j])
                s = n % 10
                c = n // 10
                res[i + j] = str(s)

            res[i + j + 1] = str(c)

        res = res[:-1] if res[-1] == '0' else res
        prod = "".join(reversed(res))
        return prod
