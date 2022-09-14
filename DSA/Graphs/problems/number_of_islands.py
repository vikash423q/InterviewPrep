from typing import List

#   https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        possibleIslands = [-1] * (n * m + 1)

        def dfs(i: int, j: int, color: int):
            if i < 0 or i >= n:
                return
            elif j < 0 or j >= m:
                return
            elif (i, j) in visited:
                return
            elif grid[i][j] == '0':
                return

            possibleIslands[i * m + j] = color
            visited.add((i, j))

            dfs(i + 1, j, color)
            dfs(i, j + 1, color)
            dfs(i - 1, j, color)
            dfs(i, j - 1, color)

        for i in range(n):
            for j in range(m):
                dfs(i, j, i * m + j)

        possibleIslands = set(possibleIslands)
        possibleIslands.remove(-1)
        return len(possibleIslands)
