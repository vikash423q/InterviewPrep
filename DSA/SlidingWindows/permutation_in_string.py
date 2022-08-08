#   https://leetcode.com/problems/permutation-in-string


# The solution requires a window of fixed size i.e. len(s1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        char = [0] * 26
        for c in s1:
            char[ord(c) - ord('a')] += 1

        cnt = [0] * 26

        for k in range(len(s1) - 1):
            cnt[ord(s2[k]) - ord('a')] += 1

        i, j = 0, len(s1) - 1
        while j < len(s2):
            cnt[ord(s2[j]) - ord('a')] += 1

            if cnt == char:
                return True

            cnt[ord(s2[i]) - ord('a')] -= 1

            i += 1
            j += 1

        return False
