from typing import Any, List


def swap(items, idx1, idx2):
    temp = items[idx1]
    items[idx1] = items[idx2]
    items[idx2] = temp


def sort(items: List[Any]):
    if len(items) <= 1:
        return items

    pivot_idx = len(items) - 1
    i, mid = 0, 0
    while i < pivot_idx:
        if items[pivot_idx] > items[i]:
            swap(items, i, mid)
            mid += 1
        i += 1

    swap(items, mid, pivot_idx)
    items[:mid] = sort(items[:mid])
    items[mid+1:] = sort(items[mid+1:])
    return items


if __name__ == "__main__":
    _list = [3, 1, 5, 1, 9, 34, 21, 73, 32, 77, 12, 43, 7, 4]
    print(sort(_list))
