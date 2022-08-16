from typing import Optional


#   https://leetcode.com/problems/balanced-binary-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h, bal = self.height(root)
        return bal

    def height(self, root):
        if not root:
            return -1, True

        l, lbal = self.height(root.left)
        r, rbal = self.height(root.right)

        bal = (lbal and rbal) and abs(l - r) <= 1

        return 1 + max(l, r), bal
