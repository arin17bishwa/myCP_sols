from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        copy_curr = dummy
        curr = head
        copy_mapping: dict[Node | None, Node | None] = {}
        while curr:
            new_node = Node(curr.val)
            copy_mapping[curr] = new_node
            copy_curr.next = new_node
            curr = curr.next
            copy_curr = copy_curr.next

        curr = head
        curr_copy = dummy.next
        while curr:
            if curr.random:
                curr_copy.random = copy_mapping[curr.random]
            curr = curr.next
            curr_copy = curr_copy.next

        return dummy.next
