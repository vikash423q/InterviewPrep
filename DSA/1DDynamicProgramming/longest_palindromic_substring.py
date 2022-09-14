#   https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = 2 * len(s) - 1

        def expand_from_centre(i):
            i, j = i // 2, (i + 1) // 2
            sub = ''
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break

                sub = s[i:j + 1]
                i -= 1
                j += 1

            return sub

        res = ""
        for i in range(n):
            pal = expand_from_centre(i)
            res = pal if len(pal) > len(res) else res

        return res
