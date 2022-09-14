from typing import List


#   https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, val: int, arr, visited: set = None):
            if visited is None:
                visited = set()

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if (i, j) in visited:
                return

            if heights[i][j] < val:
                return

            visited.add((i, j))

            arr[i][j] = True
            val = heights[i][j]

            dfs(i + 1, j, val, arr, visited)
            dfs(i, j + 1, val, arr, visited)
            dfs(i - 1, j, val, arr, visited)
            dfs(i, j - 1, val, arr, visited)

        for i in range(m):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, n - 1, heights[i][n - 1], atl)

        for i in range(n):
            dfs(0, i, heights[0][i], pac)
            dfs(m - 1, i, heights[m - 1][i], atl)

        res = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])

        return res
