import dataclasses

from typing import Any, Iterable, Optional


@dataclasses.dataclass
class Node:
    value: Any = None
    left: 'Node' = None
    right: 'Node' = None

    @property
    def leaf(self) -> bool:
        return not self.left and not self.right


class Tree:
    def __init__(self, root_value: Any = None):
        self.root = Node(root_value)

    @property
    def height(self):
        return self.__height(self.root)

    def __height(self, temp: Node):
        if not temp or temp.value or temp.leaf:
            return 0
        left_height = self.__height(temp.left)
        right_height = self.__height(temp.right)
        return max(left_height, right_height) + 1

    def create(self, values: Iterable):
        for value in values:
            self.insert(value)

    def insert(self, value: Any):
        self.root = self.__insert_at_step(self.root, value)

    def __insert_at_step(self, temp: Node, value: Any):
        if temp is None or temp.value is None:
            return Node(value)
        elif value < temp.value:
            temp.left = self.__insert_at_step(temp.left, value)
        else:
            temp.right = self.__insert_at_step(temp.right, value)
        return temp

    def search(self, value: Any) -> Optional[Node]:
        temp = self.root
        while temp and temp.value != value:
            temp = temp.left if value < temp.value else temp.right

        if temp and temp.value == value:
            return temp

    def remove(self, value: Any):
        self.remove_at_step(self.root, value)

    def remove_at_step(self, temp: Node, value: Any) -> Optional[Node]:
        if temp is None:
            return temp

        if value < temp.value:
            temp.left = self.remove_at_step(temp.left, value)
        elif value > temp.value:
            temp.right = self.remove_at_step(temp.right, value)
        else:
            # leaf node
            if not temp.right and not temp.left:
                return None
            # only left node exists
            elif not temp.right:
                return temp.left
            # only right node exists
            elif not temp.left:
                return temp.right
            # both node exists
            else:
                min_at_right = temp.right
                while min_at_right.left:
                    min_at_right = min_at_right.left

                temp.value = min_at_right.value
                temp.right = self.remove_at_step(temp.right, temp.value)
        return temp

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __inorder(self, temp: Node):
        if not temp:
            return
        self.__inorder(temp.left)
        print(temp.value, end=" ")
        self.__inorder(temp.right)

    def preorder(self):
        self.__preorder(self.root)
        print()

    def __preorder(self, temp: Node):
        if not temp:
            return
        print(temp.value, end=" ")
        self.__preorder(temp.left)
        self.__preorder(temp.right)

    def postorder(self):
        self.__postorder(self.root)
        print()

    def __postorder(self, temp: Node):
        if not temp:
            return
        self.__postorder(temp.left)
        self.__postorder(temp.right)
        print(temp.value, end=" ")

    def level_order(self):
        level = [self.root]

        while level:
            next_level = []
            for temp in level:
                print(temp.value, end=" ")
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            level = next_level
        print()


if __name__ == "__main__":
    """
                    5
            1             6
                    4          8
            2                       10
                               9          12
                                    11      
    """
    t = Tree(5)
    t.create([6, 1, 4, 2, 8, 10, 12, 11, 9])

    t.inorder()
    t.preorder()
    t.postorder()
    t.level_order()

    print(bool(t.search(8)))
    print(bool(t.search(3)))
    t.remove(2)
    t.remove(12)
    t.remove(8)
    t.remove(5)
    t.remove(6)
