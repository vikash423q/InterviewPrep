from DSA.Tree.node_based.tree import Tree, Node


class ViewTree(Tree):
    def left_view(self):
        self._left_view(self.root, {}, 0)

    def _left_view(self, temp: Node, saved: dict, level):
        if not temp:
            return
        if level not in saved:
            print(temp.value)
            saved[level] = temp.value

        self._left_view(temp.left, saved, level + 1)
        self._left_view(temp.right, saved, level + 1)

    def right_view(self):
        self._right_view(self.root, {}, 0)

    def _right_view(self, temp: Node, saved, level):
        if not temp:
            return
        if level not in saved:
            print(temp.value)
            saved[level] = temp.value

        self._right_view(temp.right, saved, level + 1)
        self._right_view(temp.left, saved, level + 1)

    def top_view(self):
        saved = {}
        self._top_view(self.root, saved, 0, 0)
        idx = 0
        while idx in saved:
            idx -= 1
        idx += 1

        while idx in saved:
            print(saved[idx][1], end=" ")
            idx += 1
        print()

    def _top_view(self, temp: Node, saved, col, lvl):
        if not temp:
            return

        self._top_view(temp.left, saved, col - 1, lvl + 1)

        if col not in saved:
            saved[col] = (lvl, temp.value)
        else:
            if lvl < saved[col][0]:
                saved[col] = (lvl, temp.value)

        self._top_view(temp.right, saved, col + 1, lvl + 1)

    def bottom_view(self):
        saved = {}
        self._bottom_view(self.root, saved, 0, 0)
        idx = 0
        while idx in saved:
            idx -= 1
        idx += 1

        while idx in saved:
            print(saved[idx][1], end=" ")
            idx += 1
        print()

    def _bottom_view(self, temp: Node, saved, col, lvl):
        if not temp:
            return

        self._bottom_view(temp.left, saved, col - 1, lvl + 1)

        if col not in saved:
            saved[col] = (lvl, temp.value)
        else:
            if lvl > saved[col][0]:
                saved[col] = (lvl, temp.value)

        self._bottom_view(temp.right, saved, col + 1, lvl + 1)


if __name__ == "__main__":
    t = ViewTree(5)
    t.create([6, 1, 4, 2, 8, 10, 12, 11, 9])

    t.inorder()

    # t.left_view()
    # t.right_view()
    t.top_view()
    t.bottom_view()
