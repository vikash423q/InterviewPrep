from typing import List

#   https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, s):
            if len(s) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != s[0]:
                return False

            # print(i, j, s)

            board[i][j] = '*'

            for dr in dirs:
                if dfs(i + dr[0], j + dr[1], s[1:]):
                    return True

            board[i][j] = s[0]
            return False

        char_map = {}
        for i in range(m):
            for j in range(n):
                char_map[board[i][j]] = char_map.get(board[i][j], 0) + 1

        for char in word:
            char_map[char] = char_map.get(char, 0) - 1

        for k, v in char_map.items():
            if v < 0:
                return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True

        return False

