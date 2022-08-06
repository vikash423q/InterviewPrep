#   https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        smap = {}
        max_count = 0
        for j in range(len(s)):
            if s[j] in smap and i <= smap[s[j]]:
                i = smap[s[j]] + 1
            max_count = max(max_count, j - i + 1)
            smap[s[j]] = j

        return max_count
