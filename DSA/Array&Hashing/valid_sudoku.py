from typing import List


#   https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        store = {}
        for r in range(9):
            # row
            for c in range(9):
                # column
                value = board[r][c]
                if value == '.':
                    continue
                # square block idx 0 - 9
                b = (r // 3) * 3 + c // 3
                store.setdefault(value, [set(), set(), set()])

                if r in store[value][0]:
                    return False
                if c in store[value][1]:
                    return False
                if b in store[value][2]:
                    return False

                store[value][0].add(r)
                store[value][1].add(c)
                store[value][2].add(b)

        return True
