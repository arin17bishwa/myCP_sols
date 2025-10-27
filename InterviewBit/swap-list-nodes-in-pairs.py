from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, A: Optional[ListNode]) -> Optional[ListNode]:
        head = A
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        prev, a, b = dummy, head, head.next

        while a and b:
            tmp = b.next

            prev.next = b
            b.next = a
            a.next = tmp

            prev = a
            b = prev.next.next if prev.next else None
            a = prev.next

        return dummy.next
