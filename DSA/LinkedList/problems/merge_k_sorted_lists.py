from typing import List, Optional
from math import inf


#   https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[ i +1] if i+ 1 < len(lists) else None

                if not right:
                    merged = left
                elif not left:
                    merged = right
                else:
                    merged = self.merge2Lists(left, right)
                merged_lists.append(merged)
            lists = merged_lists

        return lists[0]

    def merge2Lists(self, l1, l2):
        if not l1 and not l2:
            return
        if not l2:
            return l1
        if not l1:
            return l2

        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1, l2.next)
            return l2
