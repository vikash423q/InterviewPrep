#   https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        dp = [0] * (len(s) + 1)
        n = len(dp)

        dp[n - 1] = 1
        dp[n - 2] = 1

        i = n - 3
        while i >= 0:
            num = int(s[i:i + 2])
            if num in [10, 20]:
                dp[i] = dp[i + 1]
                i -= 1
                if i >= 0:
                    dp[i] = dp[i + 1]
            elif num % 10 == 0:
                return 0
            elif 10 < num <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
            i -= 1

        return dp[0]
