from typing import List


#   https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ['(']
        total = []
        self.gen(total, s, n - 1, n)
        return total

    def gen(self, total: list, st: list, op: int, cl: int):
        if op == 0 and cl == 0:
            total.append("".join(st))
        if op:
            st.append('(')
            self.gen(total, st, op - 1, cl)
            st.pop()
        if cl > op:
            st.append(')')
            self.gen(total, st, op, cl - 1)
            st.pop()
