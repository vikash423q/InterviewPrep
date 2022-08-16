from typing import Optional

#   https://leetcode.com/problems/reverse-nodes-in-k-group


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ref = trail = lead = ListNode(next=head)

        i = 0
        while lead and i < k:
            lead = lead.next
            i += 1

        while lead:
            trail.next, lead = self.reverse(trail.next, lead.next)

            n = 0
            while lead and n < k:
                lead = lead.next
                trail = trail.next
                n += 1

        return ref.next

    def reverse(self, head, tail):
        prev = None
        curr = head
        nxt_ref = tail
        while curr != tail:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = nxt_ref
        return prev, head

