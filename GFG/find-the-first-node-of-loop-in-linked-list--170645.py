class Node:
    def __init__(self, data: int):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def findFirstNode(self, head: Node):

        curr = head
        seen: set[Node] = {curr}

        while curr:
            curr = curr.next
            if curr in seen:
                return curr
            seen.add(curr)
        return None
