from typing import Optional


#   https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, -2 ** 31 - 1, 2 ** 31)

    def valid(self, root, low, high) -> bool:
        if not root:
            return True

        valid = low < root.val < high
        if root.left and root.right:
            valid = root.left.val < root.val < root.right.val
        elif root.left:
            valid = root.left.val < root.val
        elif root.right:
            valid = root.right.val > root.val

        return valid and self.valid(root.left, low, root.val) and self.valid(root.right, root.val, high)
