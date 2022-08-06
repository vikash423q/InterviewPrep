from typing import Any, List


def binary_search(value: Any, arr: List[Any], start: int = 0, end: int = None):
    if end is None:
        end = len(arr)-1

    mid = start
    while start < end:
        mid = (start + end)//2

        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            start = mid+1
        else:
            end = mid

    return mid


def bisect_left(value: Any, arr: List[Any], start: int = 0, end: int = None):
    if end is None:
        end = len(arr)-1

    mid = start
    while start < end:
        mid = (start + end)//2

        if arr[mid] < value:
            start = mid+1
        elif arr[mid] >= value:
            end = mid

    return mid


def bisect_right(value: Any, arr: List[Any], start: int = 0, end: int = None):
    if end is None:
        end = len(arr)-1

    mid = start
    while start < end:
        mid = (start + end)//2

        if arr[mid] <= value:
            start = mid+1
        elif arr[mid] > value:
            end = mid

    return mid


if __name__ == '__main__':
    a = [1, 2, 4, 5, 5, 5, 5, 5, 6, 7, 7, 9]

    print(binary_search(5, a))
    print(bisect_left(5, a))
    print(bisect_right(5, a))
