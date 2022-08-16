from typing import Optional

#   https://leetcode.com/problems/same-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q:
            return False
        elif q and not p:
            return False
        elif not p and not q:
            return True

        lsame = self.isSameTree(p.left, q.left)
        rsame = self.isSameTree(p.right, q.right)

        return p.val == q.val and lsame and rsame
