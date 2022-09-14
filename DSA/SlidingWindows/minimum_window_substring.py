# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        win_map = {}
        tgt_map = {}

        def valid():
            for c in tgt_map:
                if tgt_map[c] > win_map.get(c, 0):
                    return False
            return True

        for char in t:
            tgt_map.setdefault(char, 0)
            tgt_map[char] += 1

        i = j = 0
        while j < len(s):
            win_map[s[j]] = win_map.get(s[j], 0) + 1
            if valid():
                break
            j += 1

        if not valid():
            return ""

        l, r = i, j
        left = i
        right = j
        while left <= right and right < len(s):
            if valid():
                l, r = left, right + 1
                win_map[s[left]] -= 1
                left += 1
                continue

            win_map[s[left]] -= 1
            left += 1
            right += 1
            if right < len(s):
                win_map[s[right]] = win_map.get(s[right], 0) + 1

        return s[l: r]
