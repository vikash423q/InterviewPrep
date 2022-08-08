from typing import List


#   https://leetcode.com/problems/evaluate-reverse-polish-notation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '*', '/', '-'}
        nums = []
        a = int(tokens[0])
        for op in tokens:
            if op in operands:
                b, a = nums.pop(), nums.pop()
                if op == '+':
                    a = a + b
                elif op == '*':
                    a = a * b
                elif op == '/':
                    a = int(a / b)
                elif op == '-':
                    a = a - b
                nums.append(a)
            else:
                nums.append(int(op))

        return a
