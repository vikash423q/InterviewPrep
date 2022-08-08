from typing import Optional


#   https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        n = len(stack)

        temp = head
        for i in range(n // 2):
            end = stack.pop()
            end.next = temp.next
            print(temp.val, end.val)
            temp.next = end
            temp = temp.next.next

        return head

