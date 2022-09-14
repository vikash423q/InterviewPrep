from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, len(dp)):
            if dp[i] == 1:
                continue

            options = []
            for coin in coins:
                if i > coin and dp[i - coin] > 0:
                    options.append(dp[i - coin])

            if min(options, default=0) <= 0:
                dp[i] = -1
            else:
                dp[i] = min(options) + 1

        return dp[-1]
