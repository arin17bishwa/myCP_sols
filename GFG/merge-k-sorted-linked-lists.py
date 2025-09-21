import heapq
from typing import Optional


class Node:
    def __init__(self, x: int):
        self.data: int = x
        self.next: Optional[Node] = None


class Solution:
    def mergeKLists(self, arr: list[Node]) -> Node:
        sentry = Node(0)
        curr = sentry
        heap: list[tuple[int, Node]] = [(node.data, node) for node in arr]
        heapq.heapify(heap)
        while heap:
            _, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.data, node.next))
            curr.next = node
            curr = curr.next
        return sentry.next
