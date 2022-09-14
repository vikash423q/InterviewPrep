from typing import List, Optional


#   https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(low: int, high: int):
            nonlocal i

            if i >= len(preorder) or low > high:
                return

            root = TreeNode(preorder[i])
            i += 1

            if low == high:
                return root

            val_i = idx[preorder[i]]
            root_i = idx[root.val]

            root.left = build(low, root_i - 1)
            root.right = build(root_i + 1, high)
            return root

        i = 0
        visited = [1] * len(inorder)
        root = TreeNode(preorder[0])
        idx = {val: i for i, val in enumerate(inorder)}
        root = build(i, len(inorder) - 1)
        return root
