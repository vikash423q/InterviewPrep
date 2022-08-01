#   https://leetcode.com/problems/valid-palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            char_i = s[i].lower()
            char_j = s[j].lower()

            if not char_i.isalnum():
                i += 1
                continue
            if not char_j.isalnum():
                j -= 1
                continue

            if char_i != char_j:
                return False

            i += 1
            j -= 1

        return True
