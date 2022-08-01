from typing import Any


class Stack:
    def __init__(self):
        self._list = []

    def push(self, value: Any):
        self._list.append(value)

    def pop(self):
        last = self._list[-1] if self._list else None
        self._list = self._list[:-1]
        return last

    def top(self):
        return self._list[-1] if self._list else None


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(1)
    s.push(8)
    s.push(0)

    print(s.top())

    for _ in range(5):
        print(s.pop())
