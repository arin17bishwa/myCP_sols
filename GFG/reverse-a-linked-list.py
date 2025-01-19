from typing import Optional


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head: Optional[Node]):
        last_node: Optional[Node] = None

        def func(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return node
            after_current = func(node.next)
            if after_current:
                after_current.next = node
            else:
                nonlocal last_node
                last_node = node
            node.next = None
            return node

        func(head)
        return last_node
