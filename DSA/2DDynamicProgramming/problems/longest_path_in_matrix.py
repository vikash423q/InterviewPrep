from typing import List


#   https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        max_path = 0

        def dfs(i, j):
            nonlocal max_path
            if (i, j) in dp:
                return dp[(i, j)]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            dist = []
            for x, y in directions:
                if i + x < 0 or i + x >= len(matrix):
                    continue
                if j + y < 0 or j + y >= len(matrix[0]):
                    continue

                if matrix[i][j] < matrix[i + x][j + y]:
                    dist.append(dfs(i + x, j + y))

            dp[(i, j)] = 1 + max(dist, default=0)
            max_path = max(max_path, dp[(i, j)])
            return dp[(i, j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)

        return max_path
