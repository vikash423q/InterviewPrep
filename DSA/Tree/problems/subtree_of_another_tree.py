from typing import Optional


#   https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, p, q):
        if p and not q:
            return False
        elif q and not p:
            return False
        elif not q and not p:
            return True

        return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)
