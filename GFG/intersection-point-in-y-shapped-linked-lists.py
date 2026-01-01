class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def intersectPoint(self, head1: Node, head2: Node) -> Node:
        seen: set[Node] = set()

        curr = head1
        while curr:
            seen.add(curr)
            curr = curr.next

        curr = head2

        while curr not in seen:
            curr = curr.next

        return curr
