import math

from typing import Optional

#   https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_p, max_limb = self.maxPath(root)
        return max_p

    def maxPath(self, root):
        if not root:
            return -math.inf, -math.inf

        lm, ll = self.maxPath(root.left)
        rm, rl = self.maxPath(root.right)

        maxl = max(root.val, root.val + ll, root.val + rl)
        maxp = max(lm, rm, root.val + ll + rl, maxl)

        return maxp, maxl
