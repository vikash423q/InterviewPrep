#   https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def backtrack(i, j, res):
            if res == s3 and i == len(s1) and j == len(s2):
                return True
            elif not s3.startswith(res):
                return False

            if (i, j, res) in dp:
                return dp[(i, j, res)]

            ans = False
            if i < len(s1):
                ans = ans or backtrack(i + 1, j, res + s1[i])

            if j < len(s2):
                ans = ans or backtrack(i, j + 1, res + s2[j])

            dp[(i, j, res)] = ans

            return ans

        return backtrack(0, 0, "")
