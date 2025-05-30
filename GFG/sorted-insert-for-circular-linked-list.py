from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None


class Solution:
    def sortedInsert(self, head: Node, data: int) -> Node:
        new_node = Node(data)
        sentry = Node(-1)
        sentry.next = head
        curr = head.next
        prev = head

        while True:
            if prev.data <= curr.data:
                if prev.data <= data <= curr.data:
                    prev.next = new_node
                    new_node.next = curr
                    return sentry.next
            else:
                prev.next = new_node
                new_node.next = head
                if data<head.data:
                    sentry.next = new_node
                return sentry.next
            prev = curr
            curr = curr.next
