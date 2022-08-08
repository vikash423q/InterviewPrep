from typing import Optional


#   https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        idx = self.rem(head, n)
        if idx == n:
            head = head.next
        return head

    def rem(self, head, n):
        if not head:
            return 0

        idx = 1 + self.rem(head.next, n)
        if idx == n + 1:
            head.next = head.next.next
        return idx


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, ListNode(next=head)

        for i in range(n):
            fast = fast.next

        if not fast:
            head = head.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
