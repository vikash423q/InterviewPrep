#   https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'(': ')', '[': ']', '{': '}'}

        arr = []
        for c in s:
            if c in char_map:
                arr.append(c)

            if c in char_map.values():
                top = arr[-1] if arr else None
                if char_map.get(top) == c:
                    arr.pop()
                else:
                    return False

        return len(arr) == 0
