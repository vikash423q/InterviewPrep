from typing import Optional


#   https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#   merge with while loop
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        h = temp = ListNode()

        while h1 and h2:
            if h1.val < h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            temp = temp.next

        while h1:
            temp.next = h1
            h1 = h1.next
            temp = temp.next

        while h2:
            temp.next = h2
            h2 = h2.next
            temp = temp.next

        return h.next


#   merge with recursive approach
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        self.merge(h, list1, list2)
        return h.next

    def merge(self, h: ListNode, h1: Optional[ListNode], h2: Optional[ListNode]):
        if h1 and h2:
            if h1.val < h2.val:
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next

        elif h1:
            h.next = h1
            h1 = h1.next

        elif h2:
            h.next = h2
            h2 = h2.next

        else:
            return None

        self.merge(h.next, h1, h2)

