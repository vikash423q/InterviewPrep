from typing import List


#   https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def break_word(s):
            if not s:
                return True

            if s in dp:
                return dp[s]

            for wd in wordDict:
                if not s.startswith(wd):
                    continue
                res = break_word(s[len(wd):])
                if res:
                    dp[s] = True
                    return True

            dp[s] = False
            return False

        return break_word(s)
