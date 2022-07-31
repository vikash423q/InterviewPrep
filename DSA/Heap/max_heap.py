from typing import Any


def parent(idx):
    return (idx - 1) // 2


class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, value: Any):
        self._heap.append(value)
        self._heapify_up()

    def pop(self):
        if not self._heap:
            return None
        value = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heapify_down()
        return value

    def _heapify_down(self, idx: int = None):
        idx = 0 if idx is None else idx
        left, right = idx*2 + 1, idx*2 + 2
        largest_idx = None
        if left < len(self._heap):
            largest_idx = left
        if right < len(self._heap):
            largest_idx = left if self._heap[left] > self._heap[right] else right

        if largest_idx and self._heap[largest_idx] > self._heap[idx]:
            self._heap[idx], self._heap[largest_idx] = self._heap[largest_idx], self._heap[idx]
            self._heapify_down(largest_idx)

    def _heapify_up(self, idx: int = None):
        if idx is None:
            idx = len(self._heap) - 1
        elif idx <= 0:
            return
        if self._heap[idx] > self._heap[parent(idx)]:
            self._heap[idx], self._heap[parent(idx)] = self._heap[parent(idx)], self._heap[idx]
            self._heapify_up(parent(idx))


if __name__ == '__main__':
    heap = MaxHeap()

    def add():
        heap.push(5)
        heap.push(0)
        heap.push(2)
        heap.push(11)
        heap.push(7)
        heap.push(8)
        heap.push(3)
        heap.push(4)

    add()

    print(heap._heap)
    for _ in range(len(heap._heap)):
        print(heap.pop(), end=" ")

