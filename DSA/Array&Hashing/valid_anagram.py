# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}
        for a, b in zip(s, t):
            char_map.setdefault(a, 0)
            char_map.setdefault(b, 0)

            char_map[a] += 1
            char_map[b] -= 1

        for val in char_map.values():
            if val != 0:
                return False

        return True
