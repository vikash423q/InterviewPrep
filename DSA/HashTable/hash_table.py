from typing import Any, List, Optional

from DSA.LinkedList.linked_list import LinkedList


class HashTable:
    def __init__(self):
        self._list: List[Optional[LinkedList]] = [None for _ in range(1000)]

    def put(self, key: Any, value: Any):
        idx = hash(key) % len(self._list)
        if self._list[idx] is None:
            self._list[idx] = LinkedList()
        self._list[idx].insert((key, value))

    def get(self, key: Any):
        idx = hash(key) % len(self._list)
        if self._list[idx] is None:
            return None
        temp = self._list[idx].head

        while temp is not None:
            if temp.value[0] == key:
                return temp.value[1]
            temp = temp.next


if __name__ == "__main__":
    ht = HashTable()

    ht.put("bob", "marley")
    ht.put("top", "gun")
    ht.put("vikash", "gaurav")
    ht.put(None, "bbbb")

    print(ht.get("top"))
    print(ht.get("vikash"))
    print(ht.get("rohit"))
    print(ht.get(None))
