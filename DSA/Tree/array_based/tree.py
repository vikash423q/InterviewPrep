from typing import Any, Iterable, Optional


def parent(idx: int):
    return idx // 2


def left_child(idx: int):
    return idx * 2 + 1


def right_child(idx: int):
    return idx * 2 + 2


class Tree:
    def __init__(self, root_value: Any = None):
        self._list = []
        if root_value:
            self._list.append(root_value)

    def create(self, values: Iterable):
        for value in values:
            self.insert(value)

    def insert(self, value: Any):
        self.__insert_at_idx(value, 0)

    def __insert_at_idx(self, value: Any, idx: int):
        if idx >= len(self._list):
            self._list += [None for _ in range(idx-len(self._list)+1)]

        if self._list[idx] is None:
            self._list[idx] = value
        elif value < self._list[idx]:
            self.__insert_at_idx(value, left_child(idx))
        else:
            self.__insert_at_idx(value, right_child(idx))

    def search(self, value: Any) -> Optional[int]:
        idx = 0
        while idx < len(self._list) or self._list[idx] != value:
            if self._list[idx] is None:
                break
            elif value < self._list[idx]:
                idx = left_child(idx)
            elif value > self._list[idx]:
                idx = right_child(idx)
            else:
                return idx
        return None

    def remove(self, value: Any):
        print("removing ", value)
        self.__remove_step(value, 0)

    def __remove_step(self, value, idx):
        if idx >= len(self._list) or self._list[idx] is None:
            return
        # value is lesser than current node, go left
        if value < self._list[idx]:
            self.__remove_step(value, left_child(idx))
        # value is greater than current node, go right
        elif value > self._list[idx]:
            self.__remove_step(value, right_child(idx))
        # value match found, remove this node
        else:
            lft_child = self._list[left_child(idx)] if left_child(idx) < len(self._list) else None
            rgt_child = self._list[right_child(idx)] if right_child(idx) < len(self._list) else None

            # has both child
            if lft_child and rgt_child:
                # find min value on right subtree
                i = right_child(idx)
                while i < len(self._list) and self._list[i] is not None:
                    i = left_child(i)
                min_idx = i if self._list[i] is not None else right_child(idx)

                # replacing with min value index, and removing min value index recursively
                self._list[idx] = self._list[min_idx]
                self.__remove_step(self._list[min_idx], min_idx)

            # only left child
            elif lft_child:
                self._list[idx] = lft_child
                self.__remove_step(lft_child, left_child(idx))
            # only right child
            elif rgt_child:
                self._list[idx] = rgt_child
                self.__remove_step(rgt_child, right_child(idx))
            # no child
            else:
                self._list[idx] = None

    def inorder(self):
        self.__inorder(0)
        print()

    def __inorder(self, idx):
        if idx >= len(self._list) or not self._list[idx]:
            return
        self.__inorder(left_child(idx))
        print(self._list[idx], end=" ")
        self.__inorder(right_child(idx))

    def preorder(self):
        self.__preorder(0)
        print()

    def __preorder(self, idx):
        if idx >= len(self._list) or not self._list[idx]:
            return
        print(self._list[idx], end=" ")
        self.__preorder(left_child(idx))
        self.__preorder(right_child(idx))

    def postorder(self):
        self.__postorder(0)
        print()

    def __postorder(self, idx):
        if idx >= len(self._list) or not self._list[idx]:
            return
        self.__postorder(left_child(idx))
        self.__postorder(right_child(idx))
        print(self._list[idx], end=" ")


if __name__ == "__main__":
    """
                    5
            1             6
                 4             8
             2                       10
                               9          12
                                     11      
    """
    t = Tree(5)
    t.create([6, 1, 4, 2, 8, 10, 12, 11, 9])

    t.inorder()
    t.preorder()
    t.postorder()

    print(bool(t.search(8)))
    print(bool(t.search(3)))
    t.remove(2)
    t.inorder()
    t.remove(12)
    t.inorder()
    t.remove(8)
    t.inorder()
    t.remove(5)
    t.inorder()
    t.remove(6)
    t.inorder()
