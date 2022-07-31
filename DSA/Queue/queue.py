from typing import Any


class Queue:
    def __init__(self):
        self._list = []

    def enqueue(self, value: Any):
        self._list.append(value)

    def dequeue(self):
        top = self._list[0] if self._list else None
        self._list = self._list[1:]
        return top

    def peek(self):
        return self._list[0] if self._list else None

    def print(self):
        print(self._list)


if __name__ == "__main__":
    q = Queue()

    q.enqueue(9)
    q.enqueue(12)
    q.enqueue(10)

    q.print()

    print(q.dequeue())
    print(q.peek())
    print(q.dequeue())
    q.print()
    print(q.dequeue())
    q.print()
    print(q.peek())



