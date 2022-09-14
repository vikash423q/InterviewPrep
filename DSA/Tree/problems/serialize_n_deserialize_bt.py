import json


#   https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.t = []
        self.traverse(root)
        return json.dumps(self.t)

    def traverse(self, root):
        if not root:
            self.t.append(None)
            return
        self.t.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        d = json.loads(data)
        pos = 0

        def fill():
            nonlocal pos

            if pos >= len(d) or d[pos] is None:
                pos += 1
                return None

            root = TreeNode(d[pos])
            pos += 1
            root.left = fill()
            root.right = fill()
            return root

        t = fill()
        return t

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
