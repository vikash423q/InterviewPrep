from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        p = 0
        while p < len(matrix) / 2:
            k = 0
            n = len(matrix) - 1 - 2 * p
            while k < n:
                i, j = p, p + k
                temp = matrix[i][j]

                matrix[i][j] = matrix[i + n - k][j - k]
                i, j = i + n - k, j - k

                matrix[i][j] = matrix[i + k][j + n - k]
                i, j = i + k, j + n - k

                matrix[i][j] = matrix[i - n + k][j + k]
                i, j = i - n + k, j + k

                matrix[i][j] = temp
                k += 1
            p += 1


# easier solution: transpose and then reverse rows
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        for i in range(len(matrix)):
            j = i
            while j < len(matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1

        # reversing rows
        for i in range(len(matrix)):
            j, k = 0, len(matrix)-1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
