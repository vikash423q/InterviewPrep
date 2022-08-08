from typing import Optional


#   https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nmap = {}

        temp = head
        h = cpy = Node(0)
        nmap[temp] = cpy
        while temp:
            cpy.next = Node(temp.val)
            cpy = cpy.next
            nmap[temp] = cpy
            temp = temp.next

        temp = head
        cpy = h.next
        while temp:
            cpy.random = nmap.get(temp.random)
            temp = temp.next
            cpy = cpy.next

        return h.next
