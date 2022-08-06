from typing import Any, List


def quick_select(k: int, arr: List[Any], start: int = 0, end: int = None):
    if end is None:
        end = len(arr) - 1

    if start > end:
        return None

    pivot = end
    i = part = start
    while i < end:
        if arr[i] < arr[pivot]:
            arr[i], arr[part] = arr[part], arr[i]
            part += 1
        i += 1

    arr[pivot], arr[part] = arr[part], arr[pivot]

    if part == k-1:
        return arr[part]
    elif part > k-1:
        return quick_select(k, arr, start, part-1)
    else:
        return quick_select(k, arr, part+1, end)


if __name__ == "__main__":
    a = [4, 1, 6, 4, 7, 8, 10, 33, 21, 56, 78, 32]
    print(quick_select(1, a))
