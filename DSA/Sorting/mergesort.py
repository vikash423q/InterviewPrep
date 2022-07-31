from typing import Any, List


def sort(items: List[Any]):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = sort(items[:mid])
    right = sort(items[mid:])
    return merge(left, right)


def merge(list1: List[Any], list2: List[Any]):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


if __name__ == "__main__":
    _list = [3, 1, 5, 1, 9, 34, 21, 73, 32, 77, 12, 43, 7, 4]
    print(sort(_list))
