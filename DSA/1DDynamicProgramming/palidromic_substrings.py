#   https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = 2 * len(s) - 1
        res = 0

        def expand_from_centre(i):
            nonlocal res

            i, j = i // 2, (i + 1) // 2

            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                res += 1
                i -= 1
                j += 1

        for i in range(n):
            expand_from_centre(i)

        return res
