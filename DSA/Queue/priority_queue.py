from typing import Any

from DSA.Queue.queue import Queue


class PriorityQueue(Queue):
    def enqueue(self, value: Any):
        # increase queue size by 1
        self._list.append(value)

        # find appropriate index for value
        i = len(self._list) - 1
        while i > 0 and value < self._list[i-1]:
            i -= 1

        # place value at right position
        temp = self._list[i]
        self._list[i] = value

        # shift every other element 1 position to the right
        while i < len(self._list) - 1:
            next_temp = self._list[i + 1]
            self._list[i + 1] = temp
            temp = next_temp
            i += 1


if __name__ == "__main__":
    q = PriorityQueue()

    q.enqueue(14)
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



