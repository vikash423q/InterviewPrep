from typing import List


#   https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])

        out = []
        top, bottom, left, right = 0, n - 1, 0, m - 1

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                out.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                out.append(matrix[i][right])
            right -= 1

            if top > bottom or left > right:
                break

            for i in range(right, left - 1, -1):
                out.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                out.append(matrix[i][left])
            left += 1

        return out
