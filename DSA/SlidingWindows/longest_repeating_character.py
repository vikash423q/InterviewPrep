class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = 0
        max_count = 0
        char_map = {}
        while j < len(s):
            char_map.setdefault(s[j], 0)
            char_map[s[j]] += 1

            w = j - i + 1
            max_rep = max(char_map.values(), default=0)

            while w - max_rep > k:
                char_map[s[i]] -= 1
                i += 1
                w = j - i + 1
                max_rep = max(char_map.values(), default=0)

            max_count = max(max_count, w)

            j += 1

        return max_count
