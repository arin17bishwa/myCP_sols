from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return
        dummy = Node(0)
        curr = head

        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt)
            curr = curr.next.next

        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        copy_header = Node(0)
        copy_curr = copy_header

        curr = head
        while curr:
            copy_curr.next = curr.next
            curr = curr.next.next
            copy_curr = copy_curr.next
        return copy_header.next
