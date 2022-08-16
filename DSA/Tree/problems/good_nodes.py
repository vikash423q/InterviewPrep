#   https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)

    def count(self, root: TreeNode, high: int) -> int:
        if not root:
            return 0

        good = 1 if root.val >= high else 0
        high = max(high, root.val)

        return good + self.count(root.left, high) + self.count(root.right, high)
