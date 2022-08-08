from typing import Optional

#   https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.path(root)[1]

    def path(self, root):
        if not root:
            return -1, 0
        ld, lmax = self.path(root.left)
        rd, rmax = self.path(root.right)
        depth = 1 + max(ld, rd)
        dia = 2 + ld + rd
        return depth, max(dia, max(lmax, rmax))
