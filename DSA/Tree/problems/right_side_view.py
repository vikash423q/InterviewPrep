from typing import Optional, List

#   https://leetcode.com/problems/binary-tree-right-side-view


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view = [0 ] *self.height(root)
        self.traverse(root, view)
        return view

    def traverse(self, root: Optional[TreeNode], view: list, h: int = 0):
        if not root:
            return

        view[h] = root.val

        self.traverse(root.left, view, h+ 1)
        self.traverse(root.right, view, h + 1)

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
