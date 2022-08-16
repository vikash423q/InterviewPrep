from typing import Optional

#   https://leetcode.com/problems/kth-smallest-element-in-a-bst


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.node = None
        self.inorder(root, k)
        return self.node.val

    def inorder(self, root: Optional[TreeNode], k: int):
        if not root:
            return None

        self.inorder(root.left, k)
        self.i += 1
        if self.i == k:
            self.node = root
        self.inorder(root.right, k)
