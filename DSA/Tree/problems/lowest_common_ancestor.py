#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left = self.find(root.left, p) or self.find(root.left, q)
        right = self.find(root.right, q) or self.find(root.right, p)

        if left != right and left and right:
            return root

        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)

    def find(self, root: 'TreeNode', n: 'TreeNode'):
        if not root:
            return None
        elif root.val == n.val:
            return root
        elif root.val > n.val:
            return self.find(root.left, n)
        else:
            return self.find(root.right, n)