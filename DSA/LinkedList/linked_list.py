from typing import Any


class Node:
    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: 'Node' = None


class LinkedList:
    def __init__(self):
        self.head = None

    @property
    def size(self):
        temp = self.head
        i = 0
        while temp is not None:
            temp = temp.next
            i += 1
        return i

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" => ")
            temp = temp.next
        print("End")

    def insert(self, value: Any):
        temp = self.head
        if not self.head:
            self.head = Node(value)
            return

        while temp.next is not None:
            temp = temp.next

        temp.next = Node(value)

    def insert_at_idx(self, value: Any, idx: int):
        if idx == 0:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head

        i = 0
        temp = self.head
        while temp is not None:
            if i == idx-1:
                new_node = Node(value)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            i += 1

    def search(self, value: Any) -> bool:
        temp = self.head

        while temp is not None:
            if temp.value == value:
                return temp
            temp = temp.next

    def remove(self, value: Any):
        temp = self.head

        while temp is not None:
            if temp.next and temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    def remove_at_index(self, idx: int):
        if idx == 0 and self.head:
            self.head = self.head.next

        i = 0
        temp = self.head
        while temp is not None:
            if i == idx-1 and temp.next:
                temp.next = temp.next.next
                return
            i += 1
            temp = temp.next


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert(5)
    ll.insert(1)
    ll.insert(3)
    ll.insert(10)
    ll.insert(23)

    ll.print()
    print(ll.size)

    print(bool(ll.search(5)))
    print(ll.search(6))

    ll.remove(10)
    ll.print()
    ll.remove(10)
    ll.print()

    ll.remove_at_index(0)
    ll.print()
    ll.insert(90)
    ll.print()
    ll.remove_at_index(3)
    ll.print()

    ll.insert(31)
    ll.insert(17)
    ll.insert(21)

    ll.print()

    ll.insert_at_idx(43, 0)
    ll.print()
    ll.insert_at_idx(78, 3)
    ll.print()
    ll.insert_at_idx(11, 8)
    ll.print()

    print(ll.size)
