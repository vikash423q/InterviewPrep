from typing import List


#   https://leetcode.com/problems/counting-bits


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp


if __name__ == "__main__":
    size = 3
    m = [[(i, j) for j in range(size)] for i in range(size)]

    t = [[((i+size)%size+j, (i+j)%size) for (i,j) in row] for row in m]


