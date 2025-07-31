from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = ListNode(0)
        prev.next = head

        sentry = prev
        first: ListNode = head
        second: Optional[ListNode] = first.next
        while first and first.next:
            second = first.next
            third: Optional[ListNode] = second.next
            second.next = first
            first.next = third
            prev.next = second
            first, prev = third, first
        return sentry.next
