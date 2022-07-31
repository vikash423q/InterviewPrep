from typing import List
from collections import defaultdict


# https://leetcode.com/problems/group-anagrams


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for s in strs:
            cnt = [0] * 26
            for char in s:
                cnt[ord(char) - ord('a')] += 1

            store[tuple(cnt)].append(s)

        return list(store.values())
