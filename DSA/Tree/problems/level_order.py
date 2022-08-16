from typing import Optional, List

#   https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lvl = [root]
        ans = [[root.val]]

        while lvl:
            new_lvl = []
            for node in lvl:
                if node.left:
                    new_lvl.append(node.left)
                if node.right:
                    new_lvl.append(node.right)

            if new_lvl:
                ans.append([node.val for node in new_lvl])
            lvl = new_lvl

        return ans

