from DSA.Tree.node_based.tree import Tree, Node


# assuming val1 and val2 always exists
def lca(root: Node, val1, val2):
    if root.value in [val1, val2]:
        return root

    left = find_node(root.left, val1)
    right = find_node(root.right, val2)

    if left and right:
        return root

    if left:
        return lca(root.left, val1, val2)
    elif right:
        return lca(root.right, val1, val2)
    else:
        return None


def find_node(root: Node, val):
    if root is None:
        return None
    if root.value == val:
        return root

    left = find_node(root.left, val)
    right = find_node(root.right, val)

    if left:
        return left
    if right:
        return right


if __name__ == '__main__':
    """
                     5
                1          6
                     4          8
                2                   10
                               9          12
                                    11          14
    """
    t = Tree()
    t.create([5, 6, 1, 4, 2, 8, 10, 12, 14, 11, 9])

    t.inorder()
    t.preorder()

    r = lca(t.root, 11, 14)
    print(r.value)
