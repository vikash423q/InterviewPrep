from typing import List


#   https://leetcode.com/problems/word-search-ii/


class Trie:
    def __init__(self):
        self.end = False
        self.count = 0
        self.nodes = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        [self.add_word(root, wd) for wd in words]

        result = []

        def backtrack(i, j, trie, wd):
            if trie.end:
                result.append(wd)
                trie.end = False
                self.remove(root, wd)
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
                    board[i][j] not in trie.nodes:
                return

            saved = board[i][j]
            board[i][j] = '#'

            for r, c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if saved not in trie.nodes:
                    break
                backtrack(i + r, j + c, trie.nodes[saved], wd + saved)

            board[i][j] = saved

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, root, '')

        return result

    def add_word(self, trie: Trie, wd: str):
        if not wd:
            trie.end = True
            return

        if wd[0] not in trie.nodes:
            trie.count += 1
            trie.nodes[wd[0]] = Trie()
        self.add_word(trie.nodes[wd[0]], wd[1:])

    def remove(self, trie: Trie, wd: str, count=0):
        if not wd:
            trie.end = False
            return 0 if trie.nodes else count

        high = self.remove(trie.nodes[wd[0]], wd[1:], count)

        if high - trie.count == 1 and trie.count == 1:
            del trie.nodes[wd[0]]

        return high
