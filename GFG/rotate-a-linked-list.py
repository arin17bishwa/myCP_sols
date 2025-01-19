from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Optional[Node] = None


class Solution:
    def rotate(self, head: Optional[Node], k: int):
        n = self.length_of_ll(head)
        k %= n
        if k == 0:
            return head

        fast = head
        prev: Optional[Node] = None
        for _ in range(k):
            prev = fast
            fast = fast.next
        prev.next = None
        new_head = fast
        while fast and fast.next:
            fast = fast.next

        fast.next = head
        return new_head

    @staticmethod
    def length_of_ll(head: Optional[Node]) -> int:
        ans = 0
        while head:
            head = head.next
            ans += 1
        return ans
